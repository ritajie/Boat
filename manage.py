from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from Boat import app
from exts import db
from models import Rule, Manning, Worker

manager = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本的命令到manage中 Command会去读取导入的User模型
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
