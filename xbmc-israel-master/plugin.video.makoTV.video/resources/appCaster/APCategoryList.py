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
from APModel import APModel
from APVodItem import APVodItem
from APCategory import APCategory

class APCategoryList(APModel):
    __hasCategories = True
    __hasVodItems = False
    vodItems = []
    children = []
    
    
    def __init__(self, params = {}):
        self.innerDictionary = params
        try:
            items = self.innerDictionary['children']
            for child in items:
                self.children.append(APCategory(child))
        except:
            self.__hasCategories = False
            pass
        try:
            items = self.innerDictionary['vod_items']
            self.__hasVodItems = True
            for vod in items:
                self.vodItems.append(APVodItem(vod))
        except:
            pass
        
    def hasSubCategories(self):
        return self.__hasCategories
    
    def hasVideoitems(self):
        return self.__hasVodItems
    
    # returns the subCategories or an empty list
    def getSubCategories(self):
        return self.children
    
    # returns the vodItems or an empty list
    def getVodItems(self):
        return self.vodItems