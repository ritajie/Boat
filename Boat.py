from flask import Flask, render_template, request, url_for, session, redirect
import config
from exts import db
from models import Rule, Manning, Worker

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def bar():
    # return render_template("test-vue.html")
    return render_template("bar.html")


@app.route('/rule/', methods=['GET', 'POST'])
def rule():
    if request.method == "GET":
        content = {
            "rules": Rule.query.all()
        }
        return render_template("rule.html", **content)
    else:
        shihedunwei = request.form.get("shihedunwei")
        chuanzhang = request.form.get("chuanzhang")
        dafu = request.form.get("dafu")
        erfu = request.form.get("erfu")
        sanfu = request.form.get("sanfu")
        zhibanshuishou = request.form.get("zhibanshuishou")
        jiushengrenyuan = request.form.get("jiushengrenyuan")

        newrule = Rule(rule_content=shihedunwei, chuanzhang=chuanzhang, dafu=dafu, erfu=erfu, sanfu=sanfu,
                       zhibanshuishou=zhibanshuishou, jiushengrenyuan=jiushengrenyuan)
        db.session.add(newrule)
        db.session.commit()

        return redirect("rule")


@app.route('/ship/', methods=['GET', 'POST'])
def ship():
    if request.method == "GET":
        content = {
            "rules": Rule.query.all(),
            "ships": Ship.query.all()
        }
        return render_template("ship.html", **content)
    else:
        rule_id = request.form.get("rule")
        shipname = request.form.get("shipname")
        newship = Ship(shipname=shipname, rule_id=rule_id)
        db.session.add(newship)
        db.session.commit()

        return redirect("ship")


@app.route('/worker/', methods=['GET', "POST"])
def worker():
    if request.method == "GET":
        content = {
            "ships": Ship.query.all()
        }
        return render_template("worker.html", **content)
    else:
        all = request.form
        workerid = request.form.get("workerid")
        password = request.form.get("password")
        # 签到按钮
        if "workin" in request.form:
            theworker = Worker.query.filter(Worker.workerid == workerid, Worker.password == password).first()
            if not theworker:
                return "密码错误"
            elif theworker.working:
                return "%s已经签到" % theworker.name
            else:
                shipid = request.form.get("ship")
                job = request.form.get("job")

                theworker.job = job
                theworker.ship_id = shipid
                theworker.working = True

                # 将船的数据更新
                theship = Ship.query.filter(Ship.id == shipid).first()
                if job == "chuanzhang":
                    theship.chuanzhang += 1
                elif job == "dafu":
                    theship.dafu += 1
                elif job == "erfu":
                    theship.erfu += 1
                elif job == "sanfu":
                    theship.sanfu += 1
                elif job == "zhibanshuishou":
                    theship.zhibanshuishou += 1
                elif job == "jiushengrenyuan":
                    theship.jiushengrenyuan += 1

                db.session.commit()
                return redirect("ship")

        # 签退按钮
        elif "workout" in request.form:
            theworker = Worker.query.filter(Worker.workerid == workerid, Worker.password == password).first()
            if not theworker:
                return "密码错误"
            elif not theworker.working:
                return "%s没有签到 因此不能签退" % theworker.name
            else:
                shipid = theworker.ship_id
                job = theworker.job

                theworker.working = False

                # 将船的数据更新
                theship = Ship.query.filter(Ship.id == shipid).first()
                if job == "chuanzhang":
                    theship.chuanzhang -= 1
                elif job == "dafu":
                    theship.dafu -= 1
                elif job == "erfu":
                    theship.erfu -= 1
                elif job == "sanfu":
                    theship.sanfu -= 1
                elif job == "zhibanshuishou":
                    theship.zhibanshuishou -= 1
                elif job == "jiushengrenyuan":
                    theship.jiushengrenyuan -= 1

                db.session.commit()
                return redirect("ship")

        # 注册按钮
        elif "login" in request.form:
            return redirect("worker_login")
        else:
            return "error"


@app.route("/worker_login/", methods=["GET", "POST"])
def worker_login():
    if request.method == "GET":
        return render_template("worker_login.html")
    else:
        name = request.form.get("name")
        workerid = request.form.get("workerid")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if not Worker.query.filter(Worker.workerid==workerid):
            return "工号已经被注册"
        if password1 != password2:
            return "两次输入的密码不一致"

        newworker = Worker(name=name, workerid=workerid, password=password1)
        db.session.add(newworker)
        db.session.commit()

        return redirect("worker")





if __name__ == '__main__':
    app.run()
