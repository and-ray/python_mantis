from model.project import Project
import random

def test_delete_projects(app):
    app.session.login("administrator", "root")
    if app.project.get_project_list() == 0:
        app.project.create(Project(name="Big-Bang Project", status="development", enabled="X",  view_status="public"))
    app.project.goto_manage_project_page()
    old_project_list = app.project.get_project_list()
    project_to_delete = random.choice(old_project_list)
    app.project.delete_project(project_to_delete)
    old_project_list.remove(project_to_delete)
    new_project_list = app.project.get_project_list()
    assert sorted(old_project_list, key=lambda p:p.name) == sorted(new_project_list, key=lambda q:q.name)

