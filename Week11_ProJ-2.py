import path
import os

fullfile = path.basepath + "/" + path.subpath
fullpath = path.basepath + "/" + path.subpath + "/" + path.subfile

if not os.path.exists(fullfile):
    os.makedirs(fullfile)

score = {}

f = open(fullpath, 'r')

while True:
    line = f.readline()
    if not line:
        break
    data = line.strip().split(',')

    score['name'] = data[0]
    score['kor']  = int(data[1])
    score['eng']  = int(data[2])
    score['math'] = int(data[3])

    summary = score['kor'] + score['eng'] + score['math']
    avr = summary / 3
    print(f"{score['name']},{score['kor']},{score['eng']},{score['math']} 평균 = {avr}")
f.close()


