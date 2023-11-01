from model.group import Group
import random
from random import randrange

def test_edit_some_group(app, db, check_ui):
    if app.group.count_group() == 0:
        app.group.create(Group("rty", "fgh", "vbn"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    gp = old_groups[index]
    group = Group("66", "66", "66")
    group.id = gp.id
    app.group.edit_some_group_by_id(gp.id, group)
    assert len(old_groups) == app.group.count_group()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_edit_first_group_header(app):
 #   if app.group.count_group() == 0:
  #      app.group.create(Group("fdsfds", "sdfdsf", "sadad"))
   # old_groups = app.group.get_group_list()
    #app.group.edit_first_group(Group(header="666"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
