import os

from fpdf import FPDF
from PIL import Image


#print(result)
#
#filenames= os.listdir (".")
#
#result = []
#for filename in filenames: # loop through all the files and folders
#    if os.path.isdir(os.path.join(os.path.abspath("."), filename)): # check whether the current object is a folder or not
#        result.append(filename)
#
#result.sort()
#print(result)

folder_parent_path ="D:/Development/EXTRA/Python_Image_To_PDF/sourcedir"
#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(folder_parent_path):
    for dirr in dirs:
        print("Inside " + dirr)
        
        pdf_out_path=folder_parent_path + "/" + dirr
        
        for root, dirs, files in os.walk(folder_parent_path + "/" + dirr):
            filelist = []
            
            for file in files:
                #append the file name to the list
                filelist.append(os.path.join(root,file))
              
            pdf = FPDF('P','mm','A4')

            #pdf.add_page()
            
            #print all the file names
            for name in filelist:
                print(name)
                pdf.add_page()
                pdf.image(name,0,0,50,50)
                # pdf.image(name)
                
            
            pdf.output(pdf_out_path+"/POA_"+dirr+".pdf","F")

        
            


#from fpdf import FPDF
#pdf = FPDF()
## imagelist is the list with all image filenames
#for image in imagelist:
#    pdf.add_page()
#    pdf.image(image,x,y,w,h)
#pdf.output("yourfile.pdf", "F")