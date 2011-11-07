"""
*****************************************************************************
* Copyright (c) 2011 Spark Integration Technologies, Inc. All rights reserved.
******************************************************************************

    Automatically generated model file.  Changes to this file will be
    overwritten.  If you wish to modify this model, please subclass
    it instead.

    Model type name: RootNode

    

	notification_proxy_list = self.root.notifications.notification_proxies #Access the list of anonymous Notification objects
	notification_proxy.<field_name> #Access a field from the Notification object
	
	
	Code generated at: May 14 2011 22:56:35 
	Database: sqlite:////Volumes/SPARK/git/distrix/Configuration/WebDemo.db

******************************************************************************
* This file contains trade secrets of Spark Integration Technologies. No part
* may be reproduced or transmitted in any form by any means or for any purpose
* without the express written permission of Spark Integration Technologies.
*****************************************************************************
"""

from objects.Notification import Notification

class RootNode:
    class NotificationsNode:
        def __init__(self, objects_module, parent=None):
            self.objects_module = objects_module
            self._node_name = "Notifications"
            self.parent = parent
            
    
            
            self.notification_proxies = []
            self.notification_creation_callback = lambda proxy: None
            self.notification_change_callback = lambda proxy: None
            self.notification_deletion_callback = lambda proxy: None
            self.notification_abandonment_callback = lambda proxy: None
            self.notification_adoption_callback = lambda proxy: None
    
        def _get_node_name(self):
            return self._node_name
        
        def _set_node_name(self, name):
            self._node_name = name
        node_name = property(_get_node_name, _set_node_name)
        
        def _get_parent(self):
            return self._parent
            
        def _set_parent(self, parent):
            self._parent = parent
        parent = property(_get_parent, _set_parent)
        
        def get_path(self):
            node_names = []
            n = self
            while n:
                node_names.append(n.node_name)
                n = n.parent
            return "/" + "/".join(reversed(node_names))
    
        def initial_commits(self):
            return
    
        def setup_pubsub(self):
            path = self.get_path() + "/"
            
            self.objects_module.subscribe(Notification, "%s" % path, self.handle_new_notification)
            return
    
        
        def handle_notification_deletion(self, proxy):
            if proxy in self.notification_proxies:
                self.notification_proxies.remove(proxy)
            self.notification_deletion_callback(proxy)
    
        def handle_new_notification(self, proxy):
            self.notification_proxies.append(proxy)
            proxy.state_change_callback = lambda proxy: self.notification_change_callback(proxy)
            proxy.deletion_callback = self.handle_notification_deletion
            proxy.orphan_callback = lambda proxy: self.notification_abandonment_callback(proxy)
            proxy.adoption_callback = lambda proxy: self.notification_adoption_callback(proxy)
            self.notification_creation_callback(proxy)
    
    
    def __init__(self, objects_module, parent=None):
        self.objects_module = objects_module
        self._node_name = "Root"
        self.parent = parent
        
        self.notifications = RootNode.NotificationsNode(objects_module, self)

        

    def _get_node_name(self):
        return self._node_name
    
    def _set_node_name(self, name):
        self._node_name = name
    node_name = property(_get_node_name, _set_node_name)
    
    def _get_parent(self):
        return self._parent
        
    def _set_parent(self, parent):
        self._parent = parent
    parent = property(_get_parent, _set_parent)
    
    def get_path(self):
        node_names = []
        n = self
        while n:
            node_names.append(n.node_name)
            n = n.parent
        return "/" + "/".join(reversed(node_names))

    def initial_commits(self):
        self.notifications.initial_commits()
        return

    def setup_pubsub(self):
        path = self.get_path() + "/"
        
        self.notifications.setup_pubsub()
        return

    



