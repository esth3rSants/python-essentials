#!usr/bin/env python

"Divisão dos alimentos por cesta!"
__version__ = "0.1.0"
__author__ = "Esther Ribeiro"


#Dados
sala1 = ["Erick","Estela","Manuela","Pedro"]
sala2 = ["Carlos","Sofia","Joana","Joao"]


aula_ingles = ["Erick","Estela","Joao"]
aula_musica = ["Pedro","Estela","Sofia"]
aula_danca = ["Carlos","Manuela","Joana"]

atividades = [
    ("Inglês", aula_ingles),
    ("Música", aula_musica),
    ("Dança", aula_danca),
]

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:
    print("\n")
    print(f"Alunos da atividade {nome_atividade}")
    


    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
            
    print("Sala1",atividade_sala1)
    print("Sala2",atividade_sala2)
