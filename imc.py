# Aula 4
peso = float(input('Informe o peso(kg): '))
altura = float(input('Informe a altura(cm):'))
imc = peso / (altura ** 2)
print(f'{imc:.2f}')
if imc < 17:
    print('Muito abaixo do peso')
elif imc >= 17 and imc < 18.5:
    print('Abaixo do peso normal')
elif imc >= 18.5 and imc < 25.0:
    print('Peso dentro do normal')
elif imc >= 25.0 and imc < 30:
    print('Acima do peso normal')
elif imc >= 30:
    print('Muito acima do peso')

# Aula 3 COM INPUT:
peso = float(input('Informe o peso(kg): '))
altura = float(input('Informe a altura(cm):'))
imc = peso / (altura ** 2)
print(f'{imc:.2f}')
print(f'Muito abaixo do peso: {imc <  17}')
print(f'Abaixo do peso normal: {imc >= 17 and imc < 18.5}')
print(f'Peso dentro do normal: {imc >= 18.5 and imc < 25.0}')
print(f'Acima do peso normal: {imc >= 25.0 and imc < 30}')
print(f'Muito acima do peso: {imc >= 30}')

# Aula 3 TRUE/FALSE
peso = 84
altura = 1.84
imc = peso / (altura ** 2)
print(f'{imc:.2f}')
print(f'Muito abaixo do peso: {imc <  17}')
print(f'Abaixo do peso normal: {imc >= 17 and imc < 18.5}')
print(f'Peso dentro do normal: {imc >= 18.5 and imc < 25.0}')
print(f'Acima do peso normal: {imc >= 25.0 and imc < 30}')
print(f'Muito acima do peso: {imc >= 30}')
