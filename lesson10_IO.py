from io import StringIO,BytesIO

f = open("file/hello.txt","r")
# print(f.read())
f.close()


f = StringIO()
f.write('hello')
print(f.read())