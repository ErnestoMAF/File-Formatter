class File:
    def __init__(self,open_file,output=False):
        file = self.__read_file(open_file)
        self.file = file
        self.files_lines = len(file)
        
    def __read_file(self,open_file):
        """Read open file content using OpenFile."""
        with open_file as archivo:
            return archivo.readlines()
        
        