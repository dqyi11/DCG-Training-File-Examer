'''
Created on Oct 9, 2015

@author: ydq
'''

from ExampleInstance import *

if __name__ == '__main__':
    
    FILE = "example_0001.xml"
    example = ExampleInstance()
    example.from_xml_file(FILE)
    print example
