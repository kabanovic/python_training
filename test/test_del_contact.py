from model.contact import Contact
from model.contact import Contact


def test_add_contact(app):
    if app.contact.count_cont() == 0:
        app.contact.add(Contact("Vasya", "Vas", "Vasilev", "89999999999"))
    app.contact.delete_first_cont()
