from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaginaCadastro:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://practice.expandtesting.com/register"
        self.wait = WebDriverWait(driver, 10)

        self.campo_username = (By.ID, "username")
        self.campo_password = (By.ID, "password")
        self.campo_confirm_password = (By.ID, "confirmPassword")
        self.botao_register = (By.CSS_SELECTOR, "button[type='submit']")
        self.mensagem = (By.ID, "flash")

    def abrir(self):
        self.driver.get(self.url)

    def preencher_username(self, username):
        campo = self.wait.until(
            EC.visibility_of_element_located(self.campo_username)
        )
        campo.clear()
        campo.send_keys(username)

    def preencher_password(self, password):
        campo = self.wait.until(
            EC.visibility_of_element_located(self.campo_password)
        )
        campo.clear()
        campo.send_keys(password)

    def preencher_confirm_password(self, confirm_password):
        campo = self.wait.until(
            EC.visibility_of_element_located(self.campo_confirm_password)
        )
        campo.clear()
        campo.send_keys(confirm_password)

    def preencher_formulario(self, username, password, confirm_password):
        self.preencher_username(username)
        self.preencher_password(password)
        self.preencher_confirm_password(confirm_password)

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

    def obter_mensagem(self):
        mensagem = self.wait.until(
            EC.visibility_of_element_located(self.mensagem)
        )
        return mensagem.text

    def esta_na_pagina_de_login(self):
        return "/login" in self.driver.current_url

    def esta_na_pagina_de_register(self):
        return "/register" in self.driver.current_url