from app import app as mapp
from flask import render_template
from app.engine.host_controller import HostController


@mapp.route('/')
@mapp.route('/index')
def index():

    return render_template("base.html", ht=1)


@mapp.route('/api/prussia/turn_on')
def api_turn_on():
    lis = HostController().hosts
    for li in lis:
        li.wake_up()
    print("TURNING ON")
    return render_template("base.html", ht=1)


@mapp.route('/api/prussia/turn_off')
def api_turn_off():
    print("TURNING ON")
    return render_template("base.html", ht=1)
