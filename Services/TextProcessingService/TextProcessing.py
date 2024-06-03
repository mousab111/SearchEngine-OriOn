# -*- coding: utf-8 -*-
from nltk.tokenize import word_tokenize
import string
from spellchecker import SpellChecker
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet
import os
import re
from Services.FilesManagmentService.FilesServices import *


class TextProcessing:

    
    def __init__(self, text):
        self.text = text
        self.stopwords = getFileContentAsArray("Services/TextProcessingService/StopWords.txt")


       #--------  Converts the input text to lowercase -------
       
    def convert_to_lowercase(self):
         self.text = self.text.lower()
    
    
        #--------  Removes all punctuation from the input text -------
        
    def remove_punctuation(self):
        self.text = ''.join(char for char in self.text if char not in string.punctuation)



        #-------  Tokenizes the text -----------
        
    def tokenize(self):
        self.text = word_tokenize(self.text)
        

        #------- Counts the number of words in the text   ----------
    
    def count_words(self):
        return len(self.text)


        #------ Removes all stopwords from the text --------
        
    def remove_stopwords(self  ):
        filtered_text = []
        for word in self.text:
            if word not in self.stopwords:
                filtered_text.append(word)
        self.text = filtered_text
        
        
       # Applies stemming to the input text using the specified stemmer

    def stem_text(self, stemmer):
        self.text = [stemmer.stem(word) for word in self.text]
    
    def convertToNaturalText(self):
        self.text = ' '.join(self.text)
        

    def correct_spelling(self):
        spell = SpellChecker()
        misspelled = spell.unknown(self.text)
        for i, token in enumerate(self.text):
            if token in misspelled:
                corrected = spell.correction(token)
                if corrected is not None:
                    self.text[i] = corrected
        return 
    
    
    def get_wordnet_pos(self,tag_parameter):
        tag = tag_parameter[0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}
        return tag_dict.get(tag, wordnet.NOUN)


    def lemmatize_text(self):
        pos_tags = pos_tag(self.text)
        lemmatizer = WordNetLemmatizer()
        self.text = [lemmatizer.lemmatize(word, pos = self.get_wordnet_pos(tag)) for word, tag in pos_tags]
         
            
    
    def getText(self):
        return self.text
    





