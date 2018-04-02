import os

# 获取config文件所在文件夹位置
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))  # 获取项目根目录
print(PROJECT_ROOT)

data_file_path = os.path.join(PROJECT_ROOT, "web_base_model/test1.html")  # 文件路径
print(data_file_path)
