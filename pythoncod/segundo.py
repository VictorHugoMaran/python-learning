aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print(f"O aluno {aluno} foi aprovado com média {media:.2f}!")
elif media < 5:
    print(f"O aluno {aluno} foi reprovado com média {media:.2f}!")
else:
    print(f"O aluno {aluno} está em recuperação com média {media:.2f}!")