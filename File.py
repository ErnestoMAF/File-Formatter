class File:
    def __init__(self, open_file):
        """Initializes a File object by reading the contents of the provided file.

        Args:
            open_file: A file object or context manager that supports the `with` statement. This is typically an instance of `OpenFile`.
        
        Attributes:
            file (list): A list containing the lines of the file.
            files_lines (int): The number of lines in the file.
        """
        file = self.__read_file(open_file)
        self.file = file
        self.files_lines = len(file)

    def __read_file(self, open_file):
        """Reads the contents of the file and returns its lines as a list.

        Args:
            open_file: A file object or context manager that supports the `with` statement. This is typically an instance of `OpenFile`.

        Returns:
            list: A list of strings, where each string represents a line in the file.
        """
        with open_file as archivo:
            return archivo.readlines()
        