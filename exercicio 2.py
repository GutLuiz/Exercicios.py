#1:
print('ola mundo')

#2:
numero= input('o numero informado foi: ')
print(numero)

#3:
n= int(input('fale o valor desse numero: '))
g= int(input('fale o valor desse numero: '))
print(n+g)

#4:
primeiro= float(input('fale a pirmeira nota: '))
segunda= float(input('fale a segunda nota: '))
terceiro = float(input('fale a terceira nota: '))
quarta= float(input('fale a quarta nota: '))
media= (primeiro + segunda + terceiro + quarta)/4
print('a media desse bimestre é {}'.format(media))

#5:
metros= float(input('quantos metros: '))
centimetros= (metros*100)
print(centimetros)

#6:
raio= float(input('qual é o raio desse circulo? '))
area= (3.4*raio**2)
print(area)

#7:
base= float(input('me fale o numero da base desse quadrado: '))
altura= float(input('me fale a altura desse quadrado: '))
area= (base*altura)
quadrado= (area*2)
print(quadrado)

#8:
ganho= float(input('quanto voce ganha por hora? '))
horas_trabalhadas= float(input('quanta horas voce trabalha por mes? '))
salario= (ganho*horas_trabalhadas)
print(salario)

#9:
fahrenheit= float(input('qual é a temperatura dele: '))
celsius=  5 * ((fahrenheit-32) / 9)
print(celsius)

#10: 
c= float(input('qual é a temperatura em graus celcius? '))
f= float
faren= f = c * 9/5 + 32
print(faren)

#11:
n1= int(input('me fale um numero: '))
n2= int(input('me fale o segundo numero: '))
n3= int(input('me fale um numero real: '))
calc1= (n1*2)/n2
print(calc1)
calc2= (n1*3) + (n3*3)
print(calc2)
calc3= n3**3
print(calc3)


#12:
alt= float(input('qual é a sua altura? '))
peso_ideal = (72.7*alt) -58
print(peso_ideal)

#13:

h= float(input('me fale sua altura: '))
sexo= input('me fale seu genero: ')
mulher= (62.1*h) -44.7
homem= (72.7*h) - 58
if mulher:
    print('seu peso ideal é {}' .format(mulher))
elif homem:
    print('seu peso ideal é {}'.format(homem))

#14:
peso_de_peixes= float(input('qual é o peso desse peixe: '))
if peso_de_peixes > 50:
    multa= (peso_de_peixes-50)*4
    print('voce foi multado! voce passou do limite maximo, e foi multado no valor de {}'.format(multa))
else:
    print('que belo peixe que voce pegou!')


#15:
hora= float(input('qual é o meu salario por hora? '))
horas_tra= float(input('quantas horas trabalhadas no mes? '))
salario_bruto= hora*horas_tra
print('o salario bruto dele foi {}'.format(salario_bruto))
inss= 8%salario_bruto
print('ele devera pagar {} de inss'.format(inss))
sindicato= 5%salario_bruto
print('ele devera pagar {} do sindicato'.format(sindicato))
ir= 11%salario_bruto
salario_liquido= salario_bruto-(ir+inss+sindicato)
print('o salario liquido dele sera {}'.format(salario_liquido))


#16:
tamanho= int(input(' o tamanho em metros quadrados da área a ser pintada: '))
litros= tamanho/3
latas= int(litros/18)
if litros % 18 !=0:
    latas += 1 
print('voce deve comprar', latas, 'latas.')
print('o valor total é: ', latas * 80)





