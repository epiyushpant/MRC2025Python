def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found!"
    except IOError:
        return "Error reading file!"

# Usage
file_content = read_file("output.txt")
print("File content:")
print(file_content)