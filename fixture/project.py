from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create_project(self, project):
        wd = self.app.wd
        self.open_manage_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.input_project_data(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.return_to_all_project_page()

    def delete_project(self, project):
        wd = self.app.wd
        self.open_manage_page()
        wd.find_element_by_partial_link_text("{}".format(project.name)).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def open_manage_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_overview_page.php") and len(wd.find_elements_by_name("Manage")) > 0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def input_project_data(self, project):
        wd = self.app.wd
        self.app.set_textbox_value("name", project.name)
        self.app.select_combobox_value("status", project.status)
        if project.inheritment:
            wd.find_element_by_name("inherit_global").click()
        self.app.select_combobox_value("view_state", project.view_status)
        self.app.set_textbox_value("description", project.description)

    def return_to_all_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Proceed").click()

    def get_project_list(self):
        print("Выполняется получение списка проектов из интерфейса")
        wd = self.app.wd
        self.open_manage_page()
        show_projects = []
        count_service_row = 2
        for i in range(len(wd.find_elements_by_xpath("/ html / body / table[3] / tbody / tr")) - count_service_row):
            index = i + count_service_row + 1
            row = wd.find_elements_by_xpath("/ html / body / table[3] / tbody / tr[{}]/td".format(index))
            name = row[0].text
            status = row[1].text
            enabled = row[2].text
            view_status = row[3].text
            description = row[4].text
            show_projects.append(Project(project_id=index,
                                         name=name,
                                         status=status,
                                         enabled=(True if enabled == 'X' else False),
                                         view_status=view_status,
                                         description=description))
        return show_projects

