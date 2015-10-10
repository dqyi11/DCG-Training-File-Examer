'''
Created on Oct 9, 2015

@author: ydq
'''

from xml.dom import minidom
from World import *
from Factor import *

class ExampleInstance(object):

    def __init__(self):
        self.instruction = ""
        self.world = None
        self.root = None
        
        
    def from_xml_file(self, filename):
        doc = minidom.parse(filename)
        rootnode = doc.getElementsByTagName("root")[0]
        for node in rootnode.childNodes:
            if node.nodeType == node.TEXT_NODE:
                continue
            if node.nodeName == "instruction":
                self.instruction = node.getAttribute("text")
            elif node.nodeName == "world":
                self.world = World()
                self.world.from_xml(node.toxml())
            else:
                self.root = Factor()
                self.root.from_xml(node.toxml())
                
    def __str__(self):
        out_str = "[instruction]" + self.instruction + "\n"
        out_str += self.world.__str__()
        out_str += self.root.__str__()
        return out_str
    
    def get_factors(self):
        factor_list = []
        self.scan_factor(self.root, factor_list)
        return factor_list
    
    def scan_factor(self, factor, factor_list): 
        factor_list.append(factor)        
        for child_factor in factor.children:
            self.scan_factor(child_factor, factor_list)
                
            
            
            
        
        