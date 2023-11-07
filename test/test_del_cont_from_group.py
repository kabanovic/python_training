from model.contact import Contact
from fixture.group import Group
from fixture.orm import ORMFixture
import random

def test_del_contact_from_group(app, db):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    group_list = app.group.get_group_list()
    id = group_list[0].id
    contacts_in_gr = db.get_contacts_in_group(Group(id=id))
    if len(contacts_in_gr) == 0:
        app.contact.add(Contact("Vasya3", "Vas3", "Vasilev3"))
        contacts_not_in_gr = db.get_contacts_not_in_group(Group(id=id))
        app.contact.add_some_cont_to_group(contacts_not_in_gr[0].id)
    new_contacts_in_gr = db.get_contacts_in_group(Group(id=id))
    app.contact.select_group_for_del_cont(id)
    app.contact.del_some_cont_from_group(new_contacts_in_gr[0].id)
    contacts_after_delete = db.get_contacts_in_group(Group(id=id))
    assert len(new_contacts_in_gr) - 1 == len(contacts_after_delete)


