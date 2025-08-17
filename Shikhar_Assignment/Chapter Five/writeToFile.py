def write_data(filename, data):
    try:
        with open(filename, 'w') as file:
            file.write(data)
        print(f"Data successfully written to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

# Usage
data_to_write = """This is line 1
This is line 2
This is line 3"""
write_data("output.txt", data_to_write)