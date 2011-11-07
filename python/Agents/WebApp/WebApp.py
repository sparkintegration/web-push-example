"""
*****************************************************************************
* Copyright (c) 2011 Spark Integration Technologies, Inc. All rights reserved.
******************************************************************************

    Automatically generated agent file.  Changes to this file will not be
    overwritten.  If this file exists, generating new code will create
    a file with .new appended to it instead.

    WebApp

    
	Code generated at: May 14 2011 22:56:35 
	Database: sqlite:////Volumes/SPARK/git/distrix/Configuration/WebDemo.db

******************************************************************************
* This file contains trade secrets of Spark Integration Technologies. No part
* may be reproduced or transmitted in any form by any means or for any purpose
* without the express written permission of Spark Integration Technologies.
*****************************************************************************
"""

import logging
log = logging.getLogger("WebApp")

from BaseWebApp import BaseWebApp

import cherrypy
import threading

notification_cv = threading.Condition()
current_notification = None

class WebAppAgent(BaseWebApp):
    def __init__(self):
        super(WebAppAgent, self).__init__()

    def pre_agent_init(self):
        #Called before any model publications or subscriptions are setup
        pass

    def initial_state_setup(self):
        #Set up any values for named objects here if desired, before they are published
        pass
    
    def on_agent_init(self):
        #This function can be used to perform any initialization when the agent starts
        #(it will be called after the models are initialized)
        pass

    def timing_action(self):
        pass

    def handle_notification_creation(self, proxy):
        global current_notification
        log.info("Notification: %s" % proxy.name)
        log.info(proxy.data)
        
        # Notify any listening webapp threads that there is a new notification
        notification_cv.acquire()
        current_notification = proxy
        notification_cv.notifyAll()
        notification_cv.release()

class WebApp(object):
    def index(self):
        f = open("index.html", "r")
        return f.read()
    index.exposed = True
    
    def get_notification(self, _):
        # Block until a notification is received then return it
        notification_cv.acquire()
        notification_cv.wait()
        notification_cv.release()
        return "<b>%s</b><br/>%s" % (current_notification.name, current_notification.data)
    get_notification.exposed = True

def main():
    # Start the web server
    cherrypy.tree.mount(WebApp(), '/')
    cherrypy.engine.start()
    
    # Start the agent
    agent = WebAppAgent()
    agent.run()
    
if __name__=="__main__":
    logging.basicConfig()
    for handler in logging.getLogger().handlers:
        handler.setFormatter(logging.Formatter("%(name)s: %(message)s"))
    logging.getLogger().setLevel(logging.WARNING)
    main()

