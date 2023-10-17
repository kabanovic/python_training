from model.group import Group


def test_edit_first_group(app):
    if app.group.count_group() == 0:
        app.group.create(Group("rty", "fgh", "vbn"))
    old_groups = app.group.get_group_list()
    group = Group("999", "888", "777")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    assert len(old_groups) == app.group.count_group()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_first_group_header(app):
 #   if app.group.count_group() == 0:
  #      app.group.create(Group("fdsfds", "sdfdsf", "sadad"))
   # old_groups = app.group.get_group_list()
    #app.group.edit_first_group(Group(header="666"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
