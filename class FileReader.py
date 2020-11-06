import nltk
import re
import os

class FileReader():
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        self.write('some_file.txt', 'some text')
        try:
            result = open(self.filename, 'r').read()
            return result
        except FileNotFoundError:
            return ""

    def write(self, file, message):
        file = open(file, 'w')
        file.write(message)

    def count(self):
        lines = 0
        data = self.read()
        data = re.sub(r'[^\w\s]', '', data)
        for line in open(self.filename, 'r'):
            lines += 1
        tokens = nltk.word_tokenize(data)

        setattr(FileReader, 'line_count', lines)
        setattr(FileReader, 'word_count', len(tokens))

    def __add__(self, other):
        obj = FileReader("result.txt")
        obj.write(obj.filename, open(self.filename, 'r').read() + open(other, 'r').read())
        return obj

    def __str__(self):
        return f"Path: {os.path.abspath(self.filename)}"

reader = FileReader('blok.txt')
text = reader.read()
print(text + '\n')
reader.count()
print("Line Count: ", str(reader.line_count))
print("Word Count: ", str(reader.word_count), '\n')
print(reader.__add__('some_file.txt'))
print(reader.__str__())