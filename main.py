from OpenFile import OpenFile
from ProcessFile import ProcessFile
from File import File

if __name__ == "__main__":
    file_src = 'src/test.txt' 
    open_file = OpenFile(file_src)
    file= File(open_file)
    process_file = ProcessFile(file.file)
    output_file_src = 'src/output.txt'
    output_open_file = OpenFile(output_file_src,'a')
    process_file.process(output_open_file)
          