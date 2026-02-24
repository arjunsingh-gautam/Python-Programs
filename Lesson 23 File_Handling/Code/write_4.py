# Writing in binary mode:
with open(r"Lesson 23 File_Handling\Code\bytes.bin","wb") as f:
    f.write(bytes(range(256)))