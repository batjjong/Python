import path
import os

fullfile = path.basepath + "/" + path.subpath
fullpath = path.basepath + "/" + path.subpath + "/" + path.subfile

if not os.path.exists(fullfile):
    os.makedirs(fullfile)

f = open(fullpath, 'w')

while True:
    name = input("이름:")
    if name == '':
        break
    kor = int(input("국어:"))
    eng = int(input("영어:"))
    math = int(input("수학:"))

    f.write(f"{name},{kor},{eng},{math}\n")

f.close()
