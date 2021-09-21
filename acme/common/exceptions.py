FILE_NOT_FOUND_ERROR = 'file was not fount. Please add or create the file in resource folder.'


class FileNotFoundException(Exception):
    def __init__(self, file_name):
        self.file_name = file_name
        super().__init__('{0} {1}'.format(file_name, FILE_NOT_FOUND_ERROR))
