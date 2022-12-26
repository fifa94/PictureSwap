import os


class PictureFolder:

    def __init__(self, folder_path):

        if not isinstance(folder_path, str):
            raise TypeError("Input must be string")

        self.folder_path = folder_path
        self.list_of_files = []

    def get_all_files(self):

        self.list_of_files = [file for file in os.listdir(self.folder_path) if file.endswith('.jpg')]

        return self.list_of_files


Path = 'C:\\Users\\Public\\Pictures'

folder_object = PictureFolder(Path)
print(folder_object.get_all_files())
