from typing import SupportsIndex
import PyPDF2
import os 
import sys
inputs = sys.argv[1:]

def pdf_combiner(pdf_list):

    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list[:len(pdf_list) - 1] :
        merger.append(f'./SamplePDF/{pdf}')
    merger.write('super.pdf')    
   

pdf_combiner(inputs)

