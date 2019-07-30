from PIL import Image, ImageDraw, ImageFont
import time

start_time = time.time()

def createPic():
    im = Image.new("RGB", (1280, 1024), "black")
    draw = ImageDraw.Draw(im)
     
    icon = Image.open("qr.png")
    shot = Image.open("2018-05-21-210948PiShots.JPG")
    # get the correct size
    x, y = icon.size
    im.paste(icon, (50,50))
    shoted = shot.resize((854,568),Image.ANTIALIAS)
    im.paste(shoted, (400,400))
    fnt = ImageFont.truetype('arial.ttf', 100)
    
    d = ImageDraw.Draw(im)
    d.text((400,100), "Sample Text1?", font=fnt, fill=(255,255,255))
    c = ImageDraw.Draw(im)
    c.text((400,200), "Sample Text 2!", font=fnt, fill=(255,255,255))
    
    del draw
    im.save("test.jpg", "JPEG")
    
createPic()
print("--- %s seconds ---" % (time.time() - start_time))