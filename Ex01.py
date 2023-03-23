num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

if num1 > num2 + num3 or num2 > num1 + num3 or num3 > num1 + num2:
    print("Pelo menos um dos números é maior que a soma dos outros dois!")
else:
    print("Nenhum dos números é maior que a soma dos outros dois.")