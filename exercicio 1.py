#1:
n1 = float(input('fale o primeiro numero: '))
n2 = float(input('fale o segundo numero: '))
if n1 < n2:
    print('o {} é o maior numero e o {} é o menor numero' .format(n2,n1))
elif n1 > n2:
    print('o {} é o maior numero e o {} é o menor numero'.format(n1,n2))
else:
    print('os numeros sao iguais')

#2:
dia = int(input('qual é o dia? '))
mes = int(input('qual é o mes? '))
ano = int (input('qual é o ano? '))
if mes == 1 or mes ==  3 or mes ==  5 or mes == 7 or mes ==  8 or mes == 10 or mes == 12:
    if dia <= 31 and ano > 0: 
        print(' a data é valida, {}/{}/{}'.format(dia,mes,ano))
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30 and ano > 0:
        print('a data é valida, {}/{}/{}' .format(dia,mes,ano))
else:
    print('data invalida.')

#3:
peso = float(input('fale seu peso: '))
altura = float(input('fale sua altura: '))
imc = peso/altura**2
if imc < 20:
    print('abaixo do peso')
elif imc >= 20 and imc <= 25:
    print('peso normal')
elif imc >= 25 and imc <= 30:
    print('sobre peso')
elif imc >= 30 and imc <= 40:
    print('obeso')
else:
    print('obeso morbido')


#4:
numero = float(input('digite um numero: '))
raiz = numero **(1/2) 
if numero > 0:
    print('a raiz quadrada desse numero é {}' .format(raiz) ) 
else:
    print('o numero é invalido')

#5:

bissexto = int(input('digite o ano: '))
if bissexto % 400 == 0 or bissexto % 4 == 0 and bissexto % 100 != 0:
    print('esse ano é bissexto.')
else:
    print('esse ano nao é bissexto')


#6:
idade = int(input('qual é a sua idade: '))
if idade >= 5 and idade <= 7:
    print('categoria infantil A')
elif idade >= 8 and idade <= 11:
    print('categoria infantil B')
elif idade >= 12 and idade <= 13:
    print(' categoria juvenil A') 
elif idade >= 14 and idade <= 17:
    print('categoria juvenil B')
else:
    print('categoria adulto.')


#7:
bitsum = 0 
bitzero = 0
bits1 = int(input('digite um bit (0 ou 1): '))
if bits1 == 0:
    bitzero = bitzero + 1
elif bits1 == 1:
        bitsum = bitsum + 1
bits2 = int(input('digite um bit (0 ou 1): '))
if bits2 == 0:
    bitzero = bitzero + 1
elif bits2 == 1:
        bitsum = bitsum + 1
bits3= int(input('digite um bit (0 ou 1): '))
if bits3 == 0:
    bitzero = bitzero + 1
elif bits3 == 1:
        bitsum = bitsum + 1
bits4= int(input('digite um bit (0 ou 1): '))
if bits4 == 0:
    bitzero = bitzero + 1
elif bits4 == 1:
        bitsum = bitsum + 1
bits5= int(input('digite um bit (0 ou 1): '))
if bits5 == 0:
    bitzero = bitzero + 1
elif bits5 == 1:
        bitsum = bitsum + 1
bits6= int(input('digite um bit (0 ou 1): '))
if bits6 == 0:
    bitzero = bitzero + 1
elif bits6 == 1:
        bitsum = bitsum + 1
bits7= int(input('digite um bit (0 ou 1): '))
if bits7 == 0:
    bitzero = bitzero + 1
elif bits7 == 1:
        bitsum = bitsum + 1
bits8 = int(input('digite um bit (0 ou 1): '))
if bits8 == 0:
    bitzero = bitzero + 1
elif bits8 == 1:
        bitsum = bitsum + 1
           
print('temos {} zeros e {} uns no byte' .format(bitzero,bitsum))     

#8:
semana = int(input('digite um numero entre 1 e 7: '))
if semana == 1:
    print('é domingo')
elif semana == 2:
    print('é segunda')
elif semana == 3:
    print('é terça')
elif semana == 4:
    print('é quarta')
elif semana == 5:
    print('é quinta')
elif semana == 6:
    print ('é sexta')
elif semana == 7:
    print('é sabado')
else:
    print('nao existe dia de semana com este numero.')

#9:  
numero = float(input('digite um numero qualquer:  '))
if numero % 3 == 0 and numero % 7 == 0:
    print('esse numero é divisivel por 3 e 7 ao mesmo tempo.')
else:
    print('esse numero nao é divisivel por 3 e 7 ao mesmo tempo.')

#10
a = float(input('digite o valor de A: '))
b = float(input('digite o valor de B: '))
c = float(input('digite o valor de c: '))
d = float(input('digite o valor de D: '))
if a > b and a > c and a > d:
    print(' {} é o maior numero'.format (a))
elif b > a and b > c and b > d:
    print(' {} é o maior numero'.format (b))
elif c > a and c > b and c > d:
    print(' {} é o maior numero'.format (c))
elif d > a and d > b and d > c:
    print(' {} é o maior numero'.format (d))
if a < b and a < c and a < d:
    print (' E o {} é o menor numero '. format(a))
elif b < a and b < c and b < d:
    print (' E o {} é o menor numero '. format(b))
elif c < a and c < b and c < d:
    print (' E o {} é o menor numero '. format(c))
elif d < a and d < b and d < c:
    print (' E o {} é o menor numero '. format(d))
else:
    print ('valor invalido')
