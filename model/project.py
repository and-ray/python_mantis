class Project:
    def __init__(self, name=None, status=None, enabled=None, view_status = None):
        self.name = name
        self.status = status
        self.enabled = enabled
        self.view_status = view_status

    def __repr__(self):
        return "%s, %s, %s, %s" %(self.name, self.status,  self.enabled, self.view_status)

    def __eq__(self, other):
        return self.name == other.name
