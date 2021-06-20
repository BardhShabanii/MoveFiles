import os
import shutil

source = input("Please give directory source path:")
dest = input("Please give directory destination path:")

img_folder = r"C:\Users\bardh\Desktop\ick-python-advanced\mini projects\MoveFiles\Dest Path\Images"
vid_folder = r"C:\Users\bardh\Desktop\ick-python-advanced\mini projects\MoveFiles\Dest Path\Videos"
aud_folder = r"C:\Users\bardh\Desktop\ick-python-advanced\mini projects\MoveFiles\Dest Path\Audios"
software_folder = r"C:\Users\bardh\Desktop\ick-python-advanced\mini projects\MoveFiles\Dest Path\Software"
doc_folder = r"C:\Users\bardh\Desktop\ick-python-advanced\mini projects\MoveFiles\Dest Path\Documents"
other_folder = r"C:\Users\bardh\Desktop\ick-python-advanced\mini projects\MoveFiles\Dest Path\Other"

files = os.listdir(source)  # takes list of files in folder
for file in files:  # takes each file of folder one by one
    suffix = (os.path.splitext(file))[-1]  # suffixes are split from source
    print(suffix)
    print('asd')
    print(file)
    if suffix == '.jpg' or suffix == '.jpeg':
        shutil.move(f"{source}/{file}", img_folder)

    elif suffix == '.mp4' or suffix == '.mov':
        shutil.move(f"{source}/{file}", vid_folder)

    elif suffix == '.WAV' or suffix == '.mp3':
        shutil.move(f"{source}/{file}", aud_folder)

    elif suffix == '.' or suffix == '.exe':
        shutil.move(f"{source}/{file}", software_folder)

    elif suffix == '.PDF' or suffix == '.DOC':
        shutil.move(f"{source}/{file}", doc_folder)

    else:
        shutil.move(f"{source}/{file}", other_folder)

    # new_path = shutil.move(f"{source}/{file}", dest)  # moves files to new folder, takes source from user input, file from organised files
    # print(new_path)

entry = input("Please give your source directory path here: ")
source = os.listdir(entry)
# entries = os.listdir(r"C:\Users\bardh\Desktop\ick-python-advanced\mini projects\MoveFiles")

print(source)
