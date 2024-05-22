from pprint import pprint

file_name = 'read_.txt'
print(file_name)
file = open(file_name, mode='rb')
file_content = file.read()
file.close()
pprint(file_content)