import os 
import glob
import shutil
import random

image_src_dir = "D:/Development/EXTRA/Python_Image_To_PDF/sampleimages"
parent_dir = "D:/Development/EXTRA/Python_Image_To_PDF/sourcedir"

for x in range(1, 100):
  print("Creating folder: '% s'" % x)
  folderName = "Folder_" + str(x)
  
  path = os.path.join(parent_dir, folderName) 
  os.mkdir(path) 
  print("Directory '% s' created" % folderName) 
  
  randomImage1 = random.randint(1,5)
  randomImage2 = random.randint(1,5)
  
  shutil.copy(image_src_dir + "/" + str(randomImage1) + ".jpg", parent_dir + "/" + folderName + "/")
  shutil.copy(image_src_dir + "/" + str(randomImage2) + ".jpg", parent_dir + "/" + folderName + "/")
  
  

print("Task Completed") 

