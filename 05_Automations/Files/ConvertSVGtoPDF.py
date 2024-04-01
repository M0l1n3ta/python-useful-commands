from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
import os

source_folder = 'D:/Datos/Input/'
output_folder = 'D:/Datos/Output/'

def list_files_recursively(source,output,extension):
    for root, dirs, files in os.walk(source):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root, file))
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output, "{0:0>3}.pdf".format(file.split(".")[0]))
                drawing = svg2rlg(input_file_path  )
                renderPDF.drawToFile(drawing, output_file_path)
                



list_files_recursively(source_folder,output_folder,'.svg')