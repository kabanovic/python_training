from model.group import Group


def test_del_first_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group("999", "", ""))
    app.session.logout()