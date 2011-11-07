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




class DX_AgentMetadata(appmodules.Objects.DistributedObject):
    type_data = ["DX_AgentMetadata"]
    object_metadata = 'A[{"fields":[["agentName",["string"]],["agentDescription",["string"]],["hostname",["string"]],["buildSystem",["string"]],["timingInterval",["uint32"]],["language",["string"]],["targetOs",["string"]],["protocols",["string"]]],"type":["DX_AgentMetadata"],"methods":[]}]'
	
    class Data(DataStruct):
        _fields_ = [("agentName", DataStruct.d_string()),
                    ("agentDescription", DataStruct.d_string()),
                    ("hostname", DataStruct.d_string()),
                    ("buildSystem", DataStruct.d_string()),
                    ("timingInterval", DataStruct.d_uint()),
                    ("language", DataStruct.d_string()),
                    ("targetOs", DataStruct.d_string()),
                    ("protocols", DataStruct.d_string())]

    def __init__(self, *args, **kwargs):
        super(DX_AgentMetadata, self).__init__(*args, **kwargs)
        self.data_struct = self.Data(self)
        self.metadata = self.object_metadata
        self.agentName = ""
        self.agentDescription = ""
        self.hostname = ""
        self.buildSystem = ""
        self.timingInterval = 0
        self.language = ""
        self.targetOs = ""
        self.protocols = ""
        
    def serialize(self):
        return self.data_struct.serialize()
    
    def get_size(self):
        return self.data_struct.get_size()
    
    def deserialize(self, data):
        self.data_struct.deserialize(data)

    
    class Proxy(appmodules.Objects.DistributedObjectProxy):
        class Data(DataStruct):
            _fields_ = [("agentName", DataStruct.d_string()),
                    ("agentDescription", DataStruct.d_string()),
                    ("hostname", DataStruct.d_string()),
                    ("buildSystem", DataStruct.d_string()),
                    ("timingInterval", DataStruct.d_uint()),
                    ("language", DataStruct.d_string()),
                    ("targetOs", DataStruct.d_string()),
                    ("protocols", DataStruct.d_string())]

        def __init__(self, *args, **kwargs):
            super(DX_AgentMetadata.Proxy, self).__init__(*args, **kwargs)
            self.data_struct = self.Data(self)
            self.agentName = ""
            self.agentDescription = ""
            self.hostname = ""
            self.buildSystem = ""
            self.timingInterval = 0
            self.language = ""
            self.targetOs = ""
            self.protocols = ""
        
        def deserialize(self, data):
            self.data_struct.deserialize(data)

    
