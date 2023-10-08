from model.group import Group


def test_del_first_group(app):
    if app.group.count_group() == 0:
        app.group.create(Group("rty", "fgh", "vbn"))
    app.group.delete_first_group()
