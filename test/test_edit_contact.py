from model.contact import Contact


def test_edit_first_cont(app):
    if app.contact.count_cont() == 0:
        app.contact.add(Contact("Vasya", "Vas", "Vasilev", "89999999999"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_cont(Contact(telephone="89991111111"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)