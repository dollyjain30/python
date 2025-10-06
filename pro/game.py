from PyPDF2 import PdfWriter
merger =PdfWriter()
pdfs=[]
n=int(input("how many pdf you want to merge"))

for i in range(0,n):
    name=input("enter the name of the pdf")
    pdfs.append(name)
for pdf in pdfs:
    merger.append(pdf)
merger.write("merge.pdf")
merger.close()        
    