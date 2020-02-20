from wakeonlan import send_magic_packet


class Communicator:
    def __init__(self):
        pass

    @staticmethod
    def wake_up(mac):
        if mac:
            send_magic_packet(mac)
