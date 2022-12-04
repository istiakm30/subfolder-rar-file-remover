
import os
import shutil

#get the current working directory
cwd = os.getcwd()

#loop through the mainf folder
for root, dirs, files in os.walk(cwd):
    #loop through the folders and subfolders
    for dir in dirs:
        for dir_name, subdirs, files in os.walk(os.path.join(root, dir)):
            #loop through the files
            for file in files:
                #check if the file is an RAR file
                if file.endswith('.rar'):
                    #unrar the file
                    os.system('unrar x {} {}'.format(os.path.join(root, dir, file), os.path.join(root, dir)))
                    #delete the RAR file
                    os.remove(os.path.join(root, dir, file))
