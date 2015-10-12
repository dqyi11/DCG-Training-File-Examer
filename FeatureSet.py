'''
Created on Oct 9, 2015

@author: ydq
'''

from xml.dom import minidom

class FeatureSet(object):
    
    def __init__(self):
        self.feature_set = []
        
        
    def from_xml_file(self, filename):
        
        doc = minidom.parse(filename)
        rootnode = doc.getElementsByTagName("root")[0]
        feature_set_node = rootnode.getElementsByTagName("feature_set")[0]
        feature_product_node = feature_set_node.getElementsByTagName("feature_product")[0]
        feature_group_nodes = feature_product_node.getElementsByTagName("feature_group")
        for feature_group in feature_group_nodes:
            feature_group_list = []
            self.feature_set.append(feature_group_list)
            for feature_node in feature_group.childNodes:
                if feature_node.nodeType == feature_node.TEXT_NODE:
                    continue
                if feature_node.nodeName == "feature_cv":
                    feature = {}
                    feature["name"] = feature_node.nodeName
                    feature["invert"] = int(feature_node.getAttribute("invert"))
                    feature["cv"] = int(feature_node.getAttribute("cv"))
                    feature_group_list.append(feature)
                elif feature_node.nodeName == "feature_word":
                    feature = {}
                    feature["name"] = feature_node.nodeName
                    feature["invert"] = int(feature_node.getAttribute("invert"))
                    feature["pos"] = feature_node.getAttribute("pos")
                    feature["text"] = feature_node.getAttribute("text")
                    feature_group_list.append(feature)
                elif feature_node.nodeName == "feature_num_words":
                    feature = {}
                    feature["name"] = feature_node.nodeName
                    feature["invert"] = int(feature_node.getAttribute("invert"))
                    feature["num_words"] = int(feature_node.getAttribute("num_words"))
                    feature_group_list.append(feature)
                elif feature_node.nodeName == "feature_object":
                    feature = {}
                    feature["name"] = feature_node.nodeName
                    feature["invert"] = int(feature_node.getAttribute("invert"))
                    feature["object_type"] = int(feature_node.getAttribute("object_type"))
                    feature_group_list.append(feature)
                elif feature_node.nodeName == "feature_object_matches_child":
                    feature = {}
                    feature["name"] = feature_node.nodeName
                    feature["invert"] = int(feature_node.getAttribute("invert"))
                    feature_group_list.append(feature)
                elif feature_node.nodeName == "feature_func_kernel":
                    feature = {}
                    feature["name"] = feature_node.nodeName
                    feature["invert"] = int(feature_node.getAttribute("invert"))
                    feature["kernel_type"] = int(feature_node.getAttribute("kernel_type"))
                    feature_group_list.append(feature)
                elif feature_node.nodeName == "feature_func_kernel_object":
                    feature = {}
                    feature["name"] = feature_node.nodeName
                    feature["invert"] = int(feature_node.getAttribute("invert"))
                    feature["object_type"] = int(feature_node.getAttribute("object_type"))
                    feature_group_list.append(feature)
                elif feature_node.nodeName == "feature_func_kernel_matches_child":
                    feature = {}
                    feature["name"] = feature_node.nodeName
                    feature["invert"] = int(feature_node.getAttribute("invert"))
                    feature_group_list.append(feature)
                elif feature_node.nodeName == "feature_func_kernel_object_matches_child":
                    feature = {}
                    feature["name"] = feature_node.nodeName
                    feature["invert"] = int(feature_node.getAttribute("invert"))
                    feature_group_list.append(feature)
                elif feature_node.nodeName == "feature_constraint":
                    feature = {}
                    feature["name"] = feature_node.nodeName
                    feature["invert"] = int(feature_node.getAttribute("invert"))
                    feature["constraint_type"] = int(feature_node.getAttribute("constraint_type"))
                    feature_group_list.append(feature)
                elif feature_node.nodeName == "feature_constraint_parent_matches_child_object":
                    feature = {}
                    feature["name"] = feature_node.nodeName
                    feature["invert"] = int(feature_node.getAttribute("invert"))
                    feature_group_list.append(feature)
                elif feature_node.nodeName == "feature_constraint_child_matches_child_object":
                    feature = {}
                    feature["name"] = feature_node.nodeName
                    feature["invert"] = int(feature_node.getAttribute("invert"))
                    feature_group_list.append(feature)
                elif feature_node.nodeName == "feature_constraint_parent_is_robot_object":
                    feature = {}
                    feature["name"] = feature_node.nodeName
                    feature["invert"] = int(feature_node.getAttribute("invert"))
                    feature_group_list.append(feature)
                elif feature_node.nodeName == "feature_constraint_child_is_robot_object":
                    feature = {}
                    feature["name"] = feature_node.nodeName
                    feature["invert"] = int(feature_node.getAttribute("invert"))
                    feature_group_list.append(feature)
                    
    def get_str(self):
        out_str = ""
        for feature_group_list in self.feature_set:
            for feature in feature_group_list:
                out_str += str(feature) + "\n"
            out_str += "\n"
        return out_str
        
    def __str__(self):
        return self.get_str()
    
    def has_word_feature(self, w):
        for feature_group in self.feature_set:
            for feature in feature_group:
                if feature["name"] == "feature_word":
                    #print w 
                    #print feature
                    if feature["pos"] == w["type"] and feature["text"] == w["text"]:
                        return True
        return False
    
    def has_object_type_feature(self, o):
        for feature_group in self.feature_set:
            for feature in feature_group:
                if feature["name"] == "feature_object":
                    if feature["object_type"] == o.type:
                        return True
        return False
            
            