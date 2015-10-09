'''
Created on Oct 9, 2015

@author: ydq
'''

from xml.dom import minidom

class Grounding(object):
    
    def __init__(self):
        self.grounding_type = ""

class GroundingObject(Grounding):
    
    def __init__(self):
        self.grounding_type = "object"
        self.type = ""
        self.name = ""
        
    def __str__(self):
        return self.get_str()
    
    def get_str(self, indent=""):
        out_str = indent + "[Object]"
        out_str += "(type)" + self.type
        out_str += "(name)" + self.name       
        return out_str
    
    def from_xml(self, xml_str):
        doc = minidom.parseString(xml_str)
        obj_node = doc.getElementsByTagName("object")[0]
        self.type = obj_node.getAttribute("type")
        self.name = obj_node.getAttribute("name")  
        
class GroundingConstraint(Grounding):    
    
    def __init__(self):
        self.grounding_type = "constraint"
        self.type = "" 
        self.child = None
        self.parent = None
        
    def __str__(self):
        return self.get_str()
        
    def get_str(self, indent=""):
        out_str = indent + "[Constraint]"
        out_str += "(type)" + self.type + "\n"
        out_str += indent + "    (parent){    "
        if self.parent != None:
            out_str += self.parent.get_str() 
        out_str += "    }\n"
        out_str += indent + "    (child){    "
        if self.child != None:
            out_str += self.child.get_str()
        out_str += "    }\n"
        return out_str

    def from_xml(self, xml_str):
        doc = minidom.parseString(xml_str)
        constraint_node = doc.getElementsByTagName("constraint")[0]
        self.type = constraint_node.getAttribute("type")
        for c_node in constraint_node.childNodes:
            if c_node.nodeType == c_node.TEXT_NODE:
                continue
            if c_node.nodeName == "parent":
                for cc_node in c_node.childNodes:
                    if cc_node.nodeName == "object" and self.parent == None:
                        self.parent = GroundingObject()
                        self.parent.from_xml(cc_node.toxml())
            elif c_node.nodeName == "child":
                for cc_node in c_node.childNodes:
                    if cc_node.nodeName == "object" and self.child == None:
                        self.child = GroundingObject()
                        self.child.from_xml(cc_node.toxml())
        
class GroundingFuncKernel(Grounding):
    
    def __init__(self):
        self.grounding_type = "func_kernel"
        self.type = ""
        self.weight = 0.0
        self.object = None
        
    def __str__(self):
        return self.get_str()
        
    def get_str(self, indent=""):
        out_str = indent + "[FuncKernel]"
        out_str += "(type)" + self.type
        out_str += "(weight)" + str(self.weight) + "\n"
        out_str += indent + "    (object){    "
        if self.object != None:
            out_str += self.object.get_str()
        out_str += "    }"
        return out_str

    def from_xml(self, xml_str):
        doc = minidom.parseString(xml_str)
        func_kernel_node = doc.getElementsByTagName("func_kernel")[0]
        self.weight = float(func_kernel_node.getAttribute("weight"))
        self.type = func_kernel_node.getAttribute("type")
        for c_node in func_kernel_node.childNodes:
            if c_node.nodeType == c_node.TEXT_NODE:
                continue
            if c_node.nodeName == "object" and self.object == None:
                self.object = GroundingObject()
                self.object.from_xml(c_node.toxml())

class Groundings(object):
    
    def __init__(self):
        self.groundings = []
        
    def from_xml(self, xml_str):
        doc = minidom.parseString(xml_str)
        grounding_node = doc.getElementsByTagName("grounding")[0]
        grounding_set_node = grounding_node.getElementsByTagName("grounding_set")[0]
        for g_node in grounding_set_node.childNodes:
            if g_node.nodeType == g_node.TEXT_NODE:
                continue
            if g_node.nodeName == "object":
                g = GroundingObject()
                g.from_xml(g_node.toxml())
                self.groundings.append(g)
            elif g_node.nodeName == "constraint":
                g = GroundingConstraint()
                g.from_xml(g_node.toxml())
                self.groundings.append(g)
            elif g_node.nodeName == "func_kernel":
                g = GroundingFuncKernel()
                g.from_xml(g_node.toxml())
                self.groundings.append(g)
                
    def __str__(self):
        return self.get_str()
        
    def get_str(self, indent=""):
        out_str = ""
        for grounding in self.groundings:
           out_str += grounding.get_str(indent) + "\n"                
        return out_str
        