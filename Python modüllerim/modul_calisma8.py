from PIL import Image,ImageFilter

resim = Image.open("papağan.jpg")

#resim.show()

resim.save("papağan2.jpg")

resim.rotate(180).save("papağan3.jpg")

resim.convert(mode = "L").save("papağan4.jpg")

daralt = (400,250)

resim.thumbnail(daralt)

resim.save("papağan5.jpg")

resim.filter(ImageFilter.GaussianBlur(10)).save("papağan6.jpg")

resim2 = Image.open("Atatürk.jpg")

kırp = (168,0,509,391)

resim2.crop(kırp).save("Mustafa Kemal.jpg")
                                                                                                               