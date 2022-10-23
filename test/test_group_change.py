from model.group import Group


def test_group_change(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_del"))
    app.group.first_group_change(Group(name="HW7_", header="HW7", footer="test"))


def test_group_change_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_del"))
    app.group.first_group_change(Group(name="New group"))



def test_group_change_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_del"))
    app.group.first_group_change(Group(header="New header"))

