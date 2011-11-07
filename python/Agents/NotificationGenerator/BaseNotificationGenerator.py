"""
*****************************************************************************
* Copyright (c) 2011 Spark Integration Technologies, Inc. All rights reserved.
******************************************************************************

    Automatically generated agent base file.  Changes to this file will be
    overwritten.

    NotificationGenerator

    
	Code generated at: May 14 2011 22:56:35 
	Database: sqlite:////Volumes/SPARK/git/distrix/Configuration/WebDemo.db

******************************************************************************
* This file contains trade secrets of Spark Integration Technologies. No part
* may be reproduced or transmitted in any form by any means or for any purpose
* without the express written permission of Spark Integration Technologies.
*****************************************************************************
"""



from distrix.agent import Agent
from distrix import protocols, appmodules

from models import DX_Metadata
from models import Root


class BaseNotificationGenerator(Agent):
    def __init__(self):
        super(BaseNotificationGenerator, self).__init__()
        self.timing_interval = 1.0
        self.name = "NotificationGenerator"
        

        localProtocol = protocols.Local()
        self.add_protocol(localProtocol)
        tcpProtocol = protocols.TCP()
        tcpProtocol.add_target("127.0.0.1", 21000)
        self.add_protocol(tcpProtocol)
        ipProtocol = protocols.IP()
        self.add_protocol(ipProtocol)
        
        # Set up any other app modules here
        self.objects_module = appmodules.Objects()
        self.add_app_module(self.objects_module)
        self.add_app_module(appmodules.ManagedProcess())
        
    def on_init(self):
        self.metadata_model = DX_Metadata.MetadataModelNode(self.objects_module)
        self.root = Root.RootNode(self.objects_module)
        self.pre_agent_init()
        self.root.setup_pubsub()
        
        self.initial_state_setup()
        self.root.initial_commits()
        
        self.on_agent_init()
        
    def initial_state_setup(self):
        pass
        
    def on_agent_init(self):
        pass
        
    def pre_agent_init(self):
        pass
