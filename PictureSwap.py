import os
import shutil
from alive_progress import alive_bar
import time


class PictureFolder:

    def __init__(self, folder_path):

        if not isinstance(folder_path, str):
            raise TypeError("Input must be string")

        self.folder_path = folder_path

    def get_all_files(self):

        return [file for file in os.listdir(self.folder_path) if file.endswith('.jpg')]


class PersonalPicture(PictureFolder):

    def __init__(self, picture_path, names_of_hr_pictures, folder_path):

        super().__init__(folder_path)

        def string_check(string):
            if isinstance(string, list):
                for i in string:
                    if not isinstance(i, str):
                        raise TypeError("Input must be string")
                    if not i.endswith('.jpg'):
                        raise TypeError('Input must be jpg image')
            else:
                if not isinstance(string, str):
                    raise TypeError("Input must be string")
                if not string.endswith('.jpg'):
                    raise TypeError('Input must be jpg image')

        string_check(picture_path)
        string_check(names_of_hr_pictures)

        self.picture_path = picture_path
        self.names_of_hr_picture = names_of_hr_pictures

    def swap_picture(self):
        with alive_bar(len(self.names_of_hr_picture)) as bar:
            for element in self.names_of_hr_picture:
                element_path = self.folder_path + '\\' + element
                os.remove(element_path)
                shutil.copy(self.picture_path, element_path)
                time.sleep(0.001)
                bar()


if __name__ == "__main__":

    Path = r'C:\Users\Public\Pictures'
    PicturePath = r'C:\Users\sramekf\Downloads\index.jpg'

    folder_object = PictureFolder(Path)
    personal_picture_object = PersonalPicture(PicturePath, folder_object.get_all_files(), Path)
    personal_picture_object.swap_picture()
