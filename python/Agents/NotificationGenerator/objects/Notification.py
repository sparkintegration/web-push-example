"""
*****************************************************************************
* Copyright (c) 2011 Spark Integration Technologies, Inc. All rights reserved.
******************************************************************************

    Automatically generated objects file.  Changes to this file will not be
    overwritten, and it should be used to customize the generated objects.
	Code generated at: May 14 2011 22:56:35 
	Database: sqlite:////Volumes/SPARK/git/distrix/Configuration/WebDemo.db

******************************************************************************
* This file contains trade secrets of Spark Integration Technologies. No part
* may be reproduced or transmitted in any form by any means or for any purpose
* without the express written permission of Spark Integration Technologies.
*****************************************************************************
"""

from distrix import appmodules
from distrix.utils import DataStruct
from NotificationBase import Notification



class Notification(Notification):
    def __init__(self, *args, **kwargs):
        super(Notification, self).__init__(*args, **kwargs)
    

    class Proxy(Notification.Proxy):    
        def __init__(self, *args, **kwargs):
            super(Notification.Proxy, self).__init__(*args, **kwargs)
    

