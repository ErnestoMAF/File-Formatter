class ProcessFile:
    def __init__(self,file,file_line = None):
        self.file = file
        self.file_line = file_line

    def __split_file(self,file_line):
        """Split file by commas in it."""
        return self.file[file_line].split(',')
    
    def __struct_file_line(self,split_data):
        """Split file by commas in it."""
        data = {
            "hexadecimal_numbers": split_data[0],
            "first_string": split_data[1],
            "second_string": split_data[2],
            "third_string": split_data[3],
            "third_string": split_data[4],
            "decimal_numbers": split_data[5]
        }
        return data
       
    def __remove_ipv6_mask(self,hexadecimal_numbers):
        """Remove ipv6 mask"""
        mask_removed = hexadecimal_numbers.split('/')[0]
        return mask_removed
    
    def __convert_hexadecimal_to_decimal(self,hexadecimal_numbers):
        blocks = hexadecimal_numbers.split(':')
        decimal_blocks = [int(block, 16) for block in blocks]
        return decimal_blocks
    
    def __convert_decimal_to_hexadecimal(self,decimal_numbers):
        octets = decimal_numbers.split('.')
        hex_octets = [hex(int(octet))[2:].upper() for octet in octets]
        hexadecimal_numbers = '.'.join(hex_octets)
        return hexadecimal_numbers
    
    def __file_line_output(self,input_struct_data,output_file):
        string = input_struct_data["second_string"]
        ivp6_removed = self.__remove_ipv6_mask(input_struct_data["hexadecimal_numbers"])
        decimales = self.__convert_hexadecimal_to_decimal(ivp6_removed)
        hexadecimales = self.__convert_decimal_to_hexadecimal(input_struct_data["decimal_numbers"])
        
        # Convert list to string
        decimales_str = ":".join(map(str, decimales))
        hexadecimales_str = "".join(map(str, hexadecimales))
        
        output = string + " " + decimales_str + ":" + hexadecimales_str

        with output_file as file:  # Usar 'a' para añadir o 'w' para sobrescribir
            file.write(output + "\n")
        return output
    

    def get_single_file_line_data(self,file_line = None):
        file_line = self.file_line if not file_line else file_line
        split_data = self.__split_file(file_line)
        struct_data = self.__struct_file_line(split_data)
        return struct_data
    
    def process(self,output_file): 
        line_number = 0       
        for line in self.file:
            split_data = self.__split_file(line_number)
            struct_data = self.__struct_file_line(split_data)
            output = self.__file_line_output(struct_data,output_file)
            line_number += 1
        return output
    


    
    
