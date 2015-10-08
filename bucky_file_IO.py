# OPEN a file
            # (or create it if it doesn't exist)

file_object = open("sample_file.txt", "w")          # W - Writing mode

file_object.write("Abstract\n")
file_object.write("Once upon a time in a galaxy far far away...\n")

file_object.close()



# READING a file

file2 = open("sample_file.txt", "r")      # R - Reading mode

text = file2.read()                       # put file's data into a text variable

print(text)

file2.close()