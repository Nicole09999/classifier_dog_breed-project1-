#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: nicole
# DATE CREATED:26/10/23                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    # part 1 reading the files in the folder 
    from os import listdir
    file_list=listdir(image_dir)
#     file_list=listdir('pet_images/')
#     print("the file names are\n")
#     for i in range(10):
#         print(f"the filename of  {i+1} is {file_list[i]}")
    
    #part 2 creating the pet labels 
    pet_labels=[]
    for i in range(len(file_list)):
        pet_label=""
        low_pet_image=file_list[i].lower()
        word_list=low_pet_image.split('_')
        for word in word_list:
            if word.isalpha():
                pet_label+=word+" "
        pet_label=pet_label.strip()
        pet_labels.append(pet_label)  
#         print(pet_label)
        
    
        
    #part 3 creating a dict to store the values of the labels 
    result_dict={}
#     items_dict=len(result_dict)
#     print(items_dict==0)
    for i in range(len(file_list)):
        if file_list[i] not in result_dict:
            result_dict[file_list[i]]=[pet_labels[i]]
        else:
           print(f"Warning: The file '{file_list[i]}' already exists. File names must be unique, and only immutable objects are allowed as keys.")
   
    
    
    
    
    
    return result_dict
