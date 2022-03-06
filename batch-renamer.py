import os

search = "document"
replace = "file"
type_filter = ".py"

#get all the files from the current directory
directory_content = os.listdir('.')
docs = [ doc for doc in directory_content if os.path.isfile(doc)]
renamed = 0

print(docs)
print(directory_content)

#show the total number of files in current diretory
print(f"{len(docs)} of {len(directory_content)} elements are files")

for doc in docs:

    doc_name,filetype = os.path.splitext(doc)
    
    if filetype == type_filter:

        if search in doc_name:

            new_name = doc_name.replace(search,replace) + filetype
            #os function to rename the file
            os.rename(doc,new_name)
            renamed += 1
            
            print(f"Renamed file {doc} to {new_name}")

print(f"Renamed {renamed} of {len(docs)} files")