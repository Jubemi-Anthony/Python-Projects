from PIL import Image

image = Image.open('AJM_2860-min.jpg')

resized_image = image.resize((3000,3000))
resized_image.save('resizedImage.jpg')
print('DONE!')