from pages.filtros_page import PaginaFiltros


def test_filtrar_tabela_por_nome_de_aluno(driver):
    pagina_filtros = PaginaFiltros(driver)

    pagina_filtros.abrir()

    texto_primeira_linha = pagina_filtros.obter_texto_primeira_linha()
    nome_aluno = texto_primeira_linha.split()[0]

    pagina_filtros.pesquisar(nome_aluno)

    assert pagina_filtros.todas_linhas_contem(nome_aluno)


def test_limpar_filtro_da_tabela(driver):
    pagina_filtros = PaginaFiltros(driver)

    pagina_filtros.abrir()

    texto_primeira_linha = pagina_filtros.obter_texto_primeira_linha()
    nome_aluno = texto_primeira_linha.split()[0]

    pagina_filtros.pesquisar(nome_aluno)
    pagina_filtros.limpar_pesquisa()

    assert len(pagina_filtros.obter_linhas()) > 0