import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img= Image.open('download.png')
array = np.asarray(img)

print (array)



rotate=np.rot90(array)
plt.imshow(rotate)
plt.show()

flip=np.fliplr(array)
plt.imshow(flip)

plt.show()

image = np.dot (num[..., :3], [0.299, 0.587, 0.114])
plt.imshow(image, cmap='gray')
plt.show()











