from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaginaFiltros:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://practice.expandtesting.com/dynamic-pagination-table"
        self.wait = WebDriverWait(driver, 10)

        self.campo_pesquisa = (By.CSS_SELECTOR, "input[type='search']")
        self.linhas_tabela = (By.CSS_SELECTOR, "table tbody tr")
        self.tabela = (By.CSS_SELECTOR, "table")

    def abrir(self):
        self.driver.get(self.url)

    def aguardar_tabela(self):
        self.wait.until(
            EC.visibility_of_element_located(self.tabela)
        )

    def obter_linhas(self):
        self.aguardar_tabela()
        return self.wait.until(
            EC.presence_of_all_elements_located(self.linhas_tabela)
        )

    def obter_texto_primeira_linha(self):
        linhas = self.obter_linhas()
        return linhas[0].text

    def pesquisar(self, texto):
        campo = self.wait.until(
            EC.visibility_of_element_located(self.campo_pesquisa)
        )
        campo.clear()
        campo.send_keys(texto)

        self.wait.until(
            lambda driver: texto.lower() in self.obter_texto_tabela().lower()
        )

    def limpar_pesquisa(self):
        campo = self.wait.until(
            EC.visibility_of_element_located(self.campo_pesquisa)
        )
        campo.clear()

    def obter_texto_tabela(self):
        tabela = self.wait.until(
            EC.visibility_of_element_located(self.tabela)
        )
        return tabela.text

    def todas_linhas_contem(self, texto):
        linhas = self.obter_linhas()

        for linha in linhas:
            if texto.lower() not in linha.text.lower():
                return False

        return True