from suds.client import Client
from suds import WebFault

class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url +"api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        client = Client(self.app.base_url +"/api/soap/mantisconnect.php?wsdl")
        try:
            list_of_projects = client.service.mc_projects_get_user_accessible(username, password)
            list_of_project_names = list(map(lambda x: x.__getattribute__("name"), list_of_projects)) #map(lambda x: x.decode('utf-8'),msglines)
            return list_of_project_names
        except WebFault:
            return False