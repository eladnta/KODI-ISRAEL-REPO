# -*- coding: utf-8 -*-
'''
    Created on 21/01/2012

    Copyright (c) 2010-2012 Shai Bentin.
    All rights reserved.  Unpublished -- rights reserved

    Use of a copyright notice is precautionary only, and does
    not imply publication or disclosure.
 
    Licensed under Eclipse Public License, Version 1.0
    Initial Developer: Shai Bentin.

    @author: shai
'''

from APLoader import APLoader

class APEpgLoader(APLoader):
    '''
    classdocs
    '''
    EPG_URI = "v{{api_version}}/accounts/{{account_id}}/broadcasters/{{broadcaster_id}}/vod_items/{{item_id}}/epg"
    

    def __init__(self, settings, itemId = ''):
        '''
        Constructor
        '''
        super(APEpgLoader, self).__init__(settings) # call the parent constructor with the settings object
        
        self.queryUrl = self.URL +  self.EPG_URI
        self.queryUrl = self.queryUrl.replace("{{api_version}}", "1" + "2")
        self.queryUrl = self.queryUrl.replace("{{account_id}}", self.accountId)
        self.queryUrl = self.queryUrl.replace("{{broadcaster_id}}", self.broadcasterId)
        self.queryUrl = self.queryUrl.replace("{{item_id}}", itemId);
        
        self.queryUrl = self.prepareQueryURL(self.queryUrl, None);