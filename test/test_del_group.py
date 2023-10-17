from model.group import Group


def test_del_first_group(app):
    if app.group.count_group() == 0:
        app.group.create(Group("rty", "fgh", "vbn"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups) - 1 == app.group.count_group()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups