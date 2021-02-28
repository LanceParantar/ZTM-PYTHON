import sys
import os 
from PIL import Image
import time 

def transfer_to_new_folder(parent_dir, filename, new_dir):
    img = Image.open(f'{parent_dir}//Images//{filename}')

    clean_name = os.path.splitext(filename)[0]
    # save the image to the new directory
    img.save(f'C://My Projects//Projects//Image Processing//{new_dir}//{clean_name}.png', 'png')


def scan_directory(parent_dir, new_dir):
    for filename in os.listdir(f'{parent_dir}//Images'):
        transfer_to_new_folder(parent_dir, filename, new_dir)

if __name__ == "__main__":

    image_folder = sys.argv[1]
    new_folder = sys.argv[2]
    
    parent_dir = 'C://My Projects//Projects//Image Processing//'
    new_dir = new_folder
    path = os.path.join(parent_dir, new_dir)

    # create a directory# check is new/ exist, if not create it 
    try:
        if not os.path.exists(new_folder):
            os.mkdir(path)
            print(f'Directory {new_dir} has been created!')  
    except OSError as err:
        print(err)
    start_time = time.time()
    scan_directory(parent_dir, new_dir)
    print(time.time() - start_time)

   