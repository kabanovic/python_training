from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group("rty", "fgh", "vbn"))
    app.group.edit_first_group(Group("999", "888", "777"))


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group("fdsfds", "sdfdsf", "sadad"))
    app.group.edit_first_group(Group(header="666"))

