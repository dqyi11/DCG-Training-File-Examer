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
            #check words in phrase
            if len(factor.words)==0:
                print WarningTypes["NO_WORD"] + "\n    " + str(factor) + "\n"
            for w in factor.words:
                if self.feature_set.has_word_feature(w) == False:
                    return ErrorTypes["NO_WORD_FEATURE"] + "\n    " + str(factor) + "\n    " + str(w) + "\n"

        