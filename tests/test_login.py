from pages.login_page import PaginaLogin


USERNAME_VALIDO = "practice"
SENHA_VALIDA = "SuperSecretPassword!"


def test_login_com_sucesso(driver):
    pagina_login = PaginaLogin(driver)

    pagina_login.abrir()
    pagina_login.fazer_login(USERNAME_VALIDO, SENHA_VALIDA)

    assert pagina_login.esta_na_pagina_segura()
    assert "You logged into a secure area" in pagina_login.obter_mensagem()
    assert pagina_login.botao_logout_visivel()


def test_login_com_username_invalido(driver):
    pagina_login = PaginaLogin(driver)

    pagina_login.abrir()
    pagina_login.fazer_login("usuarioerrado", SENHA_VALIDA)

    assert pagina_login.esta_na_pagina_de_login()
    assert "Your username is invalid!" in pagina_login.obter_mensagem()


def test_login_com_senha_invalida(driver):
    pagina_login = PaginaLogin(driver)

    pagina_login.abrir()
    pagina_login.fazer_login(USERNAME_VALIDO, "senhaerrada")

    assert pagina_login.esta_na_pagina_de_login()
    assert "Your password is invalid!" in pagina_login.obter_mensagem()


def test_logout_com_sucesso(driver):
    pagina_login = PaginaLogin(driver)

    pagina_login.abrir()
    pagina_login.fazer_login(USERNAME_VALIDO, SENHA_VALIDA)
    pagina_login.clicar_logout()

    assert pagina_login.esta_na_pagina_de_login()
    assert "You logged out of the secure area" in pagina_login.obter_mensagem()