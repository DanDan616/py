import sys
import subprocess
import pdfkit
import os

def ipynb_to_pdf(file_name):
    inputfile = file_name

    command = 'ipython nbconvert --to html ' + inputfile

    subprocess.call(command, shell=True)
    
def get_file_name(path,ext):
    """
    获取指定路径下，指定格式的所有文件名
    @param path: 路径，如：上一层 '../'
    @param ext: 指定后缀
    """
    listallfile = os.listdir(path)
    listfile = []

    # 获取指定格式的文件
    for i in listallfile:
        if ext in i:
            listfile.append(i)
    return listfile[:]


files_name = get_file_name('./', '.ipynb')
for file in files_name:
    print(file)
    ipynb_to_pdf(file)
