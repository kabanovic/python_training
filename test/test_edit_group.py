from model.group import Group


def test_edit_first_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group("999", "", ""))
    app.session.logout()


def test_edit_name_group(app):
    app.session.login("admin", "secret")
    app.group.edit_name_group(name="888")
    app.session.logout()