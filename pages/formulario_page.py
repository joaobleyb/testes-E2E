from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class PaginaFormulario:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://practice.expandtesting.com/form-validation"
        self.wait = WebDriverWait(driver, 10)

        self.campo_nome = (By.CSS_SELECTOR, "input[type='text']")
        self.campo_contato = (By.CSS_SELECTOR, "input[type='tel']")
        self.campo_data = (By.CSS_SELECTOR, "input[type='date']")
        self.select_pagamento = (By.TAG_NAME, "select")
        self.botao_register = (By.CSS_SELECTOR, "button[type='submit']")

    def abrir(self):
        self.driver.get(self.url)

    def preencher_nome(self, nome):
        campo = self.wait.until(
            EC.visibility_of_element_located(self.campo_nome)
        )
        campo.clear()
        campo.send_keys(nome)

    def preencher_contato(self, contato):
        campo = self.wait.until(
            EC.visibility_of_element_located(self.campo_contato)
        )
        campo.clear()
        campo.send_keys(contato)

    def preencher_data(self, data):
        campo = self.wait.until(
            EC.visibility_of_element_located(self.campo_data)
        )
        campo.clear()
        campo.send_keys(data)

    def selecionar_pagamento(self, pagamento):
        select = self.wait.until(
            EC.visibility_of_element_located(self.select_pagamento)
        )
        Select(select).select_by_visible_text(pagamento)

    def preencher_formulario(self, nome, contato, data, pagamento):
        self.preencher_nome(nome)
        self.preencher_contato(contato)
        self.preencher_data(data)
        self.selecionar_pagamento(pagamento)

    def clicar_register(self):
        botao = self.wait.until(
            EC.presence_of_element_located(self.botao_register)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            botao
        )

        self.wait.until(
            EC.element_to_be_clickable(self.botao_register)
        )

        self.driver.execute_script("arguments[0].click();", botao)

    def obter_texto_pagina(self):
        return self.driver.find_element(By.TAG_NAME, "body").text
    
    def esta_na_pagina_de_confirmacao(self):
        return "/form-confirmation" in self.driver.current_url
    
    def limpar_formulario(self):
        campo_nome = self.wait.until(
            EC.visibility_of_element_located(self.campo_nome)
        )
        campo_contato = self.wait.until(
            EC.visibility_of_element_located(self.campo_contato)
        )
        campo_data = self.wait.until(
            EC.visibility_of_element_located(self.campo_data)
        )

        campo_nome.clear()
        campo_contato.clear()
        campo_data.clear()