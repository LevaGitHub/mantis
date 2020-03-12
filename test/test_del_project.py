from model.project import Project
from fixture.general import generate_sequence
from random import choice


def checking_preconditions_before_delete(app):
    if len(app.project.get_project_list()) == 0:
        app.person.create_project(Project(name=generate_sequence(10),
                                          status="development",
                                          enabled=True,
                                          view_status="public",
                                          description=generate_sequence(30)))


def test_del_project(app):
    checking_preconditions_before_delete(app)
    old_projects = app.project.get_project_list()
    del_project = choice(old_projects)
    app.project.delete_project(del_project)
    new_projects = app.project.get_project_list()
    old_projects.remove(del_project)
    assert sorted(old_projects,
                  key=Project.name_and_description) == sorted(new_projects, key=Project.name_and_description)
