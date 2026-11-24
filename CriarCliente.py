from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import time
import os
import json

load_dotenv()


def CriarCliente(nome, telefone):
  #Puxar UltimoUsuarioTEste
  with open("UltimoTeste.json", "r") as arquivo:
    dados = json.load(arquivo)

  usuario_cliente = dados["Usuario"]
  opcoes = Options()
  opcoes.add_experimental_option("debuggerAddress", os.getenv("CHROME_DEBUG_ADDRESS"))

  # Conecta no Chrome que você já abriu pelo terminal
  navegador = webdriver.Chrome(options=opcoes)
  navegador.implicitly_wait(5)

  # Acessa direto o dashboard (aproveitando o login já feito na janela)
  navegador.get(os.getenv("URL_GERENCIAR_CLIENTES"))
  time.sleep(3) 
  PesquisaUsername = navegador.find_element(By.XPATH, '//*[@id="filterLines"]/div/div[1]/div/input')
  time.sleep(3) 
  PesquisaUsername.send_keys(usuario_cliente)
  time.sleep(3)
  EnviarPesquisaUsuario = navegador.find_element(By.XPATH, '//*[@id="filterLines"]/div/div[7]/div/button')
  EnviarPesquisaUsuario.click()
  time.sleep(2)
  opcoesUsuario = navegador.find_element(By.XPATH, '//table//tbody/tr/td/div/button')
  opcoesUsuario.click()
  time.sleep(2)
  editarUsuario = navegador.find_element(By.LINK_TEXT, "Editar")
  editarUsuario.click()
  time.sleep(2)
  adicionarnome = navegador.find_element(By.NAME, 'name')
  time.sleep(2)
  adicionarnome.send_keys(nome)

  adicionartelefone = navegador.find_element(By.ID, 'phone')
  adicionartelefone.send_keys(telefone)

  
print(CriarCliente("Teste", "29998973212"))
