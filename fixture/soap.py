from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("{}api/soap/mantisconnect.php?wsdl".format(self.app.config['web']['baseUrl']))
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault as err:
            print("%s" % err)
            return False

    def get_projects_list(self):
        client = Client("{}api/soap/mantisconnect.php?wsdl".format(self.app.config['web']['baseUrl']))
        username = self.app.config['webadmin']["username"]
        password = self.app.config['webadmin']["password"]
        try:
            dict = client.service.mc_projects_get_user_accessible(username, password)
            return dict
        except WebFault:
            return None
