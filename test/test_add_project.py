from datetime import datetime

from model.project import Project

def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.goto_manage_project_page()
    old_project_list = app.project.get_project_list()
    new_project = Project(name="Big-Bang Project"+str(datetime.now().time()), status="development", enabled="X",  view_status="public")
    app.project.create_new_project(new_project)
    old_project_list.append(new_project)
    new_project_list = app.project.get_project_list()
    assert sorted(old_project_list, key=lambda p:p.name) == sorted(new_project_list, key=lambda q:q.name)







