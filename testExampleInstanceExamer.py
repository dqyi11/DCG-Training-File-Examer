'''
Created on Oct 10, 2015

@author: ydq
'''

from ExampleInstanceExamer import *

if __name__ == '__main__':
    EXAMPLE_FILE = "example_0001.xml"
    FEATURE_SET_FILE = "feature_set.xml"
    
    examer = ExampleInstanceExamer()
    examer.load(EXAMPLE_FILE, FEATURE_SET_FILE)
    examer.exam()