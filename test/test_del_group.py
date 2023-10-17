from model.group import Group
from random import randrange


def test_del_some_group(app):
    if app.group.count_group() == 0:
        app.group.create(Group("rty", "fgh", "vbn"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_some_group(index)
    assert len(old_groups) - 1 == app.group.count_group()
    new_groups = app.group.get_group_list()
    old_groups[index:index + 1] = []
    assert old_groups == new_groups