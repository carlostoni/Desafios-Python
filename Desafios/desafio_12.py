#Faça um programa que pergunte uma data ao usuário (dia, mês e ano separadamente) e valide se aquela data é real ou não, fazendo as seguintes validações:
#Verificar se o dia informado existe dentro daquele mês
#Tem 31 dias se o mês for 1, 3, 5, 7, 8, 10 ou 12;
#Tem 30 dias se o mês for 4, 6, 9 ou 11;	
#Tem 28 dias se o mês for 2 e o ano não for bissexto;
#Tem 29 dias se o mês for 2 e o ano for bissexto.
#Verificar se o mês informado existe (ano vai até 12 meses);
#Verificar se o dia, mês e ano são valores positivos.
#Informar ao usuário se a data for válida ou não.

dia = int(input("Digite sua data de nacimento "))
mes = int(input("Digite o mes do seu aniversario "))
ano = int(input("Digite o ano do seu aniversario "))



meses_31 =[1, 3, 5, 7, 8, 10, 12]
bissexto = 0

if mes in meses_31 and mes <= 12:
    print(f"O {mes} tem 31 dias")
elif bissexto == ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print("oi")
        
else:
    print("nao e bissexto")