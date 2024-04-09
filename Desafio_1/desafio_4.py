#Sistema de Reservas de Hotel:
#Crie um sistema que permita aos usuários reservar quartos de hotel, com funcionalidades como consulta de disponibilidade e confirmação de reserva.

quartos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Estes sao os quartos disponiveis{quartos} deseja reservar um desses?")

opcao = input("sim ou nao: ")
if opcao == 'sim':
    print("simm")
else:
    print("naoo")    
