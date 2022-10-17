from model.group import Group

def test_group_change(app):
    app.session.login(login="admin", password="secret")
    app.group.first_group_change(Group(name="HW7_", header="HW7", footer="test"))
    app.session.logout()