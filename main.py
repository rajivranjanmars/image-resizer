from PIL import Image

image=Image.open("./image-resizer/qr.png")

print("current size of image is: ",image.size)

length=int(input("enter the length of image: "))
width=int(input("enter the width of image: "))
resized_image=image.resize((length,width))
resized_image.save("./image-resizer/qr_resized.png")
print("new size of image is: ",resized_image.size)