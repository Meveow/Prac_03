import os


def main():
    dict = {}
    os.chdir('FilesToSort')  # opens directory
    for file in os.listdir('.'):
        extension = file.split('.')[-1]
        if extension not in dict:
            sort = input("What category would you like to sort {} files into? ".format(extension))
            dict[extension] = sort
            try:
                os.mkdir(sort)
            except FileExistsError:
                pass

        os.rename(file, f"{dict[extension]}/{file}")


main()
