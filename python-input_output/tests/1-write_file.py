>>> write_file = __import__('1-write_file').write_file

>>> write_file("test_write.txt", "Hello School")
12
>>> with open("test_write.txt", "r") as f:
...     print(f.read())
Hello School
