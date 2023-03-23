nota1 = int(input("Insira a primeira nota (0 a 100): "))
nota2 = int(input("Insira a segunda nota (0 a 100): "))

if nota1 + nota2 >= 60 and nota1 >= 40 and nota2 >= 40:
    print("O aluno passou!")
else:
    print("O aluno não passou.")