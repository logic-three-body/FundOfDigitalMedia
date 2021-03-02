import os
# https://www.cnblogs.com/yoyoketang/p/9083932.html
VedeoPath="D:/EVERTHING/test/hello.py"
#f=os.popen(r"python D:/EVERTHING/test/hello.py","r")
f=os.popen("python D:/EVERTHING/test/hello.py","r")
d=f.read()
print(d)
print(f)


