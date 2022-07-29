from PIL import Image
import numpy as np
import glob

# make sure this file is in the same directory as all of the target images
all_imgs = glob.glob('*.png') 

def gray2rgb(img_arr, *, channel_axis=-1):
        return np.stack(3 * (img_arr,), axis=channel_axis)

def crop_rgb_save(img_name): 
    img = Image.open(img_name)

    # convert grayscale to RGB
    img_arr = np.array(img)

    if (len(img_arr.shape) == 2):
        img_arr_rgb = gray2rgb(img_arr)
        img = Image.fromarray(img_arr_rgb, mode='RGB')
        
    
    height = int(img.height)
    width = int(img.width)
    count = 0
    # i = vertical cordinate, j = horizontal cordinate
    for i in range(0, int(height/248)):
        for j in range(0, int(width/248)):
            patch = img.crop((j*248, i*248, (j+1)*248, (i+1)*248))
            count += 1
            patch.save("cropped_images/" + img_name + "_patch" + str(count) + ".png")

    img.close()

for img_name in all_imgs:
    crop_rgb_save(img_name)