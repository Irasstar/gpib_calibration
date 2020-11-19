class Device:
    def __init__(self):
        self.GPIB_settings = ''
        self.ID = ''

    def gpib_connect(self):
        pass

    def gpib_disconnect(self):
        pass

    def __gpib_write(self):
        pass

    def __gpib_read(self):
        pass

    def send_command(self):
        pass

    def receive_data(self):
        pass

    def __del__(self):
        pass
