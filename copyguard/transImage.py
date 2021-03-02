import glob
import os
import shutil
import sys

dummy_fname = "tuxedoMask"

# make dummy dir
try:
    os.mkdir("./../dummy")
except:
    print("warning : dir already exist\n")

# search image file in file img
extension = ["jpg","png","eps"]
for ex in extension:
    files = glob.glob("./../img/*."+ex) 
    for file in files:
        dname = "./"+dummy_fname+"."+ex
        print(file[9:]+" -> "+dname)
        shutil.copyfile(dname,"./../dummy/"+file[9:])