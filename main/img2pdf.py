import os
import time

from fpdf import FPDF
from PIL import Image
from jproperties import Properties

def show(message):
    print(message)
    time.sleep(2)

current_dir=os.getcwd()

configs = Properties()
with open('config.props', 'rb') as config_file:
    configs.load(config_file)
    
source_dir=configs.get("TARGET_DIR").data
distance=configs.get("DISTANCE").data

folder_parent_path=current_dir + "/" + source_dir
print("Source PDF Directory=" + folder_parent_path)

show("Confirm parameters before proceeding.")

while True:
    try:
        answer = int(input("Please enter 1 to confirm or 0 to stop : "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break
if answer == 1: 
    show("Great - You have confirmed to continue. Process will now start!")
else:
    show("Re-run script with correct parameters. I will exit now.")
    exit()
    

#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(folder_parent_path):
    for dirr in dirs:
        #print("Inside " + dirr)
        
        pdf_out_path=folder_parent_path + "/" + dirr
        
        for root, dirs, files in os.walk(folder_parent_path + "/" + dirr):
            filelist = []
            
            for file in files:
                #append the file name to the list
                filelist.append(os.path.join(root,file))
              
            pdf = FPDF('P','mm','A4')

            #pdf.add_page()
            
            #print all the file names
            for imageFile in filelist:
                cover = Image.open(imageFile)
                width, height = cover.size
                width, height = float(width * 0.264583), float(height * 0.264583)
                pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}
                orientation = 'P' if width < height else 'L'

                width = width if width < pdf_size[orientation]['w'] else pdf_size[orientation]['w']
                height = height if height < pdf_size[orientation]['h'] else pdf_size[orientation]['h']

                pdf.add_page(orientation=orientation)
                pdf.image(imageFile, 0, 0, width, height)
                # END FOR
            
            pdf_out_file=pdf_out_path+"/POA_"+dirr+".pdf"
            print("Writing => "+ pdf_out_file)
            pdf.output(pdf_out_file,"F")
            # END FOR
        
        # END FOR


