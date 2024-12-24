from PIL import Image

image = Image.open('monro.jpg')
image = image.convert('RGB')

red, green, blue = image.split()

coordinates1 = (100, 0, image.width, image.height)
red_left_cropped = red.crop(coordinates1)
coordinates2 = (50, 0, 646, image.height)
red_right_cropped = red.crop(coordinates2)
red_blended = Image.blend(red_left_cropped, red_right_cropped, 0.5)

coordinates1 = (0, 0, 596, image.height)
blue_left_cropped = blue.crop(coordinates1)
coordinates2 = (50, 0, 646, image.height)
blue_right_cropped = blue.crop(coordinates2)
blue_blended = Image.blend(blue_left_cropped, blue_right_cropped, 0.5)

coordinates3 = (50, 0, 646, image.height)
green_cropped = green.crop(coordinates3)

mix_image = Image.merge('RGB', (red_blended, green_cropped, blue_blended))
mix_image.save('bias_moro.jpg')

mix_image.thumbnail((80, 80))
mix_image.save('ava.jpg')

