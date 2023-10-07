from model.group import Group


def test_edit_first_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group("999", "888", "777"))
    app.session.logout()

def test_edit_first_group_header(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group(header="666"))
    app.session.logout()
