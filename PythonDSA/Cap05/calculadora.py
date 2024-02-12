print("************Calculadora Python************")
print('Selecione o número da operação desejada')
print('1 - SOMA')
print('2 - SUBTRAÇÃO')
print('3 - MULTIPLICAÇAO')
print('4 - DIVISÃO')
op=input("Digite sua operação (1/2/3/4): ")
a=float(input("Digite o primeiro valor: "))
b=float(input("Digite o segundo valor: "))

if op == '1':
	print(f'{a} + {b} = {a+b}')
elif op =='2':
	print(f'{a} - {b} = {a-b}')
elif op =='3':
	print(f'{a} X {b} = {a*b}')
elif op =='4':
	print(f'{a} / {b} = {a/b}')
else:	
	print("Opção invalida")
