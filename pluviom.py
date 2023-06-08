import matplotlib.pyplot  as plt
import time
meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho']
chuvas = []
valida = False
mes = 1
tot = 0   
print('Controle Pluviométrico Semestral')
for i in meses:
    ##while valida == False:
        chuva = input('Digite o volume pluviométrico de '+ i+' em ML(utilize "." para separar decimais): ')
      ##  try :
        chuva = float(chuva)
        chuvas.append(chuva)
       # mount = input('Digite o mês atual: ').upper()
        #meses.append(mount)

        ##except:
          ##  print ("Formato inválido, Use apenas numeros e '.' para separar os decimais.")
           ## valida == True
        mes += 1
for a in chuvas:
        tot=+ a
media = tot/6
print('A média de chuva semestral foi ',media)
input('Pressione enter para ver o Gráfico')
plt.plot (meses,chuvas)
plt.show()
input('Pressione Enter para sair')
