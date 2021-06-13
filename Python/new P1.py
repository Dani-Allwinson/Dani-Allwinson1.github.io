import Image , ImageFilter
before = image.open("D:\gamer.PNG")
after = before.filter(ImageFilter.BoxBlur(5))
after.save("d:\blurimage.PNG")