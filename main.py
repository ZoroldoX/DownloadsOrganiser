#!/usr/bin/python3
import os
import shutil
import re


downloadsDir = os.chdir('/Users/dhruv/Downloads') #change to the absolute path of your downloads
files = os.listdir(downloadsDir)
excluded_extensions = ['pdf', 'jpeg', 'jpg', 'png', 'gif', 'bmp', 'zip', 'doc', 'docx', 'epub', 'dmg']# add non miscallenous file extensions here here!

def zipmover(f):
    zipdest = '/Users/dhruv/Downloads/ZIP'
    dst = os.path.join(zipdest,os.path.basename(f))
    shutil.move(f,dst)
    print("Moved "+f+"-->"+zipdest)

def imgmover(f):
    imgdest = '/Users/dhruv/Downloads/IMAGES'
    dst = os.path.join(imgdest,os.path.basename(f))
    shutil.move(f,dst)
    print("Moved "+f+"-->"+imgdest)

def docmover(f):
    docdest = '/Users/dhruv/Downloads/DOCX'
    dst = os.path.join(docdest,os.path.basename(f))
    shutil.move(f,dst)
    print("Moved "+f+"-->"+docdest)

def pdfmover(f):
    pdfdest = '/Users/dhruv/Downloads/PDF'
    dst = os.path.join(pdfdest,os.path.basename(f))
    shutil.move(f,dst)
    print("Moved "+f+"-->"+pdfdest) 

def dmgmover(f):
    dmgdest = '/Users/dhruv/Downloads/DMG'
    dst = os.path.join(dmgdest,os.path.basename(f))
    shutil.move(f,dst)
    print("Moved "+f+"-->"+dmgdest) 
def epubmover(f):
    epubdest = '/Users/dhruv/Downloads/Books'
    dst = os.path.join(epubdest,os.path.basename(f))
    shutil.move(f,dst)
    print("Moved "+f+"-->"+epubdest) 

def miscmover(f):
    miscdest = '/Users/dhruv/Downloads/MISC'
    dst = os.path.join(miscdest,os.path.basename(f))
    shutil.move(f,dst)
    print("Moved "+f+"-->"+miscdest) 



for f in files:
    print("checking...")
    m1 = re.search('\.zip$',f)
    if m1:
        zipmover(f)
    m2 = re.search('\.doc|.docx$',f)
    if m2:
        docmover(f)
    m3 = re.search('\.pdf$',f)
    if m3:
        pdfmover(f)
    m4 = re.search('\.dmg$',f)
    if m4:
        dmgmover(f)
    m5 = re.search(r'(?i)\.((?:jpeg|jpg|png|gif|bmp))$', f)
    if m5:
        imgmover(f)
    m6 = re.search('\.epub', f)
    if m6:
        epubmover(f)
    m7 = re.search(r'(?i)\.(?!' + '|'.join(excluded_extensions) + r'\b)\w+$',f)
    if m7:
        miscmover(f)
    
    
    
        
