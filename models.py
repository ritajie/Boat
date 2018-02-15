from exts import db


class Rule(db.Model):
    __tablename__ = "rule"
    # 规则id
    rule_id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)

    # 规则介绍
    rule_content = db.Column(db.Text)
    # 船长 大副 二副 三副 值班水手 救生人员
    rule_captain = db.Column(db.INTEGER, default=0)
    rule_officer1 = db.Column(db.INTEGER, default=0)
    rule_officer2 = db.Column(db.INTEGER, default=0)
    rule_officer3 = db.Column(db.INTEGER, default=0)
    rule_sailor = db.Column(db.INTEGER, default=0)
    rule_lifeguard = db.Column(db.INTEGER, default=0)

# 配员
class Manning(db.Model):
    __tablename__ = "manning"
    manning_id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    # 船长 大副 二副 三副 值班水手 救生人员
    manning_captain = db.Column(db.INTEGER, default=0)
    manning_officer1 = db.Column(db.INTEGER, default=0)
    manning_officer2 = db.Column(db.INTEGER, default=0)
    manning_officer3 = db.Column(db.INTEGER, default=0)
    manning_sailor = db.Column(db.INTEGER, default=0)
    manning_lifeguard = db.Column(db.INTEGER, default=0)
    manning_shipid = db.Column(db.String(10))


class Worker(db.Model):
    __tablename__ = "worker"
    worker_id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    # 工号 密码 姓名 职位
    worker_jobnumber = db.Column(db.String(20), nullable=False)
    worker_password = db.Column(db.String(20), nullable=False)
    worker_name = db.Column(db.String(20), nullable=False)
    worder_position = db.Column(db.String(20), nullable=True)
    worker_isworking = db.Column(db.BOOLEAN, default=False)
    # worker_shipid = db.Column(db.INTEGER, db.ForeignKey("ship.id"), default=1)
    # 反向引用
    # ship = db.relationship("Ship", backref=db.backref("workers"))
