class File:
    def __init__(self, open_file):
        """Initializes a File object by reading the contents of the provided file.

        Args:
            open_file: A file object or context manager that supports the `with` statement.
        
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

class FileReader:
    """A class to read lines from a file.

    This class provides methods to read a specific line or all lines from a file
    or a list of file lines.

    Attributes:
        file (file object): Content the file object.
    """    
    
    def __init__(self, file):
        """Initialize the FileReader with a file or list of lines.

        Args:
            file (list or file object): The file content as a list of lines or a file object.
        """

        self.file = file

    def read_line(self, line_number):
        """Read a specific line from the file.

        Args:
            line_number (int): The index of the line to read (0-based).

        Returns:
            str: The content of the specified line.

        """
        return self.file[line_number]

    def read_all_lines(self):
        """Read all lines from the file.

        Returns:
            list: A list of strings, where each string represents a line in the file.
        """
        return self.file

class FileWriter:
    """A utility class for writing data to a file.

    This class provides a static method to write content to a file.
    """

    @staticmethod
    def write_file(open_file, output):
        """Write the provided output to the specified file.

        This method opens the file in write mode and writes the given output to it.

        Args:
            open_file: A file object that supports the `with` statement.This is typically an instance of `OpenFile`.
            output (str): The content to write to the file.
        """
        
        with open_file as file:
            file.write(output)

        