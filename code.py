import os 
import PyPDF2
from PyPDF2 import PdfReader , PdfWriter, PdfMerger

path = input("Enter the folder location: ")
resultFile = input("\nEnter the name of the result file : ")
if '.pdf' not in resultFile:
    resultFile += '.pdf'

pdfFiles = [] # variable 

for root, dirs, filenames in os.walk(path): # Root and directory pathway.
    for filename in filenames: 
        if filename.lower().endswith('.pdf'):# for loop for all files with .pdf in the name.
            pdfFiles.append(os.path.join(root,filename)) 
            # Appending files to root name from OS (operating system).
            
# Sorting the files by forcing everything to lower case.
pdfFiles.sort(key=str.lower)

# Assigning the pdfWriter() function to pdfWriter.
pdfWriter = PyPDF2.PdfWriter()


for filename in pdfFiles: # Starting a for loop.
    pdfFileObj = open(filename, 'rb') # Opens each of the file paths in filename variable.
    pdfReader = PyPDF2.PdfReader(pdfFileObj) # Reads each of the files in the new varaible you've created above and stores into memory.
    pageObj = pdfReader.pages[0] # Reads only those that are in the varaible.
    pdfWriter.add_page(pageObj) # Adds each of the PDFs it's read to a new page.

# Name of the PDF file can be written here.
if not os.path.exists(path+'/Output'):
    os.mkdir(path+'/Output')
pdfOutput = open(path+'/Output/'+resultFile, 'wb') 

# Writing the output file using the pdfWriter function.
pdfWriter.write(pdfOutput)
pdfOutput.close()