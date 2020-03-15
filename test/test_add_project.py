from model.project import Project
from fixture.general import generate_sequence


def test_add_project(app):
    old_projects = app.project.convert_to_project(app.soap.get_projects_list())
    pr = Project(name=generate_sequence(10),
                 status="development",
                 enabled=True,
                 view_status="public",
                 description=generate_sequence(30))
    app.project.create_project(pr)
    new_projects = app.project.convert_to_project(app.soap.get_projects_list())
    old_projects.append(pr)
    assert sorted(old_projects,
                  key=Project.name_and_description) == sorted(new_projects, key=Project.name_and_description)
