'''
Created on Oct 9, 2015

@author: ydq
'''

from xml.dom import minidom

class WorldObject(object):
    
    def __init__(self):
        self.name = ""
        self.type = ""
        
    def __str__(self):
        return "Object (name)" + self.name + " (type)" + self.type + "\n"

class World(object):

    def __init__(self):
        self.objects = []
        
    def from_xml(self, xml_str):
        doc = minidom.parseString(xml_str)
        
        worldnode = doc.getElementsByTagName("world")[0]
        for object_node in worldnode.childNodes:
            if object_node.nodeName == "object":
                obj = WorldObject()
                obj.name = object_node.getAttribute("name")
                obj.type = object_node.getAttribute("type")
                self.objects.append(obj)
                
    def __str__(self):
        out_str = "World\n"
        for obj in self.objects:
            out_str += "    " + obj.__str__()
        return out_str
    
                