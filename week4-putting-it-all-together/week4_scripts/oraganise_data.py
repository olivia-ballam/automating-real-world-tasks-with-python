

def read_data(text_file):

    # Open and read text file. 
    with open(text_file, 'r') as f:
        name = f.readline().strip()
        weight = f.readline().strip()
        description = f.read.strip()

