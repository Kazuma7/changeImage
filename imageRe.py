from PIL import Image
import os
import glob

files = glob.glob('./image/*')

for i, f in enumerate(files):
    try:
        img = Image.open(f)
        img_resize = img.resize((960, int(img.height*960/img.width)))
        title, ext = os.path.splitext(f)
        print(title)
        print(ext)
        img_resize.save('./Reimage/' + str(i) + ext, quality = 60)
    except OSError as e:
        pass
