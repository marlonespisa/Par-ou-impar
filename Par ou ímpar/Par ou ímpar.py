while True:
    numero = input('Digite um número para saber se é par ou impar: ')
    if numero.isdigit():
        numero = float(numero)
        resto = numero % 2
        if resto == 0:
            print('O número é par')
        else:
            print('O número é ímpar')
        deseja_continuar = input('Para continuar a descobrir se um número é par ou ímpar, digite [s] para sim ou [n] para não? ')
        while deseja_continuar != 's' and deseja_continuar != 'n':
            print('Digite somente "s" ou "n"')
            deseja_continuar = input('Para continuar a descobrir se um número é par ou ímpar, digite [s] para sim ou [n] para não? ')
        if deseja_continuar == 'n':
            break
    else:
        print('Comando inválido, digite somente números!')
print('***Fim***')

"""
***FORMULA***

numero = float(input('Digite um número para saber se é par ou impar:'))
resto = numero % 2

if resto == 0:
    print('Número é par')
else:
    print('Número é impar')
"""
