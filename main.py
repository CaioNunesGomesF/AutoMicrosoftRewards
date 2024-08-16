import pyautogui
import pygetwindow as gw
import time

# Abrir Windows 
pyautogui.press('win')

# Apos abrir o windows, pesquisar pelo microsoft edge.

pyautogui.write('Microsoft Edge')

pyautogui.press('Enter')

# Entrar no  Microsoft | Rewards  

pyautogui.sleep(1)

pyautogui.moveTo(1778, 131)

pyautogui.click()

pyautogui.sleep(1)

pyautogui.moveTo(1600, 182)

pyautogui.click()

# Fazer missões do dia

pyautogui.sleep(2)

# Primeira
pyautogui.moveTo(539, 735)
pyautogui.keyDown('ctrl')
pyautogui.click()
pyautogui.keyUp('ctrl')

# Segunda
pyautogui.moveTo(1140, 691)
pyautogui.keyDown('ctrl')
pyautogui.click()
pyautogui.keyUp('ctrl')

# Terceiro
pyautogui.moveTo(1511, 685)
pyautogui.keyDown('ctrl')
pyautogui.click()
pyautogui.keyUp('ctrl')
pyautogui.sleep(1)

# Quarto

pyautogui.press('tab')
pyautogui.press('tab')

pyautogui.keyDown('ctrl')
pyautogui.press('Enter')
pyautogui.keyUp('ctrl')


# quinto até decimo 

for i in range(5):
    pyautogui.press('tab')
    pyautogui.keyDown('ctrl')
    pyautogui.press('Enter')
    pyautogui.keyUp('ctrl')

# Fechar chrome e reabrir para não ficar bagunçado

pyautogui.keyDown('Alt')
pyautogui.press('F4')
pyautogui.keyUp('Alt')

# Reabrir Windows 
pyautogui.press('win')

# Pesquisar pelo microsoft edge novamente.

pyautogui.write('Microsoft Edge')

pyautogui.sleep(1)

pyautogui.press('Enter')

pyautogui.click(192, 54)
pyautogui.click(192, 54)


# Pesquisas

def search_topic(topic):
    pyautogui.write(topic)
    pyautogui.sleep(1)
    pyautogui.press('Enter')
    pyautogui.sleep(5)
    pyautogui.keyDown('Ctrl')
    pyautogui.press('t')
    pyautogui.keyUp('Ctrl')
    

topics = [
 "Inteligência Artificial e Machine Learning",
"Mudanças Climáticas e Sustentabilidade",
"Tecnologias de Energia Renovável",
"Impacto da Tecnologia na Educação",
"Segurança Cibernética e Privacidade de Dados",
"Desenvolvimento de Software e Engenharia de Sistemas",
"Robótica e Automação",
"Realidade Virtual e Aumentada",
"Blockchain e Criptomoedas",
"Internet das Coisas (IoT)",
"Computação Quântica",
"Saúde Digital e Telemedicina",
"Desigualdade Social e Inclusão Digital",
 "Economia Digital e Comércio Eletrônico",
"Mobilidade Urbana e Veículos Autônomos",
"Tecnologias de Assistência para Pessoas com Deficiência",
"Desenvolvimento Sustentável e Economia Circular",
"Impacto das Redes Sociais na Sociedade",
"Tecnologias de Comunicação 5G",
"Big Data e Análise de Dados",
"Desafios Éticos na Inteligência Artificial",
"Tecnologias de Agricultura Inteligente",
"Desenvolvimento de Jogos e Gamificação",
"Cidades Inteligentes e Infraestrutura Urbana",
"Tecnologias de Conservação Ambiental",
"Educação STEM (Ciência, Tecnologia, Engenharia e Matemática)",
"Tecnologias de Assistência Médica e Biotecnologia",
"Impacto da Automação no Mercado de Trabalho",
"Tecnologias de Produção e Manufatura Avançada",
"Desenvolvimento de Aplicativos Móveis"
]

for topic in topics:
    search_topic(topic)
    time.sleep(5)
    
    