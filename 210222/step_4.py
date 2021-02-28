import numpy as np
from PIL import Image

image_name = 'car.jpg'
image = Image.open(image_name)
image_np = np.array(image)
print(image_np.size, image_np.shape)
image_np_conv = image_np + 0.5
image_np_conv[:, :, 2][image_np_conv[:, :, 2] <= 225] += 30
new_image = Image.fromarray(image_np_conv.astype('uint8'))
save_name = 'car_conv.jpg'
new_image.save(save_name)
