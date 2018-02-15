import os

DEBUG = True
# session的安全随机字符串
SECRET_KEY = os.urandom(24)

# 数据路相关配置信息
SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:root@127.0.0.1:3306/Boat?charset=utf8"

# 拒绝跟踪修改？视频:注册功能完成06：30
SQLALCHEMY_TRACK_MODIFICATIONS = False