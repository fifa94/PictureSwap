import os


class PictureFolder:

    def __init__(self, folder_path):

        if not isinstance(folder_path, str):
            raise TypeError("Input must be string")

        self.folder_path = folder_path

    def get_all_files(self):

        return [file for file in os.listdir(self.folder_path) if file.endswith('.jpg')]


class PersonalPicture:

    def __init__(self, picture_path, names_of_hr_pictures):

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




Path = 'C:\\Users\\Public\\Pictures'
PicturePath = 'C:\\Users\\sramekf\\Desktop\\FotkyZaloha\\IMG_20170810_211241.jpg'

folder_object = PictureFolder(Path)
personal_picture_object = PersonalPicture(PicturePath,folder_object.get_all_files())
#personal_picture_object = PersonalPicture(PicturePath,['tesxt',1])
print(folder_object.get_all_files())
