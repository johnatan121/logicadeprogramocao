frutas = ["maçã", "banana", "uva"]
print("Lista inicial:", frutas)
nova_fruta = input("Digite uma fruta para adicionar: ")
posicao = int(input("Digite a posição onde deseja inserir (0 para início): "))
frutas.insert(posicao, nova_fruta)
print("Lista atualizada:", frutas)
opcao = input("Deseja adicionar mais uma fruta (s/n)? ")
if opcao == "s":
    outra_fruta = input("Digite a nova fruta: ")
    frutas.append(outra_fruta) 
    print("Lista final:", frutas)
else:
    print("Lista completa:", frutas)