'''
Created on Oct 9, 2015

@author: ydq
'''

from FeatureSet import *

if __name__ == '__main__':
    
    FILE = "feature_set.xml"
    feature_set = FeatureSet()
    feature_set.from_xml_file(FILE)
    
    print feature_set