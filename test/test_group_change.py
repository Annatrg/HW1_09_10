from random import randrange
from model.group import Group

def test_group_change(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_del"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="HW7_", header="HW7", footer="test")
    group.id = old_groups[index].id
    app.group.group_change_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_group_change_name(app):
 #   old_groups = app.group.get_group_list()
  #  if app.group.count() == 0:
   #     app.group.create(Group(name="test_del"))
    #group = Group(name="New group")
   # app.group.first_group_change(group)
#    group.id = old_groups[0].id
 #   new_groups = app.group.get_group_list()
  #  assert len(old_groups) == len(new_groups)
   # old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_group_change_header(app):
 #   old_groups = app.group.get_group_list()
  #  if app.group.count() == 0:
   #     app.group.create(Group(name="test_del"))
    #group = Group(header="New header")
   # app.group.first_group_change(group)
  #  group.id = old_groups[0].id
 #   new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
 #   old_groups[0] = group
  #  assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
