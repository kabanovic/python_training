from model.contact import Contact
from fixture.group import Group

from fixture.orm import ORMFixture
import random


def test_add_contact_to_group(app, db):
    if app.contact.count_cont() == 0:
        app.contact.add(Contact("Vasya", "Vas", "Vasilev"))
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len(app.group.get_group_list()) == 0:
        app.group.create(Group("gr1", "hd1", "foo1"))
    group_list = app.group.get_group_list()
    id = group_list[0].id
    contacts_not_in_gr = db.get_contacts_not_in_group(Group(id=id))
    if len(contacts_not_in_gr) == 0:
        app.contact.add(Contact("Vasya2", "Vas2", "Vasilev2"))
        contacts_not_in_gr = db.get_contacts_not_in_group(Group(id=id))
    contact = random.choice(contacts_not_in_gr)
    app.contact.add_some_cont_to_group(contact.id)
    new_contacts_not_in_gr = db.get_contacts_not_in_group(Group(id=id))
    assert len(contacts_not_in_gr) - 1 == len(new_contacts_not_in_gr)