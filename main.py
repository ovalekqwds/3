from PIL import Image
import os
for number in range(5):
    file_path=f"photo_end_{number}"
    if not os.path.isdir(file_path):
        os.mkdir(file_path)
    image=Image.open(f"photo{number}.jpg")
    image_vk=image.resize((1400,1000))
    image_vk.save(f"{file_path}/vk.png","png")
    image_inst=image.resize((1080,1080))
    coordinates=(10, 0, image_inst.width-10, image_inst.height)
    image_inst = image_inst.crop(coordinates)
    image_inst.save(f"{file_path}/inst.png","png")
    image_fb=image.resize((1200,628))
    image_fb.save(f"{file_path}/fb.png","png")