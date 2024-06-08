def read_file(filename):
  """Reads the contents of a file and returns them as a string."""
  try:
    with open(filename, 'r') as file:
      return file.read()
  except FileNotFoundError:
    print("Error: File not found.")
    return ""

def write_file(filename, content):
  """Writes content to a file."""
  with open(filename, 'w') as file:
    file.write(content)
    print("Content written to", filename)

filename = input("Enter the filename to read: ")
content = read_file(filename)
if content:
  print("File contents:\n", content)

new_content = input("Enter content to write to a new file (or 'q' to quit): ")
if new_content != 'q':
  new_filename = input("Enter the filename for the new file: ")
  write_file(new_filename, new_content)
