#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import os.path
import shutil
import sys
from PIL import Image
import threading

SUPPORTED_FORMATS = ('jpg', 'jpeg', 'png')


def create_dirs(raw_images, save_dir):
    for image in raw_images:
        compress_dir = save_dir + '/' + os.path.dirname(image)
        if not os.path.isdir(compress_dir):
            os.makedirs(compress_dir)


def get_raw_images(raw_images_dir):

    if not os.path.isdir(raw_images_dir):
        messagebox.showinfo('Directory Error !',
                            """Input Folder Does not Exist.
        Please Check the Directory and Try Again"""
                            )

    raw_images = []

    for (root, directories, files) in os.walk(raw_images_dir):
        for filename in files:
            if not filename.startswith('.'):
                file_type = filename.split('.')[-1].lower()
                if file_type in SUPPORTED_FORMATS:
                    filepath = os.path.join(root, filename)
                    raw_images.append(filepath.replace(raw_images_dir,
                            ''))

    return raw_images


def change_dir(abs_image_path, raw_images_dir, save_dir):
    custom_dir_path = os.path.dirname(abs_image_path)
    custom_dir_path = custom_dir_path.split('\\')
    compressed_custom_dir_path = save_dir + '/' \
        + '/'.join(custom_dir_path)
    os.chdir(compressed_custom_dir_path)


def compress_and_save(abs_image_path):

    (only_image_path, image_info) = os.path.split(abs_image_path)

    index = image_info.rindex('.')
    (image_name, image_type) = (image_info[:index], image_info[index
                                + 1:])
    optimized_filename = '{}_optimized.{}'.format(image_name,
            image_type)

    im=Image.open(abs_image_path,'r') # Open the image in Read Mode
    pix_val = list(im.getdata())  # get pixel value in RGB format
    #print(pix_val[:10])
    print("Compressing")

    '''a= [x for sets in pix_val for x in sets] #Convert list of tuples into one list 
    print(a[:30])'''

    myRoundedList =  [round(x,-1) for sets in pix_val for x in sets]  #Round integers to nearest 10
    if im.mode in("RGBA","p"):
        b=list(tuple(myRoundedList[i:i+4]) for i in range(0, len(myRoundedList), 4))  #Group list to a tuple of 4 integers
    elif im.mode in("RGB"):
        b=list(tuple(myRoundedList[i:i+3]) for i in range(0, len(myRoundedList), 3))   #Group list to a tuple of 3 integers
    #print(b[:10])
   
    '''list_of_pixels = list(b)
    print(list_of_pixels[:10])'''

    im2 = Image.new(im.mode, im.size) #Create a new image 

    im2.putdata(b) #put image data into the new image 
    
    if im.mode in("RGBA","p"):           #save the file 
        im2.save(optimized_filename,"PNG")
    elif im.mode in("RGB"):
        im2.save(optimized_filename,"JPEG")
      #save the file 
    im.close()
    im2.close()
    '''if not os.path.isfile(optimized_filename):
        source = tinify.from_file(abs_image_path)
        source.to_file(optimized_filename)'''

def main():
    or_folder='Z:\\Modules\\Image Compress\\New\\Pictures'
    co_folder='Z:\\Modules\\Image Compress\\New\\PicturesCompressed'
    raw_images = get_raw_images(or_folder)
    create_dirs(raw_images, co_folder)
    length = len(raw_images)

    for (index, image) in enumerate(raw_images):

        (only_image_path, image_info) = os.path.split(image)
        change_dir(image, or_folder, co_folder)
        compress_and_save(or_folder + '/'
                + image)

if __name__ == "__main__":
    t1 = threading.Thread(target=main)
    t1.start()

