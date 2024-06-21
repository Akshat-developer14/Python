import os

# Select the directory whose content you want to list
directory_path = '/Users/aksha/PycharmProjects/Python_Projects'

# Use the os module to list the directory content
contents = os.listdir(directory_path)

# Print the contents of the directory
print(contents)