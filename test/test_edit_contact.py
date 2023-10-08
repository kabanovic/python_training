from model.contact import Contact


def test_edit_first_cont(app):
    app.contact.edit_first_cont(Contact("Имя", "Отчество", "Фамилия", "89991111111"))
