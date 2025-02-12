from OpenFile import OpenFile
from ProcessFile import *
from File import *

if __name__ == "__main__":
    """
    Main script to process a file, format its content, and write the results to an output file.

    This script performs the following steps:
        1. Opens an input file for reading and an output file for writing.
        2. Reads the content of the input file using the `File` class.
        3. Processes each line of the file using the `FormatSingleLine` and `FormatAllFile` classes.
        - Splits each line into parts.
        - Structures the data into a dictionary.
        - Processes IPv6 and IPv4 addresses.
        - Formats the data into a specific output format.
        4. Writes the formatted data to the output file using the `FileWriter` class.
    """
    input_file_src = 'src/test.txt'
    output_file_src = 'src/output.txt'

    open_file = OpenFile(input_file_src)
    output_open_file = OpenFile(output_file_src,'w')

    file= File(open_file)
    file_reader = FileReader(file.file)    

    splitter = LineSplitter()
    structurer = LineStructurer()
    ipv6_processor = IPv6ProcessorToDecimal()
    ipv4_processor = IPv4ProcessorToHexaDecimal()
    line_formatter = FormatSingleLine(splitter, structurer, ipv6_processor, ipv4_processor)
    file_formatter = FormatAllFile(line_formatter)
    file_formated_data = file_formatter.process_file(file_reader.read_all_lines())
    
    FileWriter.write_file(output_open_file,file_formated_data)

          