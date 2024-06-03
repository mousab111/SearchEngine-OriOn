# -*- coding: utf-8 -*-
from Services.TextProcessingService.TextProcessing import TextProcessing
from nltk.stem import PorterStemmer
from Services.FilesManagmentService.FilesServices import *



def cleanTextAlgorithm( text):
    text_processor = TextProcessing(text)
    text_processor.remove_punctuation()
    text_processor.convert_to_lowercase()
    text_processor.tokenize()
    text_processor.remove_stopwords()
    stemmer = PorterStemmer()
    text_processor.stem_text(stemmer)
    #text_processor.lemmatize_text()
    # correct the text
    text_processor.convertToNaturalText()
    return text_processor.getText()
    



def queryCleanTextAlgorithm(text):
    text_processor = TextProcessing(text)
    text_processor.remove_punctuation()
    text_processor.convert_to_lowercase()
    text_processor.tokenize()
    
    # correct the text
    text_processor.correct_spelling()
    
    # get corrected text as tokins
    corrected = TextProcessing( text_processor.getText())
    
    #convert to natural text
    corrected.convertToNaturalText()
    
    #remove stopWords

    text_processor.remove_stopwords()
    stemmer = PorterStemmer()
    text_processor.stem_text(stemmer)
    #text_processor.lemmatize_text()
    text_processor.convertToNaturalText()
    return  [ corrected.getText() , text_processor.getText() ]


def cleanTokenizeText(text ):
    text_processor = TextProcessing(text  )
    text_processor.remove_punctuation()
    text_processor.convert_to_lowercase()
    text_processor.tokenize()
    text_processor.remove_stopwords()
    return text_processor.getText()
    