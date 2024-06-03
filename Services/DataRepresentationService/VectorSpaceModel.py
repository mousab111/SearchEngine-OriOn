# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from Services.FilesManagmentService.FilesServices import *
from Services.TextProcessingService.TextProcessingServices import * 
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
import numpy as np
        


class VectorSpaceModel:
    
    def __init__(self , datasetName , firstTime = False ):
        #--- 
        self.dataset_name = datasetName
        if firstTime != True :
        # get documents vectors from file..
            self.vector_space_model = getObjectFrom_PKL_File ( datasetName , 'doc_vectors.pkl' )
        # get documents map (index) from file..
            self.document_map = getObjectFrom_PKL_File ( datasetName , 'docs_map.pkl' )
        # get model (vectorizer ) from file..
            self.vectorizer = getObjectFrom_PKL_File ( datasetName , 'Model.pkl' )


    def buildeVectorSpaceModel(self):
        
        document_map =[]
        datasetName = build_key_value_transformer(keys, values)
        
        dataset = ir_datasets.load(datasetName[self.dataset_name])

        
        vectorizer =  TfidfVectorizer(
             tokenizer  = word_tokenize ,
             max_df     = 0.75,
             preprocessor = cleanTextAlgorithm
              )
        
        
        docs_path = getprojectPath() + "Services/FilesManagmentService/storge/Datasets/" + self.dataset_name + "/docs"
        
        print("\n processing , please waite..")
        # Build the vector space model
        vectorizer.fit([ get_document_content_PKL_File(self.dataset_name, filename) for filename in os.listdir(docs_path) ])
        vector_space_model = vectorizer.transform([ get_document_content_PKL_File(self.dataset_name, filename) for filename in os.listdir(docs_path) ]) 
        saveObjectTo_PKL_File( vector_space_model , self.dataset_name , "doc_vectors.pkl")
        saveObjectTo_PKL_File( vectorizer , self.dataset_name, "Model.pkl")
        document_map = [ get_document_Id_PKL_File(self.dataset_name, filename) for filename in os.listdir(docs_path) ]
        saveObjectTo_PKL_File( document_map , self.dataset_name, "docs_map.pkl")
       
       
 
    def buildDocumentsMap(self):
       print("please waite..")
       docs_path = getprojectPath() + "Services/FilesManagmentService/storge/Datasets/" + self.dataset_name + "/docs"
       document_map = [ get_document_Id_PKL_File(self.dataset_name, filename) for filename in os.listdir(docs_path) ]
       saveObjectTo_PKL_File( document_map , self.dataset_name, "docs_map.pkl")

        
        
    def printVectorSpaceModel(self):
        df = pd.DataFrame( self.vector_space_model.toarray() , columns = self.vectorizer.get_feature_names_out())
        print(df)
    
    def getWords(self):
        return self.vectorizer.get_feature_names_out()
        
        
    def convertQueryToVector(self , query):
       return self.vectorizer.transform([query])
   
   
    def getSimilarityDocuments( self , queryVector , top_k ):
        similarity = cosine_similarity( queryVector , self.vector_space_model)
        # Convert to a one dimensional matrix
        similarity = similarity.flatten()
        # sort documents
        sorted_indices = similarity.argsort()[::-1]
        # get top k
        top_documents = sorted_indices[:top_k]
        
       # for index in top_documents:
         #   if  similarity[index] > 0.00009 : print(similarity[index])
            
        # return more similarity documents
        return [index for index in top_documents if similarity[index] > 0.00009 ]


    def getDocumentVectors(self, doc_id):
        if doc_id in self.vector_space_model:
            return self.vector_space_model[doc_id]
        else:
            return None
        
    
    def get_document_name( self, index ):
        return self.document_map[index]
    
    def setVectorizer( self , vectorizer):
        self.vectorizer = vectorizer

    def setDocumentMap( self , document_map):
        self.document_map = document_map  
        
    def setDocumentVectors(self , doc_vectors ):
        self.vector_space_model = doc_vectors
 
    def getDocumentVectors( self):
        return self.vector_space_model

    def getDocumentMap(self):
        return self.document_map 
    
    def get_vectorizer(self):
        return self.vectorizer
    
    

        
        




