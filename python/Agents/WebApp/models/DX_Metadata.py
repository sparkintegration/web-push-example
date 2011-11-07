"""
*****************************************************************************
* Copyright (c) 2011 Spark Integration Technologies, Inc. All rights reserved.
******************************************************************************

    Automatically generated model file.  Changes to this file will be
    overwritten.  If you wish to modify this model, please subclass
    it instead.
	Code generated at: May 14 2011 22:56:35 
	Database: sqlite:////Volumes/SPARK/git/distrix/Configuration/WebDemo.db

******************************************************************************
* This file contains trade secrets of Spark Integration Technologies. No part
* may be reproduced or transmitted in any form by any means or for any purpose
* without the express written permission of Spark Integration Technologies.
*****************************************************************************
"""

import socket
import sys

from objects.DX_AgentMetadata import DX_AgentMetadata

class MetadataModelNode:
    def __init__(self, objects_module):
        self.objects_module = objects_module
        self.agentMetadata = DX_AgentMetadata("/DX_Metadata/", objects_module.cached, self.handle_agentMetadata_error);

        self.agentMetadata.language = "python"
        self.agentMetadata.targetOs = {'darwin':'OS X', 'win32':'Windows', 'linux2':'Linux'}.get(sys.platform, 'Unknown')
        self.agentMetadata.agentName = "WebApp"
        self.agentMetadata.buildSystem = "default"
        self.agentMetadata.agentDescription = ""
        self.agentMetadata.timingInterval = 1000
        self.agentMetadata.protocols = "[{\"certificate\": \"cert.pem\", \"protocol\": \"Local\", \"key\": \"key.pem\", \"serverPort\": \"23000\", \"memSize\": \"16777216\", \"cas\": \"CAs.pem\", \"encrypted\": 0}, {\"protocol\": \"TCP\", \"certificate\": \"cert.pem\", \"key\": \"key.pem\", \"cas\": \"CAs.pem\", \"encrypted\": 0, \"targets\": [{\"ip\": \"127.0.0.1\", \"port\": \"21000\"}]}, {\"protocol\": \"IP\", \"localPort\": \"22000\", \"certificate\": \"cert.pem\", \"cas\": \"CAs.pem\", \"encrypted\": 0, \"key\": \"key.pem\", \"multicastPort\": \"22001\", \"multicastGroup\": \"239.0.1.2\"}]"
        self.agentMetadata.hostname = socket.gethostname()
        
        self.agentMetadata.commit();
        self.agentMetadata_error_callback = lambda obj: None

    def handle_agentMetadata_error(self, obj):
        self.agentMetadata = None
        self.agentMetadata_error_callback(obj)
