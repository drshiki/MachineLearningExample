from PIL import Image
import numpy as np
import matplotlib.pylab as plt
k = 1
for a in [5,7,8]:
    im=Image.open(str(a)+"test.jpg")
    img_gray=im.convert("L")
    #img = np.array(im)
    arr = []
    for i in range(28):
        for j in range(28):
            pixel = 1.0 - float(img_gray.getpixel((j, i)))/255.0
            arr.append(pixel)
    img_np_array = np.array(arr).reshape(28,28)
    #print(img_np_array)
    plt.subplot(2,2,k)
    k+=1
    plt.imshow(img_np_array)
plt.show()

