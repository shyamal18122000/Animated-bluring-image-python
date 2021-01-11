import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def blur(img,kernel_size):
    return cv.blur(img,(kernel_size,kernel_size))

def join(img,type='blur'):
    list_images=[]
    if(type=='blur'):
        for i in range(3,501,2):
            temp=blur(img,i)
            list_images.append(temp[:,:,0])
        return list_images

#To read images.
img=cv.imread("my image.jpg",1)
list_blurs=join(img,"blur")

#To show the image loaded and with the effect added.
fig=plt.figure(figsize=(15,15))
img_sample=list_blurs[0]
plt.imshow(img_sample,cmap='jet')

reverse_list_blurs=list_blurs[::-1]
print(len(list_blurs),len(reverse_list_blurs))

#To make the video with gradual blurring.
from matplotlib import animation
fig=plt.figure()
plt.axis("off")
ims=[]
for blurred in list_blurs:
    im=plt.imshow(blurred,animated=True,cmap='seismic')
    ims.append([im])
for rev_blurred in reverse_list_blurs:
    im=plt.imshow(rev_blurred,animated=True,cmap='seismic')
    ims.append([im])
ani=animation.ArtistAnimation(fig,ims,interval=84,blit=True,repeat_delay=1000)
writergif = animation.PillowWriter(fps=30)
ani.save('filename.gif',writer=writergif)