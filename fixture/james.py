from telnetlib import Telnet

class JamesHelper:

    def __init__(self, app):
        self.app = app

    def ensure_user_exists(self, usermane, password):
        james_config = self.app.config['james']
        session = JamesHelper.Session(james_config["host"],
                                      james_config["port"],
                                      james_config["username"],
                                      james_config["password"])
        if session.is_user_registred(usermane):
            session.reset_password(usermane, password)
        else:
            session.create_user(usermane, password)
        session.quite()

    class Session:

        def __init__(self, host, port, username, password):
            self.telnet = Telnet(host, port, timeout=10)
            self.read_until("Login id:")
            self.write(username + "\n")
            self.read_until("Password:")
            self.write(password + "\n")
            self.read_until("Welcome {}. HELP for a list of commands".format(username))

        def read_until(self, text):
            self.telnet.read_until(text.encode('ascii'), 10)

        def write(self, text):
            self.telnet.write(text.encode("ascii"))

        def is_user_registred(self, username):
            self.write("verify {}\n".format(username))
            res = self.telnet.expect([b"exists", b"does not exist"])
            return res[0] == 0

        def create_user(self, username, password):
            self.write("adduser {} {}\n".format(username, password))
            self.read_until("User {} added".format(username))

        def reset_password(self, username, password):
            self.write("setpassword {} {}\n".format(username, password))
            self.read_until("Pasword for {} reset".format(username))

        def quite(self):
            self.write("quite\n")
