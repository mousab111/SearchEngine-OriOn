# -*- coding: utf-8 -*-
from Services.FilesManagmentService.FilesServices import * 
from Services.DataRepresentationService.VectorSpaceModel import VectorSpaceModel 



projectPath = getprojectPath()

datasetName = "antique-train"

vsm = VectorSpaceModel(datasetName , True)
vsm.buildDocumentsMap()

#fileClear(  datasetName , 'suggestions.txt')
#vsm.buildeVectorSpaceModel(keys , values )

#saveObjectTo_PKL_File( vsm.getDocumentVectors(), "trec-tot-2023-train", "doc_vectors.pkl")
#saveObjectTo_PKL_File( vsm.get_vectorizer(), "trec-tot-2023-train", "Model.pkl")
#saveObjectTo_PKL_File( vsm.getDocumentMap(), "trec-tot-2023-train", "docs_map.pkl")

"""
for word in vsm.getWords():
    writeContentToFile( 'words.txt' , "\n"+word ) 
"""

print("\n\n----- Objects Created Successfully -----")
print("-- Done --")

#print(top_documents)
#print(vsm.getDocumentId(top_documents[0]))

