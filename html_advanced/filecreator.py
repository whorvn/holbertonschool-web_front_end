import os

# Get the directory where the Python script is located
directory = os.path.dirname(os.path.abspath(__file__))

# Create files from 9 to 34
for i in range(9, 35):
    filename = f'{i}-index.html'
    filepath = os.path.join(directory, filename)
    
    # Create the file and write a simple HTML template
    with open(filepath, 'w') as file:
        file.write(f'<!DOCTYPE html>\n<html>\n<head>\n<title>{filename}</title>\n</head>\n<body>\n<h1>File {filename}</h1>\n</body>\n</html>')

print("Files created successfully.")
