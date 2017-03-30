
#! python
'''This script cleans up files before the
next run of the scraper'''
import os

path = "../recipe_files"
fileList = os.listdir(path)
for fileName in fileList:
    os.remove(path+"/"+fileName)

os.remove("../recipes.json") # remove json file
