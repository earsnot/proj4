from PIL import Image, ImageTk, ImageTransform

bg_image = Image.open(r"C:\dev\proj4\gui\modules\bg.png")
scale = bg_image.size
bg_image = bg_image.resize((137, 79), Image.ANTIALIAS)
bg_image.save('lol.png', 'png')
#resizing image wil PIL
#q_icon = Image.open(r"C:\dev\proj4\gui\modules\stop.png")
#q_icon = q_icon.resize((21, 21), Image.ANTIALIAS)
#q_icon.save('resized.png', 'png')

print(scale)
