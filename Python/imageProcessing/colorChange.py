# Author: Ossim Belias
# Date: 2020-07-12
# This code take an image create a contact sheet and modify the intensity of the color of each channel

import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageDraw, ImageFont

# read image and convert to RGB
image=Image.open("C:/Users/Belias/Desktop/ProjetPerso_BacUp/chasingCube/Python/imageProcessing/images/poly.JPG")
image=image.convert('RGB')
font = ImageFont.truetype("C:/Users/Belias/Desktop/ProjetPerso_BacUp/chasingCube/Python/imageProcessing/images/fanwood-webfont.ttf",60)

# build a list of 9 images which have different brightnesses
enhancer=ImageEnhance.Brightness(image)
images=[]
for i in range(1, 10):
    images.append(enhancer.enhance(i/10))

# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

#dictionnaries for the intensity and the row of the contact sheet
intensityDict = {0:0.1,
                    first_image.width:0.5,
                    first_image.width*2: 0.9
                }

rowDict = {0: 0,
            first_image.height: 1,
            first_image.height*2: 2
        }

for img in images:
    #Draw the text on the image
    text = "Channel {} intensity {}".format(rowDict[y], intensityDict[x])
    draw = ImageDraw.Draw(img)
    draw.rectangle((0,image.height - 50, img.width, img.height), fill="black", outline="red")
    draw.text((0,image.height - 50), text, font = font, align ="left") 
    
    #put the appropriate intensity on the image
    img_width, img_height = img.size
    pixels = img.load()
    for i in range(img_width):
        for j in range(img_height):
            row = rowDict[y]
            if row == 0:
                pixels[i,j] = (int(pixels[i,j][0] * intensityDict[x]), pixels[i,j][1], pixels[i,j][2])
            if row == 1:
                pixels[i,j] = (pixels[i,j][0], int(pixels[i,j][1] * intensityDict[x]), pixels[i,j][2])
            if row == 2:
                pixels[i,j] = (pixels[i,j][0], pixels[i,j][1], int(pixels[i,j][2] * intensityDict[x]))
    
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and save the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
contact_sheet = contact_sheet.save("C:/Users/Belias/Desktop/ProjetPerso_BacUp/chasingCube/Python/imageProcessing/images/polyResult.JPG")