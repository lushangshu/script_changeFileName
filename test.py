import os
# 列出当前目录下所有的文件
files = os.listdir(".")
print(files)
count = 0
for filename in files:

    portion = os.path.splitext(filename)
    # 如果后缀是.txt
    if portion[1] == ".txt":
        # 重新组合文件名和后缀名
        newname = str(count) + ".mp4"
        count+=1
        os.rename(filename,newname)
