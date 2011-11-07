"""
*****************************************************************************
* Copyright (c) 2011 Spark Integration Technologies, Inc. All rights reserved.
******************************************************************************

    Automatically generated model file.  Changes to this file will be
    overwritten.  If you wish to modify this model, please subclass
    it instead.

    Model type name: RootNode

    

	notification_obj = self.root.notifications.get_notification() #Get a reference to the first object
	...or...
	notification_obj = self.root.notifications.get_notification(n) #Get a reference to the n'th object
	notification_obj.<field_name> = 43 #Do stuff to the object
	notification_obj.commit() #Publish the state of the object when you're done
	...or...
	self.root.notifications.set_notification(notification_obj) #Alternate method of comitting object
	notification_list = self.root.notifications.notification_list #Get the list of anonymous objects
	notification_obj = Notification() # Create a new anonymous object
	self.root.notifications.set_notification(notification_obj) #Add it to the list of anonymous objects and commit it
	
	
	
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
            
    
            self.notification_error_callback = lambda obj: None
            
    
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
            
            self.notification_list = []
            return
    
        def handle_notification_error(self, obj):
            if obj in self.notification_list:
                self.notification_list.remove(obj)
            self.notification_error_callback(obj)
    
        def get_notification(self, index = 0):
            return self.notification_list[index]
        
        def get_notification_count(self):
            return len(self.notification_list)
            
        def set_notification(self, obj):
            if obj not in self.notification_list:
                self.notification_list.append(obj)
            obj.commit()
            
        def add_notification(self):
            path = self.get_path() + "/"
            obj = Notification("%s" % path, self.objects_module.unsaved, self.handle_notification_error)
            obj.dataset_flags = 0 | (obj.dataset_flags & ~obj.flagtypes.prioritymask)
            obj.object_flags = 0
            self.notification_list.append(obj)
            return obj
        
    
    
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

    



