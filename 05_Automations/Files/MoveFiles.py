import shutil
import os
source_folder = 'C:/Users/m0l1n3ta/AulaVirtual4/DATA/.books/dbf0aa4c69ceee58c4850bce7e831a3d393c449b_9788468080338/BK/pages/'

destination_folder = 'D:/Datos/Input/'

def list_files_recursively(directory,extension):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root, file))
                shutil.copy2(os.path.join(root, file), os.path.join(destination_folder,file))



list_files_recursively(source_folder,'.svg')