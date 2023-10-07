from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group("999", "888", "777"))


def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header="666"))

