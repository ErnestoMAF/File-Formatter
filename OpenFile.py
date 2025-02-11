class OpenFile:
    def __init__(self, file_path, mode='r'):
        """Initializes the context for opening a file.

        Args:
            file_path (str): The path of the file to be opened.
            mode (str, optional): The mode in which the file is opened. Defaults to 'r' (read).
        """
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Opens the file and returns it for use within the `with` block.

        Returns:
            file: The opened file object.
        """
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closes the file when exiting the `with` block and raise and exception if error.

        Args:
            exc_type (type): The type of exception if one occurred.
            exc_val (Exception): The exception instance if one occurred.
            exc_tb (traceback): The traceback object if an exception occurred.
        """
        self.file.close()

        if exc_type is not None:
            print(f"An exception occurred: {exc_type} - {exc_val}")
