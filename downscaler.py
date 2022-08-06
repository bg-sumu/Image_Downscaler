import cv2 as cv
import numpy as np

#Size of the Downscaled Image
canvas_size = (1000,500)

scale_down_iter = 7 #Value which determines in how much percentage should the Scale Down iter through

try:
    #Reading an Image
    img = cv.imread(f"image.jpg")

    #Calculating Dimensions of the Image
    h,w,l = img.shape
    print(f"Dimensions of Image = {img.shape}")
    print(F"Downscaled Image Dimensions = {canvas_size}")

    #Scaling Down an Image
    for i in range(scale_down_iter,100,scale_down_iter):
        hsc = h-((i/100)*h)
        wsc = w-((i/100)*w)

        #Shows the Live Scaling down of Image Use itwhen Needed
        """print(f"height scaled down to {100-i}% = {hsc}")
        print(f"width scaled down to {100-i}% = {wsc}")
        print(f"Ratio == {h/w}")
        print("\n")"""
        if((hsc <= canvas_size[0]) and (wsc <= canvas_size[1]) ) :
            h = hsc
            w = wsc
            break

    #calculating new dimensions of Resaled image
    dim=(int(w),int(h)) #passed to resize Function should be in the Form of Width,height

    #Calculating space for Padding
    h_r = canvas_size[0]-dim[1]
    w_r = canvas_size[1]-dim[0]
    print(w_r,h_r)

    #Rescaling the Image
    img_resize = cv.resize(img, dim, interpolation = cv.INTER_AREA)

    ## Adding Padding to an Image
    old_image_height, old_image_width, channels = img_resize.shape

    # create new image of desired size and color for padding
    new_image_width =  old_image_width + w_r
    new_image_height = old_image_height + h_r
    color = (255,255,255)
    result = np.full((new_image_height,new_image_width, channels), color, dtype=np.uint8)

    # compute center offset
    x_center = (new_image_width - old_image_width) // 2
    y_center = (new_image_height - old_image_height) // 2

    # copy img image into center of result image
    result[y_center:y_center+old_image_height, 
        x_center:x_center+old_image_width] = img_resize

    img_resize = result

    cv.imwrite(f"reshaped_image_{scale_down_iter}.jpg",img_resize)
    print(f"Dimensions of Downscaled Image Output : {img_resize.shape}")

except:
    print("\nImage Can't be Rescaled down to the Size Specified, Enter a New Shape and Try Again.")
