from PIL import Image

image1 = Image.open("girl.jpg")

area = (120,0,260,140)

cropped_image1 = image1.crop(area)

brian = Image.open("145.jpg")

dimensions = (260-120, 140-0)           # (140,140)

area_to_insert = (100,100,240,240)

brian.paste(cropped_image1, area_to_insert)

brian.show()


image3 = Image.open("chick_pussy.jpg")

r, g, b = image3.split()

new_img = Image.merge("RGB", (r,g,b))


model = Image.open("model.jpg")
brian = Image.open("145.jpg")

r2, g2, b2 = brian.split()
r3, g3, b3 = model.split()

combined_img = Image.merge("RGB", (r2,g3,b3))
combined_img.show()


# RESIZING

marine = Image.open("sc2marine.jpg")            # 225 x 225 image

marine.show()

small_marine = marine.resize((50,50))         # takes TUPIL as a parameter.

small_marine.show()

large_marine = marine.resize((500,500))

large_marine.show()

flipped_marine = marine.transpose(Image.FLIP_LEFT_RIGHT)

flipped_marine.show()

rotated_marine = marine.transpose(Image.ROTATE_90)          # rotates COUNTER-CLOCKWISE

rotated_marine.show()

