from model.contact import Contact
from random import randrange


def test_edit_some_cont(app):
    if app.contact.count_cont() == 0:
        app.contact.add(Contact("Vasya", "Vas", "Vasilev"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firsname="Петька", lastname="Петков")
    contact.id = old_contacts[index].id
    app.contact.edit_some_cont(index, contact)
    assert len(old_contacts) == app.contact.count_cont()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)