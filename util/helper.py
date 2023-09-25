

import os

def get_all_files_in_directory(directory_path):
    file_paths = []

    for foldername, subfolders, filenames in os.walk(directory_path):
        for filename in filenames:
            file_paths.append(os.path.join(foldername, filename))

    return file_paths

## directory = "/path/to/your/directory"  # Replace this with your directory path
## all_files = get_all_files_in_directory(directory)

## for file_path in all_files:
##     print(file_path)


#Helper function for printing docs

def pretty_print_docs(docs):
    print(f"\n{'-' * 100}\n".join([f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]))