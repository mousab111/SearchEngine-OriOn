from gensim.models import Word2Vec
from Services.TextProcessingService.TextProcessingServices import *
from Services.FilesManagmentService.FilesServices import *


class WordEmbeddingModel:
    
    def __init__( self, dataset_name , firstTime = False ):
        self.dataset_name = dataset_name
        if firstTime :
                self.model = None   
        else :
                self.model =  getObjectFrom_PKL_File( dataset_name , "EmbeddingModel.pkl" )



    def train_model(self):
        
        docs_path = getprojectPath() + "Services/FilesManagmentService/storge/Datasets/" + self.dataset_name + "/docs"
        
        print('Hello Musab , processing is currently underway, please wait..')
        self.model = Word2Vec(
            [ cleanTokenizeText(get_document_content_PKL_File( self.dataset_name, filename) )  for filename in os.listdir(docs_path) ], 
                              vector_size=100, 
                              window = 5,
                              min_count = 3,
                              workers = 4
                              )  
        
    # save model to the file..
        saveObjectTo_PKL_File( self.model , self.dataset_name, 'EmbeddingModel.pkl')




    def get_word_embedding(self, word):

        if self.model:
            return self.model[word]
        else:
            raise ValueError("Please train the model first")
            
            
            
            

    def search_similar_words(self, word, topn=5):
        if self.model:
            similar_words = self.model.wv.most_similar(word, topn=topn)
            return similar_words
        else:
            raise ValueError("Please train the model first")



