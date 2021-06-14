import os
import shutil

path = '/home/source/images.jpg'

suffix = (os.path.splitext(path))
print(suffix)
# mi da nbaz t suffixave

os.mkdir(r"C:\Users\bardh\Desktop\ick-python-advanced\mini projects\MoveFiles\Images")
os.mkdir(r"C:\Users\bardh\Desktop\ick-python-advanced\mini projects\MoveFiles\Videos")
os.mkdir(r"C:\Users\bardh\Desktop\ick-python-advanced\mini projects\MoveFiles\Audios")

if suffix == '.jpg':
    #me marr source me qit te dest me shutil.move
    shutil.move()

entry = input("Please give your source directory path here: ")
source = os.listdir(entry)
# entries = os.listdir(r"C:\Users\bardh\Desktop\ick-python-advanced\mini projects\MoveFiles")
print(source)

os.makedirs
