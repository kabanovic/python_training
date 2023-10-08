from model.contact import Contact


def test_edit_first_cont(app):
    if app.contact.count_cont() == 0:
        app.contact.add(Contact("Vasya", "Vas", "Vasilev", "89999999999"))
    app.contact.edit_first_cont(Contact("Имя", "Отчество", "Фамилия", "89991111111"))
