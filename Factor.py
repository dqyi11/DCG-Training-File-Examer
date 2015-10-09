'''
Created on Oct 9, 2015

@author: ydq
'''
from __builtin__ import True

PHRASE_TYPE = {"VP", "NP", "PP"}
WORD_TYPE = {"VB", "JJ", "DT", "NN", "TO"}

from xml.dom import minidom
from Groundings import *

def is_phrase_type(type_name):
    for ph_type in PHRASE_TYPE:
        if type_name == ph_type:
            return True
    return False

def is_word_type(type_name):
    for word_type in WORD_TYPE:
        if word_type == type_name:
            return True
    return False

class Factor(object):
    
    def __init__(self):
        self.groundings = None
        self.words = []
        self.pos = ""
        self.children = []
    
    def from_xml(self, xml_str):        
        doc = minidom.parseString(xml_str)
        self.pos = doc.firstChild.nodeName
        for child_node in doc.firstChild.childNodes:
            if child_node.nodeType == child_node.TEXT_NODE:
                continue
            if child_node.nodeName == "grounding":
                self.groundings = Groundings()
                self.groundings.from_xml(child_node.toxml())
            else:
                if is_word_type(child_node.nodeName):
                    w = {}
                    w["type"] = child_node.nodeName
                    w["text"] = child_node.getAttribute("text")
                    self.words.append(w)
                elif is_phrase_type(child_node.nodeName):
                    factor = Factor()
                    factor.from_xml(child_node.toxml())
                    self.children.append(factor)     
    
    def __str__(self):
        return self.get_str()
        
    def get_str(self, indent=""):
        out_str = indent + "Factor ";
        out_str += self.pos + "\n"
        out_str += indent + "    " + "(Word) "
        for w in self.words:
            out_str += "[" + w["type"] + ":" + w["text"] + "]"
        out_str += "\n"
        out_str += self.groundings.get_str(indent + "    ") + "\n"
        for f in self.children:
            out_str += f.get_str(indent + "    ") + "\n"
        return out_str
        