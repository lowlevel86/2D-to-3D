import struct

def loadFloatData(filename):

    floats = []
    with open(filename, 'rb') as file:
        while True:
        
            # read 4 bytes (32 bits) at a time
            bytes_data = file.read(4)
            
            if not bytes_data:
                break  # end of file
                
            # unpack the bytes into a float
            float_value = struct.unpack('f', bytes_data)[0]
            floats.append(float_value)
            
    return floats

