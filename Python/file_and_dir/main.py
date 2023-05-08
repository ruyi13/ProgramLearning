import os
import shutil
import random


workdir = os.getcwd()
patched_dir = os.path.join(workdir,"patched")
fuzz_dir =   os.path.join(workdir,"fuzz")
#print(patched_dir)
files = os.listdir(patched_dir)
if files :
    if os.path.exists(fuzz_dir):
        shutil.rmtree(fuzz_dir)#os.rmdir(fuzz_dir) # 删除当前测试的结果
    os.mkdir(fuzz_dir) # 创建一个新的目录
    # 构造源文件和目的文件的完整路径
    selected_file = random.choice(files)
    src_path = os.path.join(patched_dir, selected_file)
    dest_path = os.path.join(fuzz_dir, selected_file)
    # 从patched中随便选择一个文件

    shutil.move(src_path, dest_path)


else: # 目录空，测试结束
    pass













