import re
import pandas as pd
import pickle
import csv
from pathlib import Path
import os



#---- Files Services -----------

def getprojectPath():
    return "C:/Users/bassam/Search_Engine/"



def getFileContent( path ):
    file = open ( path , "r" )
    fileData = file.read()
    file.close()
    return fileData

def fileClear(datasetName,fileName):
    try:
        with open(getprojectPath() +"Services/FilesManagmentService/storge/Datasets/"+ datasetName +"/"+fileName , "w+", encoding="utf-8") as file:
            file.write("")
    except Exception as e:
        print("error:", str(e))
    
def writeContentToFile( datasetName , fileName, content):
    try:
        with open(getprojectPath() +"Services/FilesManagmentService/storge/Datasets/"+ datasetName +"/"+fileName, "w+", encoding="utf-8") as file:
            file.write(content)
    except Exception as e:
        print("error:", str(e))

 
def AddContentToFile(datasetName ,fileName, content):
    try:
        with open(getprojectPath() +"Services/FilesManagmentService/storge/Datasets/"+ datasetName +"/"+fileName, "a+", encoding="utf-8") as file:
            file.write(content)
    except Exception as e:
        print("error:", str(e))

def getFileContentAsArray( filename):
    with open(getprojectPath() + filename , "r") as file:
        text = file.read()
    return re.findall(r"\S+", text)


def getDatasetFileContentAsArray(  datasetName,filename):
    with open(getprojectPath() +"Services/FilesManagmentService/storge/Datasets/"+ datasetName +"/"+filename , "r") as file:
        text = file.read()
    return re.findall(r"\S+", text)


def read_file(directory, filename):
    with open(os.path.join(directory, filename), "r") as file:
        text = file.read()
    return text


def saveObjectTo_CSV_File(myObject , dataset_name , object_name):
    df = pd.DataFrame(myObject.toarray())
    df.to_csv(  getprojectPath()+"Services/FilesManagmentService/storge/Datasets/"+dataset_name+"/objects/"+object_name+".csv" , index=False)


def getObjectFrom_CSV_File( dataset_name , object_name):
    df = pd.read_csv( getprojectPath()+"Services/FilesManagmentService/storge/Datasets/"+dataset_name+"/objects/"+object_name+".csv" )
    return df.values

def saveObjectTo_PKL_File (myObject , dataset_name , object_name):
    directory = getprojectPath()+"Services/FilesManagmentService/storge/Datasets/"+dataset_name+"/objects"
    Path(directory).mkdir(parents=True, exist_ok=True)
    file_path = f"{directory}/{object_name}"
    with open(file_path, 'wb') as file:
        pickle.dump(myObject, file)
            
        

def getObjectFrom_PKL_File ( dataset_name , object_name ):
    with open(  getprojectPath()+"Services/FilesManagmentService/storge/Datasets/" + dataset_name + "/objects/" + object_name , 'rb') as file:
        return pickle.load(file)


def save_To_Dataset(myObject , path):
    df = pd.DataFrame(myObject.toarray())
    df.to_csv( path , index=False)
    
    
def get_document_content(datasetName , docNumber):
    path = getprojectPath() +"Services/FilesManagmentService/storge/Datasets/"+ datasetName +"/docs/document_"+ str(docNumber) +".csv"
    df = pd.read_csv( path )
    rr = df.values
    ff = pd.DataFrame(rr.toarray())
    return ff


def get_document_id(datasetName , docNumber):
    with open(getprojectPath() +"Services/FilesManagmentService/storge/Datasets/"+ datasetName +"/docs/document_" + str(docNumber) +".csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row['doc_id'] for row in reader]

def get_document(datasetName , docNumber):
    with open(getprojectPath() +"Services/FilesManagmentService/storge/Datasets/"+ datasetName +"/docs/document_" + str(docNumber) +".csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]
    
    
def get_document_PKL_File ( dataset_name , object_name ):
    with open(  getprojectPath()+"Services/FilesManagmentService/storge/Datasets/" + dataset_name + "/docs/" + object_name , 'rb') as file:
        return pickle.load(file)

#vms = getObjectFrom_PKL_File( "trec-tot-2023-train" , 'VectorSpaceModel')

def save_document_To_PKL_File (myObject , dataset_name , object_name):
    directory = getprojectPath()+"Services/FilesManagmentService/storge/Datasets/"+dataset_name+"/docs"
    Path(directory).mkdir(parents=True, exist_ok=True)
    file_path = f"{directory}/{object_name}"
    with open(file_path, 'wb') as file:
        pickle.dump(myObject, file)


def get_qrel_PKL_File ( dataset_name , object_name ):
    with open(  getprojectPath()+"Services/FilesManagmentService/storge/Datasets/" + dataset_name + "/qrels/" + object_name , 'rb') as file:
        return pickle.load(file)

#vms = getObjectFrom_PKL_File( "trec-tot-2023-train" , 'VectorSpaceModel')

def save_qrel_To_PKL_File (myObject , dataset_name , object_name):
    directory = getprojectPath()+"Services/FilesManagmentService/storge/Datasets/"+dataset_name+"/qrels"
    Path(directory).mkdir(parents=True, exist_ok=True)
    file_path = f"{directory}/{object_name}"
    with open(file_path, 'wb') as file:
        pickle.dump(myObject, file)


def get_query_PKL_File ( dataset_name , object_name ):
    with open(  getprojectPath()+"Services/FilesManagmentService/storge/Datasets/" + dataset_name + "/queries/" + object_name , 'rb') as file:
        return pickle.load(file)

#vms = getObjectFrom_PKL_File( "trec-tot-2023-train" , 'VectorSpaceModel')

def save_query_To_PKL_File (myObject , dataset_name , object_name):
    directory = getprojectPath()+"Services/FilesManagmentService/storge/Datasets/"+dataset_name+"/queries"
    Path(directory).mkdir(parents=True, exist_ok=True)
    file_path = f"{directory}/{object_name}"
    with open(file_path, 'wb') as file:
        pickle.dump(myObject, file)


def get_document_content_PKL_File( dataset_name , object_name ):
    doc = get_document_PKL_File(dataset_name, object_name)
    print(doc.doc_id)
    return doc.text

def get_document_Id_PKL_File( dataset_name , object_name ):
    doc = get_document_PKL_File(dataset_name, object_name)
    return doc.doc_id



def build_key_value_transformer(keys, values):
    transformer = dict(zip(keys, values))
    return transformer


