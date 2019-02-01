#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:56:44 2019

@author: danw
"""

import textract

class EPDInfo_English:
    EXTRACT_TABLE_KEYS = {"Owner" : "Owner of the Declaration", 
                          "Number": "Declaration number",
                          "Valid" : "Valid to"}
    TAB_OFFSET = 2
    MATCH_STR_FOR_TEXT_BLOCK = "Declared product"
    
    def __init__(self,fname):
        self._textlines = textract.process(fname).splitlines()
        self._textlines = [_.decode("UTF-8") for _ in self._textlines]
        
    def get_table_value(self,tablekey):
        return self._textlines[self._textlines.index(tablekey) + self.TAB_OFFSET]
    
    def extract_table_values(self):
        tabvals = {k : self.get_table_value(v) for k,v in self.EXTRACT_TABLE_KEYS.items()}
        return tabvals 
    
    def get_declared_product(self):
        loc_start = [self.MATCH_STR_FOR_TEXT_BLOCK in _ for _ in self._textlines].index(True) + 1
        loc_end = [len(_) == 0 for _ in self._textlines[loc_start:]].index(True)
        print(loc_start)
        print(loc_end)
        text = " ".join(self._textlines[loc_start:loc_start+loc_end])
        return text
        
        
        
if __name__ == "__main__":
    inf = EPDInfo_English('Besam Automatic Revolving Door RD4.pdf')
    text = inf.get_declared_product()
    print(text)
    
    
    
    