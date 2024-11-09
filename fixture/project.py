from selenium.webdriver.common.by import By
from model.project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def goto_manage_project_page(self):
        wd = self.app.wd
        if not len(wd.find_elements(By.XPATH,"//input[@value='Create New Project']")) > 0:
            wd.find_element(By.XPATH,"//a[text()='Manage']").click()
            wd.find_element(By.XPATH,"//a[text()='Manage Projects']").click()

    def create_new_project(self, project):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//input[@value='Create New Project']").click()
        wd.find_element(By.XPATH, "//input[@name='name']").send_keys(project.name)
        wd.find_element(By.XPATH,"//input[@value='Add Project']").click()

    def get_project_list(self):
        wd = self.app.wd
        self.goto_manage_project_page()
        project_list=[]
        for each_element in wd.find_elements(By.XPATH, "//table[@class='width100']//tr[@class='row-1' or @class='row-2']"):
                name = each_element.find_element(By.XPATH, "td/a").text
                status = each_element.find_element(By.XPATH, "td[2]").text
                enabled = each_element.find_element(By.XPATH, "td[3]").text
                view_status = each_element.find_element(By.XPATH, "td[4]").text
                project_list.append(Project(name=name, status=status,enabled=enabled, view_status=view_status))
        return project_list

    def delete_project(self, project_to_delete):
        wd = self.app.wd
        self.goto_manage_project_page()
        wd.find_element(By.XPATH,"//a[text()='%s']" % project_to_delete).click()
        wd.find_element(By.XPATH,"//input[@value='Delete Project']").click()
        wd.find_element(By.XPATH,"//input[@value='Delete Project']").click()


