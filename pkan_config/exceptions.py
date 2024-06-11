class ConfigFileNotFound(BaseException):
    """
    Raised when the csv file is not found; can occur only while testing
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def __str__(self):
        return 'Config file {} not found'.format(self.file_path)

class DirectoryMissing(BaseException):
    """
    Missing Directory
    """
