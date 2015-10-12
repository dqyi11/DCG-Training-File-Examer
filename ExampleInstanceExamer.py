'''
Created on Oct 10, 2015

@author: ydq
'''

from ExampleInstance import *
from FeatureSet import *
from ErrorTypes import *

class ExampleInstanceExamer(object):

    def __init__(self):
        self.example_instance = None
        self.feature_set = None
        
    def load(self, example_file, feature_set_file):
        self.example_instance = ExampleInstance()
        self.example_instance.from_xml_file(example_file)
        
        self.feature_set = FeatureSet()
        self.feature_set.from_xml_file(feature_set_file)
        
    def exam(self):
        
        factor_list = self.example_instance.get_factors()
        for factor in factor_list:
            #check words in factor
            if len(factor.words)==0:
                print WarningTypes["NO_WORD"] + "\n    " + str(factor) + "\n"
            for w in factor.words:
                if self.feature_set.has_word_feature(w) == False:
                    return ErrorTypes["NO_WORD_FEATURE"] + "\n    " + str(factor) + "\n    " + str(w) + "\n"
                
            #check groundings in factor
            if len(factor.groundings.groundings)==0:
                print WarningTypes["NO_GROUNDING"] + "\n    " + str(factor) + "\n"
            for g in factor.groundings.groundings:
                if g.grounding_type == "object":
                    if False == self.example_instance.world.has_object(g.type, g.name):
                        return ErrorTypes["NO_OBJECT_IN_WORLD"] + "\n    " + str(factor) + "\n    " + str(g) +"\n"
                    #elif False == self.feature_set.has_object_type_feature(g):
                    #    return ErrorTypes["NO_OBJECT_FEATURE"] + "\n    " + str(factor) + "\n    " + str(g) +"\n"
                elif g.grounding_type == "constraint":
                    if None==g.parent or None==g.child:
                        return ErrorTypes["NO_OBJECT"] + "\n    " + str(factor) + "\n     " + str(g) + "\n"
                    elif False == self.example_instance.world.has_object(g.parent.type, g.parent.name):
                        return ErrorTypes["NO_OBJECT_IN_WORLD"] + "\n    [parent]    " + str(factor) + "\n    " + str(g) +"\n"
                    elif False == self.example_instance.world.has_object(g.child.type, g.child.name):
                        return ErrorTypes["NO_OBJECT_IN_WORLD"] + "\n    [child]    " + str(factor) + "\n    " + str(g) +"\n"
                    elif False == self.example_instance.world.has_object(g.parent.type, g.parent.name):
                        return ErrorTypes["NO_OBJECT_IN_WORLD"] + "\n    [parent]    " + str(factor) + "\n    " + str(g) +"\n"
                    elif False == self.example_instance.world.has_object(g.child.type, g.child.name):
                        return ErrorTypes["NO_OBJECT_IN_WORLD"] + "\n    [child]    " + str(factor) + "\n    " + str(g) +"\n"
                elif g.grounding_type == "func_kernel":
                    if None==g.object:
                        return ErrorTypes["NO_OBJECT"] + "\n    " + str(factor) + "\n     " + str(g) + "\n"
                    elif False == self.example_instance.world.has_object(g.object.type, g.object.name):
                        return ErrorTypes["NO_OBJECT_IN_WORLD"] + "\n    [parent]    " + str(factor) + "\n    " + str(g) +"\n"
                    
        return "Good"
                    
                

        