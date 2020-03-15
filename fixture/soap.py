from suds.client import Client
from suds import WebFault

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault as err:
            print("%s" % err)
            return False

    def get_projects_list(self):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        username = self.app.config['webadmin']["username"]
        password = self.app.config['webadmin']["password"]
        try:
            dict = client.service.mc_projects_get_user_accessible(username, password)
            return dict
        except WebFault:
            return None


