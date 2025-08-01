from PyPDF4 import PdfFileMerger
import numpy as np
import os

source_folder = 'D:/Datos/Output/'

def list_files_recursively(directory,extension):
    dirFiles = os.listdir(directory)
    sorted(dirFiles)
    merger = PdfFileMerger(strict=False)
    for file in dirFiles:
        if file.endswith(extension):
            print(file)
            merger.append(fileobj=open(os.path.join(directory,file), 'rb'))
    merger.write(fileobj=open(os.path.join(directory,"JoinFile.pdf"), 'wb'))


list_files_recursively(source_folder,'.pdf')