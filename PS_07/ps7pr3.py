#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import load_pixels
from hmcpng import save_pixels
from hmcpng import compare_images

def create_green_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are colored green.
        inputs: height and width are non-negative integers
    """
    pixels = []

    for r in range(height):
        row = [[0, 255, 0]] * width
        pixels += [row]

    return pixels

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below
#function 1
def grayscale(pixels):
    """ takes the 2-D list pixels containing pixels for an image, 
    and that creates and returns a new 2-D list of pixels for an 
    image that is a grayscale version of the original image.
    """
    new_pixels = create_green_image(len(pixels), len(pixels[0])) #return new 2-d list instead of modify
    
    for r in range(len(new_pixels)): #len(new_pixels) 和 lem(pixels) 都行，新旧list规模一样
        for c in range(len(new_pixels[0])):
            new_pixels[r][c] = [brightness(pixels[r][c])] * 3 #new_pixels的像素点全是绿的，现在改成灰色，用原始pixels参数
    
    return new_pixels
            

#function 2
def mirror_vert(pixels):
    """ takes the 2-D list pixels containing pixels for an image, 
    and that creates and returns a new 2-D list of pixels for an 
    image in which the original image is “mirrored” vertically.
    """
    height = len(pixels)
    width = len(pixels[0])
    half_height = height // 2
    
    new_pixels = create_green_image(height, width)
    
    for r in range(half_height):
        for c in range(width):
            new_pixels[r][c], new_pixels[height - r - 1][c] = pixels[r][c], pixels[r][c]
      
    if height % 2 != 0:
        middle_row = pixels[half_height]
        pixels[half_height] = middle_row[::-1]

    return new_pixels

                
#function 3
def flip_horiz(pixels):
    """ takes the 2-D list pixels containing pixels for an image, 
    and that creates and returns a new 2-D list of pixels for an 
    image in which the original image is “flipped” horizontally.
    """
    height = len(pixels)
    width = len(pixels[0])
    half_width = width // 2
    
    new_pixels = create_green_image(height, width)
    
    for r in range(height):
        for c in range(half_width):
            new_pixels[r][c], new_pixels[r][width - 1 - c] = pixels[r][width - 1 - c], pixels[r][c]
            
    return new_pixels


#function 4
def extract(pixels, rmin, rmax, cmin, cmax):
    """ takes the 2-D list pixels containing pixels for an image, 
    and that creates and returns a new 2-D list that represents 
    the portion of the original image that is specified by the 
    other four parameters.
    """
    height = len(range(rmin, rmax))
    width = len(range(cmin, cmax))
    
    new_pixels = create_green_image(height, width)
    
    for r in range(rmin, rmax):
        for c in range(cmin, cmax):
            new_pixels[r - rmin][c - cmin] = pixels[r][c]
    
    return new_pixels



    
                
            
    
    
    
            
            