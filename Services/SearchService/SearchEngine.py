from Services.FilesManagmentService.FilesServices import * 
from Services.TextProcessingService.TextProcessingServices import queryCleanTextAlgorithm
from sklearn.metrics.pairwise import cosine_similarity
from Services.DataRepresentationService.VectorSpaceModel import VectorSpaceModel
from Services.EvaluationService.EvaluationServices import fullEvaluation
import pandas as pd

from Services.WordEmbeddingServices.WordEmbeddingModel import WordEmbeddingModel


class SearchEngine:
    
    def __init__( self , dataset_name ):
        self.results = []
        self.dataset_name = dataset_name
        self.corrected_query = None
        

    def search( self , query ):
        
        # setup vector space model
        vsm = VectorSpaceModel(self.dataset_name)
        
        # build VSM
       # vsm.buildeStorgeVSM()
    
        # apply text processing on query
        preprocessed_query = queryCleanTextAlgorithm( query )
        self.corrected_query = preprocessed_query[0]
        clean_query = preprocessed_query[1]
        
        model = WordEmbeddingModel(datasetName) 
        expanded_Query = model.search_similar_words(clean_query ,4)
        
        # build vector of query using vsm object  
        query_vector  = vsm.convertQueryToVector(expanded_Query)
        # get top document in result 
        top_documents = vsm.getSimilarityDocuments(queryVector = query_vector, top_k = 10)
        
        #vsm.printVectorSpaceModel()
        #print()
        #no_result = True
        
        # ranck
        for index in top_documents: 
            # get document name
            doc_name = vsm.get_document_name(index)
            doc = get_document_PKL_File(  self.dataset_name , doc_name )
            self.results.append(index)
            
        return self.results
    
    

    def get_results(self):
        return self.results
    
    def get_corrected_query(self):
        return self.corrected_query
    
    
    def evaluationSearchEngine(self , queries_count):
        
        i = 0
        all_relevant_docs  = []
        all_retrieved_docs = []
        
            # get qrels from dataset's path
            # for every qrels file...
        for filename in os.listdir( getprojectPath() +"Services/FilesManagmentService/storge/Datasets/"+ self.dataset_name +"/qrels" ):
            i = i+1
            print('\n -Try search for Query : ' + str(i))
            qrel = get_qrel_PKL_File( self.dataset_name ,filename ) 
           # get query from dataset's path
            query = get_query_PKL_File( self.dataset_name ,"Query_"+ str( qrel.query_id ) +".csv" ) 
            print("  ----evaluate the result\n")
           
            engine = SearchEngine(self.dataset_name)
            engine.search(query.text)
            
            relevant_docs  = []
            retrieved_docs = []
            
            for doc in engine.get_results():
                retrieved_docs.append(doc.doc_id)
                print( str(doc.doc_id) +" -- "+ str(qrel.doc_id))
                if doc.doc_id == qrel.doc_id:
                    relevant_docs.append(doc.doc_id)
                break
                    
            # add to all_relevant_docs array
            all_relevant_docs.append(relevant_docs)
            
            # add to all_relevant_docs array
            all_retrieved_docs.append(retrieved_docs)
            if i == queries_count : break
        
        # evaluation..
        print('\n evaluate of final results.. ')
        fullEvaluation(all_relevant_docs , all_retrieved_docs )
    
    
    
    


engine = SearchEngine("antique-train")
#engine.evaluationSearchEngine(20)



result = engine.search("The building standing in for the courthouse is the Pasadena City Hall in Pasadena, California. The title sequence would then end with him entering his chambers, sitting down, and signing some documentsThe nationally syndicated version was originally taped in Los Angeles for its first four runs of 10 episodes each (1986â€“89), and later moved to Toronto, Ontario, Canada for its")

for doc in result:
       print("\n----------")
       print(doc)
     #  print(doc.text)
       
       #print("\n\n----------")

  







    
