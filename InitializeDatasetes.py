# -*- coding: utf-8 -*-
from Services.FilesManagmentService.FilesServices import *
import ir_datasets
import pandas as pd
import os
from Services.TextProcessingService.TextProcessingServices import cleanTextAlgorithm , queryCleanTextAlgorithm
from nltk.tokenize import word_tokenize



dataset = ir_datasets.load('trec-tot/2023/train')

dataset_name = "test"


class InitializeDatasetes:
    
    def __init__( self , loadDataaset , dataset_folder ):
        self.dataset = ir_datasets.load(loadDataaset)
        self.dataset_name = dataset_folder
        
      
    def loadDocuments(self ):
        i=0
        for  doc in self.dataset.docs_iter(): 
            i = i+1
            print(i)
            doc.doc_id
            save_document_To_PKL_File(doc , dataset_name , str (doc.doc_id) +".pkl" )
        print("--- Done ---")
        
        
        
    def loadQueries(self ):
        i=1
        for  Query in self.dataset.queries_iter():
            save_query_To_PKL_File( Query , dataset_name, "Query_" + Query.query_id +".pkl")
            i=i+1
            print(i)
        print("--- Done ---")


    def loadQrels(self ):
        for qrel in self.dataset.qrels_iter():
            i=0
            save_qrel_To_PKL_File(qrel, dataset_name, "qrel_" + qrel.query_id +".pkl")
            i=i+1
            print(i)
        print("--- Done ---")
            
    def createDocumentsMap(self):
        i = 0
        docs_path = getprojectPath() + "Services/FilesManagmentService/storge/Datasets/" + self.dataset_name + "/docs"
        documents_map = []
        for filename in os.listdir(docs_path): 
            i = i+1
            print (i)
            doc_id = get_document_Id_PKL_File(self.dataset_name, filename)
            documents_map.append(doc_id)
        saveObjectTo_PKL_File(documents_map, self.dataset_name, 'docs_map.pkl')
        print("--- Done ---")
        
        
        
        
        
#------------------------------------ CODE --------------------------------  

dataset = InitializeDatasetes('trec-tot/2023/train' ,"trec-tot-2023-train" ) 
dataset.createDocumentsMap()


"""
dataset = InitializeDatasetes('antique/train' ,"antique-train" ) 
dataset.createDocumentsMap()

"""
    
    
