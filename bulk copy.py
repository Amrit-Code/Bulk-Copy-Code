#This code must be in the same directory as your images
import os
import shutil
#Use the array below to type the names of the files you want to copy
images = [
6839,
6845,
7102,
7110,
7111,
7117,
7169,
7211,
7215,
7369,
7369,
7375,
7478,
6929,
6934,
6945,
6843,
7100,
7299,
7048,
7186,
7190,
7223,
7518
]
#Make sure you have an empty file called "editPics" that already exists
#This code workds for files in the format "DSC00000.ARW" There are five numbers
#Thus the code adds 0's before the numbers in the aray above to make it 5 digits
#Then the files are coppied accordingly, change to suite ur naming convention
src_dir = os.getcwd()
dest_file = src_dir + "/editPics"

for i in images:
    prefix = (5 - len(str(i))) * "0"
    print(i)

    shutil.copy(src_dir+"/DSC"+prefix+str(i)+".ARW" ,dest_file)
