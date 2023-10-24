# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from data.group import constant as testdata


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
   old_groups = app.group.get_group_list()
   app.group.create(group)
   assert len(old_groups) + 1 == app.group.count_group()
   new_groups = app.group.get_group_list()
   old_groups.append(group)
   assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_add_empty_group(app):
#    old_groups = app.group.get_group_list()
#    group = Group("", "", "")
#    app.group.create(group)
#    assert len(old_groups) + 1 == app.group.count_group()
#    new_groups = app.group.get_group_list()
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


