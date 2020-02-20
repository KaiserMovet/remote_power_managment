from flask import render_template
import yaml
from app.engine.communicator import Communicator


class HostController:
    def __init__(self):
        self.hosts = self._load_hosts()

    @staticmethod
    def _load_hosts():
        with open(r'app/config.yaml') as file:
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            hosts_data = yaml.load(file, Loader=yaml.FullLoader)
        hosts = []
        for host_name, host_data in hosts_data.items():
            hosts.append(Host(host_name, host_data))
        return hosts


class Host:
    def __init__(self, name, dict_data):
        self.name = name
        self.ip = dict_data.get("ip")
        self.mac = dict_data.get("mac")

    def __html__(self):
        return render_template("card.html")

    def wake_up(self):
        Communicator.wake_up(self.mac)
