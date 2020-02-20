from app import app as mapp
from flask import render_template
from app.engine.host_controller import HostController

print(":fdfsfgsdfsdfdse")


@mapp.route('/')
@mapp.route('/index')
def index():
    lis = HostController().hosts
    for li in lis:
        li.wake_up()
    return render_template("base.html", ht=1)
