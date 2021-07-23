from PIL import Image

img_base = Image.open("fleur.jpg")
img_modif = Image.new("RGB", img_base.size)

largeur = img_base.width
hauteur = img_base.height


for x in range(largeur):
  for y in range(hauteur):
    pixel = img_base.getpixel((x, y))
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    
    new_r = r
    new_g = g
    new_b = b
    
    new_pixel = (new_r, new_g, new_b)
    img_modif.putpixel((x, y), new_pixel)
  
img_modif.show()
img_modif.save("new_fleur.jpg")