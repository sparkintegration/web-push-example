"""
*****************************************************************************
* Copyright (c) 2011 Spark Integration Technologies, Inc. All rights reserved.
******************************************************************************

    Automatically generated agent file.  Changes to this file will not be
    overwritten.  If this file exists, generating new code will create
    a file with .new appended to it instead.

    NotificationGenerator

    
	Code generated at: May 14 2011 22:56:35 
	Database: sqlite:////Volumes/SPARK/git/distrix/Configuration/WebDemo.db

******************************************************************************
* This file contains trade secrets of Spark Integration Technologies. No part
* may be reproduced or transmitted in any form by any means or for any purpose
* without the express written permission of Spark Integration Technologies.
*****************************************************************************
"""
import sys
import logging
log = logging.getLogger("NotificationGenerator")

from BaseNotificationGenerator import BaseNotificationGenerator


class NotificationGenerator(BaseNotificationGenerator):
    def __init__(self, name, description):
        super(NotificationGenerator, self).__init__()
        self.name = name
        self.description = description

    def pre_agent_init(self):
        #Called before any model publications or subscriptions are setup
        pass

    def initial_state_setup(self):
        #Set up any values for named objects here if desired, before they are published
        pass
    
    def on_agent_init(self):
        #This function can be used to perform any initialization when the agent starts
        #(it will be called after the models are initialized)
        notification = self.root.notifications.add_notification()
        notification.name = self.name
        notification.data = self.description
        notification.commit()
        print "Notification sent"

    def timing_action(self):
        pass



def main():
    if len(sys.argv) < 3:
        print "Usage: %s <notification name> <notification description>" % sys.argv[0]
        sys.exit(1)
        
    agent = NotificationGenerator(sys.argv[1], sys.argv[2])
    
    agent.run()
    
if __name__=="__main__":
    logging.basicConfig()
    for handler in logging.getLogger().handlers:
        handler.setFormatter(logging.Formatter("%(name)s: %(message)s"))
    logging.getLogger().setLevel(logging.WARNING)
    main()

