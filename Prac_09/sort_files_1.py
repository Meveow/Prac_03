import os
import shutil


def main():
    os.chdir('FilesToSort')  # opens directory
    for file in os.listdir('.'):
        ext = file.split('.')[-1]  # splits extension (eg: .doc)
        try:
            os.mkdir(f'{ext}')  # creates directory using variable
        except FileExistsError:
            print("Already exists")
        shutil.move(file, "{}".format(ext))  # moves file into directory


main()
