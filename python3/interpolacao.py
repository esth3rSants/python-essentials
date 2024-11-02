 email_tmpl = """
    ...: Olá, %(nome)s
    ...: 
    ...: Você tem interesse em comprar %(produto)s ?
    ...: 
    ...: Este produto é ótimo para resolver %(texto)s
    ...: 
    ...: Clique agora em %(link)s
    ...: 
 Apenas %(quantidade)d disponiveis!!!!
 
 Preço promocional R$ %(preco).2f
 
 """


In [20]: for cliente in clientes:
     print(email_tmpl
     % {
         "nome":cliente,
         "produto": "Estante",
         "texto": "Armazenar equipamentos, objetos pessoais e de trabalho",
         "link": "https://estantemaneira.io",
         "quantidade": 8,
         "preco": 162.30,
         }
)
 




