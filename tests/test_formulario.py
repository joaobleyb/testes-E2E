from pages.formulario_page import PaginaFormulario


def test_preencher_formulario_com_sucesso(driver):
    pagina_formulario = PaginaFormulario(driver)

    pagina_formulario.abrir()
    pagina_formulario.preencher_formulario(
        "Joao Teste",
        "012-3456789",
        "2026-06-04",
        "cash on delivery"
    )
    pagina_formulario.clicar_register()

    texto_pagina = pagina_formulario.obter_texto_pagina()

    assert pagina_formulario.esta_na_pagina_de_confirmacao()
    assert "Thank you for validating your ticket" in texto_pagina


def test_formulario_vazio_exibe_mensagens_de_validacao(driver):
    pagina_formulario = PaginaFormulario(driver)

    pagina_formulario.abrir()
    pagina_formulario.limpar_formulario()
    pagina_formulario.clicar_register()

    texto_pagina = pagina_formulario.obter_texto_pagina()

    assert "Please enter your Contact name." in texto_pagina
    assert "Please provide your Contact number." in texto_pagina
    assert "Please provide valid Date." in texto_pagina
    assert "Please select the Paymeny Method." in texto_pagina