'''
Created on Oct 12, 2015

@author: ydq
'''

import sys
from ExampleInstanceExamer import *

if __name__ == '__main__':
    
    EXAMPLE_FILE = sys.argv[1]
    FEATURE_SET_FILE = sys.argv[2]
    
    examer = ExampleInstanceExamer()
    examer.load(EXAMPLE_FILE, FEATURE_SET_FILE)
    print examer.exam()