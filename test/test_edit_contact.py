from model.contact import Contact


def test_edit_first_cont(app):
    if app.contact.count_cont() == 0:
        app.contact.add(Contact("Vasya", "Vas", "Vasilev", "89999999999"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(telephone="89991111111")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname
    contact.firstname = old_contacts[0].firstname
    app.contact.edit_first_cont(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)