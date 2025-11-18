#n1 = int( input(F"digite um numoro: "))
##n2 = int( input(f"digite um numero: "))
#proximo =  n1+1

#print(proximo)
#print (F"soma de {n1} e {n2} = {n1+n2}")

#idade = int(input("digite sua idade "))

#if idade >= 18:
    #print("voce e maior de idade")
#else:
    #print("voce e menor de idae")

#nota = float(input("digite sua nota "))
#if nota == 10:
    #print("nota maxima! parabens")
#elif nota >= 7: 
    #print("aprovado")
#elif nota >= 5:
   #print("recuperacao")
#else:
    #print("reprovado")
"""cadastro = float(input("digite numero de alunos "))
if cadastro == 12:
     print('sala lotada ')
elif cadastro >=9:
     print("sala cheia ")
elif cadastro == 6:
    print("sala esta meia vazia ")
elif cadastro >=4:
    print("muitos alunos faltaram") 
else: 
    print("não tera aula")           
"""
passou_de_ana = input("voê passou de ano? (sim/não):").strip().lower()
passou_no_vestibular =input("você passou no vestibular? (sim/não):").strip().lower()

if passou_de_ana == "sim":
    if passou_no_vestibular == "sim":
        print("comecarei a faculdade no proximo ano. ")
    else:
        print("vou precisar tenta o vestibular novamente") 
else:
    print("preciso estudar mais para passar de ano. ")           