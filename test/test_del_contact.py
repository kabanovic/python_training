
from model.contact import Contact


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.delete_first_cont()
    app.session.logout()