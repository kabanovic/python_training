from model.contact import Contact
from random import randrange


def test_edit_some_cont(app, db, check_ui):
    if app.contact.count_cont() == 0:
        app.contact.add(Contact("Vasya", "Vas", "Vasilev"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    ct = old_contacts[index]
    contact = Contact(firstname="Петька", lastname="Петков")
    contact.id = ct.id
    app.contact.edit_some_cont_by_id(ct.id, contact)
    assert len(old_contacts) == app.contact.count_cont()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)