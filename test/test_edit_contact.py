from model.contact import Contact
from random import randrange

def test_edit_some_cont(app):
    if app.contact.count_cont() == 0:
        app.contact.add(Contact("Vasya", "Vas", "Vasilev", "89999999999"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(telephone="89991111112")
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    contact.firstname = old_contacts[index].firstname
    contact.telephone = old_contacts[index].telephone
    app.contact.edit_some_cont(index, contact)
    assert len(old_contacts) == app.contact.count_cont()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)