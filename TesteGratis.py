from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import time
import os
import json

load_dotenv()


def gerar_teste():
    opcoes = Options()
    opcoes.add_experimental_option("debuggerAddress", os.getenv("CHROME_DEBUG_ADDRESS"))

    # Conecta no Chrome que você já abriu pelo terminal
    navegador = webdriver.Chrome(options=opcoes)
    navegador.implicitly_wait(5)

    # Acessa direto o dashboard (aproveitando o login já feito na janela)
    navegador.get(os.getenv("URL_DASHBOARD"))

    testegratis = navegador.find_element(By.XPATH, '//*[@id="navbar-nav"]/div[1]/div[2]/div/div/div/li[12]/a')
    testegratis.click()
    time.sleep(1)
    testeIptv = navegador.find_element(By.XPATH, '//*[@id="sidebarQuickTest"]/ul/li[1]/a')
    testeIptv.click()
    time.sleep(3)

    loginteste = navegador.find_element(By.XPATH, '//*[@id="myModal"]/div/div/div[2]/pre').text
    Dns = os.getenv("DNS_URL")
    for linha in loginteste.splitlines():
        if "Usuário" in linha:
            Usuario = linha.split(":", 1)[1].strip("* ")
        elif "Senha:" in linha:
            senha = linha.split(":", 1)[1].strip("* ")

    dados = {"Usuario": Usuario, "Senha": senha, "Dns":Dns}
    with open("UltimoTeste.json", "w") as arquivo:
        json.dump(dados,arquivo)

    MensagemTeste = f"""✅ *SEU ACESSO ESTÁ LIBERADO!*

Você tem *6 horas* para testar com calma e ver a qualidade na prática. 📺

👤 *Usuário:* {Usuario}
🔑 *Senha:* {senha}
🌐 *DNS:* {Dns}

*Como ativar em 1 minuto:*
1️⃣ Abra o aplicativo que você instalou
2️⃣ Escolha a opção de login com usuário e senha
3️⃣ Digite os dados acima e pronto!

⏳ O teste expira em 6 horas, então aproveite agora para testar nos canais, filmes e séries que você mais assiste.

Qualquer dúvida na instalação, me chama aqui que eu te ajudo na hora! 🙌

Gostou? Me avisa que eu te passo os planos e já deixo seu acesso definitivo ativado. 😉"""

    navegador.get("https://www.google.com/?hl=pt_BR")
    return MensagemTeste, Usuario


print(gerar_teste())
