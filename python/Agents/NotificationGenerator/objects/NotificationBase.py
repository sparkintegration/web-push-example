"""
*****************************************************************************
* Copyright (c) 2011 Spark Integration Technologies, Inc. All rights reserved.
******************************************************************************

    Automatically generated objects file.  Changes to this file *WILL* be
    overwritten.  If an object needs to be customized for this agent, edit the
    objects.py file.
	Code generated at: May 14 2011 22:56:35 
	Database: sqlite:////Volumes/SPARK/git/distrix/Configuration/WebDemo.db

******************************************************************************
* This file contains trade secrets of Spark Integration Technologies. No part
* may be reproduced or transmitted in any form by any means or for any purpose
* without the express written permission of Spark Integration Technologies.
*****************************************************************************
"""

from distrix import appmodules
from distrix.utils import DataStruct, SubscribableList




class Notification(appmodules.Objects.DistributedObject):
    type_data = ["Notification"]
    object_metadata = 'A[{"fields":[["name",["string"]],["data",["string"]]],"type":["Notification"],"methods":[]}]'
	
    class Data(DataStruct):
        _fields_ = [("name", DataStruct.d_string()),
                    ("data", DataStruct.d_string())]

    def __init__(self, *args, **kwargs):
        super(Notification, self).__init__(*args, **kwargs)
        self.data_struct = self.Data(self)
        self.metadata = self.object_metadata
        self.name = ""
        self.data = ""
        
    def serialize(self):
        return self.data_struct.serialize()
    
    def get_size(self):
        return self.data_struct.get_size()
    
    def deserialize(self, data):
        self.data_struct.deserialize(data)

    
    class Proxy(appmodules.Objects.DistributedObjectProxy):
        class Data(DataStruct):
            _fields_ = [("name", DataStruct.d_string()),
                    ("data", DataStruct.d_string())]

        def __init__(self, *args, **kwargs):
            super(Notification.Proxy, self).__init__(*args, **kwargs)
            self.data_struct = self.Data(self)
            self.name = ""
            self.data = ""
        
        def deserialize(self, data):
            self.data_struct.deserialize(data)

    
