# learning b file

# learning b file

# x - creating a file in binary mode
with open("L_10_2.bin", "xb") as f:
    f.write(b"This is f\n")   # notice the b before string

# r - reading the content inside the file
with open("L_10_2.bin", "rb") as f:
    print(f.read())   # will show bytes like b'This is f\n'

# w - changing the previous content by writing new ones
with open("L_10_2.bin", "wb") as f:
    f.write(b"This is the second line\n")

# a - adding new lines into the current file without removing the previous ones
with open("L_10_2.bin", "ab") as f:
    f.write(b"This is the third line.\n")

# read final content
with open("L_10_2.bin", "rb") as f:
    print(f.read())
