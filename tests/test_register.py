from pages.register_page import PaginaCadastro
from random import randint

SENHA_VALIDA = "SenhaTeste123!"


def gerar_username():
    numero = randint(100000, 999999)
    return "joaoteste" + str(numero)


def test_cadastro_com_sucesso(driver):
    pagina_cadastro = PaginaCadastro(driver)

    username = gerar_username()

    pagina_cadastro.abrir()
    pagina_cadastro.preencher_formulario(
        username,
        SENHA_VALIDA,
        SENHA_VALIDA
    )
    pagina_cadastro.clicar_register()

    assert pagina_cadastro.esta_na_pagina_de_login()
    assert "Successfully registered" in pagina_cadastro.obter_mensagem()


def test_cadastro_sem_username(driver):
    pagina_cadastro = PaginaCadastro(driver)

    pagina_cadastro.abrir()
    pagina_cadastro.preencher_password(SENHA_VALIDA)
    pagina_cadastro.preencher_confirm_password(SENHA_VALIDA)
    pagina_cadastro.clicar_register()

    assert pagina_cadastro.esta_na_pagina_de_register()
    assert "All fields are required" in pagina_cadastro.obter_mensagem()


def test_cadastro_sem_password(driver):
    pagina_cadastro = PaginaCadastro(driver)

    username = gerar_username()

    pagina_cadastro.abrir()
    pagina_cadastro.preencher_username(username)
    pagina_cadastro.preencher_confirm_password(SENHA_VALIDA)
    pagina_cadastro.clicar_register()

    assert pagina_cadastro.esta_na_pagina_de_register()
    assert "All fields are required" in pagina_cadastro.obter_mensagem()


def test_cadastro_com_senhas_diferentes(driver):
    pagina_cadastro = PaginaCadastro(driver)

    username = gerar_username()

    pagina_cadastro.abrir()
    pagina_cadastro.preencher_formulario(
        username,
        "SenhaTeste123!",
        "OutraSenha123!"
    )
    pagina_cadastro.clicar_register()

    assert pagina_cadastro.esta_na_pagina_de_register()
    assert "Passwords do not match" in pagina_cadastro.obter_mensagem()