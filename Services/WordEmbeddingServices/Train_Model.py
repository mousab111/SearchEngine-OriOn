# -*- coding: utf-8 -*-

from Services.FilesManagmentService.FilesServices import *
from Services.WordEmbeddingServices.WordEmbeddingModel import WordEmbeddingModel








#-----------------------------------------------

#  antique-train

datasetName = "trec-tot-2023-train"


projectPath = getprojectPath()


model = WordEmbeddingModel(datasetName , True)

model.train_model()


print("\n\n---- Model created Successfully !") 



