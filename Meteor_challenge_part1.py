#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Importing LIB PIL useful for digital image processing
from PIL import Image, ImageFilter

#function for counting meteor, stars and FallWater and to get the result
def accountStarsMeteors(img, resultImg): 
    # Variables to store a count starting with zero.
    meteorsCounter = 0 
    starsCounter = 0
    meteorsFallWaterCounter = 0

    waterAxisX = [] 
    
    # Traversing the image as a matrix and findign for pixels that have 
    for i in range(0, img.width): 
        for j in range(0, img.height):
            r,g,b = resultImg.getpixel((i,j)) 

            if ((r == 0) and (g == 0) and (b== 255)):
                waterAxisX.append(i)

    for i in range(0, img.width):
        for j in range(0, img.height):
            r,g,b = resultImg.getpixel((i,j))
            # testing img.putpixel((i,j), (2,119,189)) # Cor Background
            if ((r == 255) and (g == 255) and (b==255)):
                starsCounter += 1
            if ((r == 255) and (g == 0) and (b==0)):
                meteorsCounter +=1
                if(i in waterAxisX):
                    meteorsFallWaterCounter += 1
    # Count printing
    print('RESULTS OF DIGITAL IMAGE PROCESSING:')            
    print(f'Stars in the image: {starsCounter}')
    print(f'Meteors in the image: {meteorsCounter}')
    print(f'Meteors falling in water in the image: {meteorsFallWaterCounter}')
#main function 
if __name__ == '__main__':
    #opening image and converting to RGB
    img = Image.open('meteor_challenge_01.png') 
    resultImg = img.convert('RGB')  
    #Calling function to manipulate image and to get the result for the callenge
    accountStarsMeteors(img, resultImg)


# In[ ]:




