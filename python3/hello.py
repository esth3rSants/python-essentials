#!/usr/bin/env python3
""" Programa Multi Línguas

Esse código retorna o "Hello World" baseado na língua que está instalada no 
sistema operacional.

Como usar o programa: 
Tenha a variável LANG corretamente configurada, exemplo:

        export LANG=pt_BR

Execução:

    python3 hello.py
        ou
    ./hello.py (para executar usando esse comando, será necessário configurar
    a permissão do usário chmod +x hello.py)
"""
__version__ ="0.0.1"
__autho__ = "Esther Ribeiro"
__license__ = "Unlicense"

import os
# a função GETEVEN pede a variável de sistema LANG que possibilita o módulo  
#'OS' ter acesso diretamente a configuranção de idioma do ambiente(sistema operacional).
#foi necessário o acréscimo do [:5] para pegar somente os cinco primeiros 
#digítos da configuração do idioma, que pode padrão vem escrito dessa forma 
#nos sistema operacionais : 'pt_BR.utf8'
# Caso o sistema opereacional não tenha nenhuma configuração do GETEVEN por 
#padrão o msg vai ser traduzido para o inglês.
current_language = os.getenv("LANG", "en_US")[:5]

msg ="Hello World!!!" 

if current_language == "pt_BR":
    msg = "Olá Mundo!!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"


print(msg)

