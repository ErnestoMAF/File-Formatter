class LineSplitter:
    """A utility class to split a line of text into parts based on a delimiter.

    This class provides a static method to split a line of text into a list of substrings
    using a specified delimiter.
    """

    @staticmethod
    def split_line(line, delimiter=','):
        """Split a line of text into parts using a delimiter.

        Args:
            line (str): The line of text to split.
            delimiter (str, optional): The delimiter to use for splitting. Defaults to ','.

        Returns:
            list: A list of substrings obtained by splitting the line.
        """
        
        return line.split(delimiter)

class LineStructurer:
    """A utility class for structuring split data into a dictionary.

    This class provides a static method to organize a list of split data
    into a dictionary with predefined keys.
    """

    @staticmethod
    def structure_line(split_data):
        """Structure split data into a dictionary with specific keys.

        This method takes a list of split data and organizes it into a dictionary
        with predefined keys. The input list is expected to have at least 5 str elements.

        Args:
            split_data (list): A list containing the data to be structured. The list should
                               have the following order:
                               - Index 0: Hexadecimal numbers (str)
                               - Index 1: First string (str)
                               - Index 2: Second string (str)
                               - Index 3: Third string (str)
                               - Index 4: Third string (str)
                               - Index 5: Decimal numbers (str)

        Returns:
            dict: A dictionary with the following keys:
                  - "hexadecimal_numbers": The hexadecimal numbers from the input list.
                  - "first_string": The first string from the input list.
                  - "second_string": The second string from the input list.
                  - "third_string": The third string from the input list.
                  - "fourth_string": The fourth string from the input list.
                  - "decimal_numbers": The decimal numbers from the input list.
        """

        return {
            "hexadecimal_numbers": split_data[0],
            "first_string": split_data[1],
            "second_string": split_data[2],
            "third_string": split_data[3],
            "fourth_string": split_data[4],
            "decimal_numbers": split_data[5]
        }

class IPv6ProcessorToDecimal:
    """A utility class for processing IPv6 addresses into decimal numbers.

    This class provides methods to manipulate and convert IPv6 addresses,
    such as removing the mask from an IPv6 address and converting hexadecimal
    blocks to their decimal representation.
    """

    @staticmethod
    def remove_mask(hexadecimal_numbers):
        """Remove the IPv6 mask from the given hexadecimal address.

        Args:
            hexadecimal_numbers (str): An IPv6 address in hexadecimal format.

        Returns:
            str: The IPv6 address without the mask.        
        """

        return hexadecimal_numbers.split('/')[0]
    
    @staticmethod
    def convert_hex_to_decimal(hexadecimal_numbers):
        """Convert hexadecimal blocks of an IPv6 address to their decimal representation.

        This method takes an IPv6 address in hexadecimal format and convert each block from hexadecimal to decimal.

        Args:
            hexadecimal_numbers (str): An IPv6 address in hexadecimal format.

        Returns:
            list[int]: A list of integers representing the decimal values of each hexadecimal block in the IPv6 address.
        """        
        
        blocks = hexadecimal_numbers.split(':')
        return [int(block, 16) for block in blocks]

class IPv4ProcessorToHexaDecimal:
    """A utility class for processing decimal numbers, particularly in the context of IPv4 addresses.

    This class provides methods to convert decimal representation IPv4 addresses into hexadecimal.    
    """

    @staticmethod
    def convert_decimal_to_hex(decimal_numbers):
        """Convert decimal octets to their hexadecimal representation.

        This method takes a string of decimal numbers separated by dots and converts each octet to its hexadecimal equivalent

        Args:
            decimal_numbers (str): A string of decimal numbers separated by dots.

        Returns:
            list[str]: A list of hexadecimal strings representing the converted octets.The hexadecimal strings are in uppercase and do not include the '0x' prefix.
        """

        octets = decimal_numbers.split('.')
        return [hex(int(octet))[2:].upper() for octet in octets]

class FormatSingleLine:
    """A class to format a single line of text by splitting, structuring, and processing file data.

    This class uses instances of `LineSplitter`, `LineStructurer`, `IPv6ProcessorToDecimal`, and `IPv4ProcessorToHexaDecimal`
    to process a line of text, extract relevant data, and format it into a specific output format.
    """

    def __init__(self, splitter, structurer, ipv6_processor, ipv4_processor):
        """Initialize the `FormatSingleLine` class with instances of the required processors.

        Args:
            splitter (LineSplitter): An instance of `LineSplitter`.
            structurer (LineStructurer): An instance of `LineStructurer`.
            ipv6_processor (IPv6ProcessorToDecimal): An instance of `IPv6ProcessorToDecimal`.
            ipv4_processor (IPv4ProcessorToHexaDecimal): An instance of `IPv4ProcessorToHexaDecimal`.
        """

        self.splitter = splitter
        self.structurer = structurer
        self.ipv6_processor = ipv6_processor
        self.ipv4_processor = ipv4_processor    
    
    def process_line(self,line):
        """Process a single line of text to extract and format IPv6 and IPv4 addresses.

        This method performs the following steps:
        1. Splits the input line into parts by a delimeter using the `LineSplitter`.
        2. Structures the split data into a dictionary using the `LineStructurer`.
        3. Removes the mask from the IPv6 address and converts it to decimal blocks.
        4. Converts the IPv4 address from decimal to hexadecimal.
        5. Combines the results into a formatted string.

        Args:
            line (str): A line of text to process.

        Returns:
            str: A formatted string containing the second string from the structured data,
                 the decimal representation of the IPv6 address, and the hexadecimal
                 representation of the IPv4 address.
        """
        
        split_line = self.splitter.split_line(line)
        structure_line = self.structurer.structure_line(split_line)
        ivp6_removed = self.ipv6_processor.remove_mask(structure_line["hexadecimal_numbers"])
        decimal_blocks = self.ipv6_processor.convert_hex_to_decimal(ivp6_removed)
        hex_octets = self.ipv4_processor.convert_decimal_to_hex(structure_line["decimal_numbers"])

        decimal_str = ":".join(map(str, decimal_blocks))
        hex_str = ".".join(hex_octets)

        return f"{structure_line['second_string']} {decimal_str}:{hex_str}"
    
class FormatAllFile:
    """A class to process and format all lines in a file using a `FormatSingleLine` instance.

    Attributes:
        line_formatter (FormatSingleLine): An instance of `FormatSingleLine` to process each line.
    """
    
    def __init__(self,line_formatter):
        """Initialize the `FormatAllFile` class with an instance of `FormatSingleLine`.

        Args:
            line_formatter (FormatSingleLine): An instance of `FormatSingleLine`.
        """

        self.line_formatter = line_formatter

    def process_file(self,file_data):
        """Process all lines in a file and return the formatted output.

        This method iterates over each line in the input file data, processes it using
        the `FormatSingleLine` instance, and concatenates the results into a single string.

        Args:
            file_data (list[str]): A list of strings, where each string represents a line in the file.

        Returns:
            str: A single string containing the formatted output for all lines, separated by newlines.
        """
        
        data_processed = ""
        for line in file_data:
            line_processed = self.line_formatter.process_line(line)
            data_processed += line_processed + '\n'
        return data_processed