# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.add(Contact("Name3", "Middle3", "Surname3", "89991234567"))
    app.session.logout()

