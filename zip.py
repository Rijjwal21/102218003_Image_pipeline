import sys
import os
import zipfile

def zip_folder (input_folder, output_zip):
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, input_folder))
                
                
    print(f"Folder '{input_folder}' has been zipped successfully into 'output_zip'.")
    
    
if __name__ == "__main__":
    folder_path = sys.argv[1]
    zip_name = sys.argv[2]

    zip_folder(folder_path, zip_name)
    print(f"Folder '{folder_path}' has been zipped successfully into '{zip_name}'.")