from model.group import Group
import random
from random import randrange

def test_edit_some_group(app, db):
    if app.group.count_group() == 0:
        app.group.create(Group("rty", "fgh", "vbn"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    #index = randrange(len(old_groups))
    group = Group("545", "888", "777")
    group.id = old_groups[index].id
    app.group.edit_some_group(index, group)
    assert len(old_groups) == app.group.count_group()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_first_group_header(app):
 #   if app.group.count_group() == 0:
  #      app.group.create(Group("fdsfds", "sdfdsf", "sadad"))
   # old_groups = app.group.get_group_list()
    #app.group.edit_first_group(Group(header="666"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
