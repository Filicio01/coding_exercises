print ('Bem vindo, calcule seu IMC aqui...')
nome = input('Digite seu nome: ')
sexo = input('Digite seu sexo "M" para masculino e "F" para feminino: ').lower

valid_alt = False
while valid_alt == False:
    alt = input('Digite sua Altura: ')
    try:
        alt = float(alt)
        break 
    except:
        print ('Formato de altura incorreto, utilize "." para separar as casas decimais.')

valid_alt == True
while valid_alt == False:
    peso = input('Digite seu peso: ')
    try:
        peso = float(peso)
        break 
    except:
        print ('Formato de peso incorreto, utilize "." para separar as casas decimais.')
valid_alt == True
def imc(peso, alt):
        valor_imc = float(peso) / float((alt*alt))
        return(valor_imc)
if sexo == 'f':
    print ('calculando seu peso, aguarde.')
    if valor_imc < 19.1:
            print(nome + 'Voce está abaixo do Peso')
            
    elif valor_imc > 19.1 and valor_imc < 25.8 :
            print(nome +' ' + 'Voce está  no Peso ideal')
                                       
    elif valor_imc > 25.8 and valor_imc < 27.3 :
            print(nome +' '+ 'Voce está um pouco acima do Peso ideal')
                                       
    elif valor_imc > 27.3 and valor_imc < 32.3 :
            print(nome +' '+ 'Voce está sobrepeso ')
                                       
    elif valor_imc > 32.3 :
            print(nome +' '+ 'Voce está Gordona')
    if sexo == 'm':
        print ('calculando seu peso, aguarde.')
    elif valor_imc < 20.7:
            print(nome + 'Voce está abaixo do Peso')
            
    elif valor_imc  > 20.7 and valor_imc < 26.4 :
            print(nome +' ' + 'Voce está  no Peso ideal')
                                       
    elif valor_imc > 26.4 and valor_imc < 27.8 :
            print(nome +' '+ 'Voce está um pouco acima do Peso ideal')
                                       
    elif valor_imc > 27.8 and valor_imc < 31.1 :
            print(nome +' '+ 'Voce está sobrepeso ')
                                       
    elif valor_imc  > 31.1 :
            print(nome +' '+ 'Voce está Gordão')
else:
        print ('Erro')


