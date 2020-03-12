from sys import maxsize

class Project:

    def __init__(self, project_id=None, name=None, status=None, enabled=None, inheritment=None, view_status=None,
                 description=None):
        self.project_id = project_id
        self.name = name
        self.status = status   # development\release\stable\obsolete
        self.enabled = enabled   # True\False
        self.inheritment = inheritment   # True\False
        self.view_status = view_status   # public\private
        self.description = description

    def __eq__(self, other):
        return ((self.project_id is None or other.project_id is None or self.project_id == other.project_id)
                and self.name == other.name
                and self.description == other.description)

    def name_and_description(self):
        return "{}{}".format(self.name, self.description)