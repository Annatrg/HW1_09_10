from model.group import Group
def test_group_change(app):
    app.group.first_group_change(Group(name="HW7_", header="HW7", footer="test"))


def test_group_change_name(app):
    app.group.first_group_change(Group(name="New group"))


def test_group_change_header(app):
    app.group.first_group_change(Group(header="New header"))
