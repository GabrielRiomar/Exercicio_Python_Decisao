#Lista de exercicios 01 - Estrutura de Decisão Endereço: https://wiki.python.org.br/EstruturaDeDecisao
q = int(input('Informe a questão: '))
if q == 1:
    #Botei a pergunta e a resolução em cada 'switch'
    print(q, 'Faça um Programa que peça dois números e imprima o maior deles.')
    x = int(input('Informe 1° numero:'))
    y = int(input('Informe 2° numero:'))
    if x > y:
        print("1° numero é maior que o 2° numero")
    else:
        print("2° numero é maior que o 1° numero")
if q == 2:
    print(q, 'Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.')
    x = int(input('Informe um numero:'))
    if x>0:
        print("Positivo")
    else:
        print("Negativo")
if q == 3:
    print(q, 'Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.')
    sexo = input('Digite (F)-Feminino, (M)-Masculino: ').upper()
    if sexo == 'M':
        print('Masculino')
    elif sexo == 'F':
        print('Feminino')
    else:
        print('Sexo Inválido')
if q == 4:
    print(q, 'Faça um Programa que verifique se uma letra digitada é vogal ou consoante.')
    letra = input('Informe alguma letra: ')
    vogais = 'aeiou'
    if letra in vogais or letra in vogais.upper(): #upper() pega letras com Caps ativo
        print(letra, 'é uma vogal')
    else:
        print(letra, 'é uma consoante')
if q == 5:
    print(q, '''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
        A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
        A mensagem "Reprovado", se a média for menor do que sete;
        A mensagem "Aprovado com Distinção", se a média for igual a dez.''')
    nota1 = float(input('Informe a primeira nota:'))
    nota2 = float(input('Informe a segunda nota:'))
    media = (nota1 + nota2)/2
    if media>=7:
        print('Aprovado')
    elif media==10:
        print('Aprovado com Distinção')
    else:
        print('Reprovado')
if q == 6:
    print(q, 'Faça um Programa que leia três números e mostre o maior deles.')
    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))
    num3 = int(input("Número 3: "))

    if num1 > num2 and num1 > num3:
        print("O Número 1 é o maior: ", num1)
    elif num2 > num1 and num2 > num3:
        print("O Número 2 é o maior: ", num2)
    elif num3 > num2 and num3 > num1:
        print("O Número 3 é o maior: ", num3)
if q == 7:

    print(q, 'Faça um Programa que leia três números e mostre o maior e o menor deles.')
    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))
    num3 = int(input("Número 3: "))

    if num1 > num2 and num1 > num3:
        print("O Número 1 é o maior: ", num1)
    elif num2 > num1 and num2 > num3:
        print("O Número 2 é o maior: ", num2)
    elif num3 > num2 and num3 > num1:
        print("O Número 3 é o maior: ", num3)

    if num1 < num2 and num1 < num3:
        print("O Número 1 é o menor: ", num1)
    elif num2 < num1 and num2 < num3:
        print("O Número 2 é o menor: ", num2)
    elif num3 < num2 and num3 < num1:
        print("O Número 3 é o menor: ", num3)
if q == 8:
   print(q, 'Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.')
   produto1 = float(input("Digite o preço do primeiro produto: "))
   produto2 = float(input("Digite o preço do segundo produto: "))
   produto3 = float(input("Digite o preço do terceiro produto: "))

   if produto1 < produto2 and produto1 < produto3:
           print("Você deve comprar o primeiro produto!")
   elif produto2 < produto1 and produto2 < produto3:
           print("Você deve comprar o terceiro produto!")
   elif produto3 < produto1 and produto3 < produto1:
            print("Você deve comprar o terceiro produto!")
if q == 9:

    print(q, 'Faça um Programa que leia três números e mostre-os em ordem decrescente.')
    decrescente = []
    qtd = 3
    for i in range(qtd):
        numero = int(input('Digite um numero: '))
        decrescente.append(numero)

    decrescente.sort(reverse=True)
    print(decrescente)
if q == 10:
    print(q, 'Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.')
    turno = input('Digite (M)-Matutino ou (V)-Vespertino ou (N)-Noturno para o turno que você estuda: ').upper()
    if turno == 'M':
        print('Bom Dia!')
    elif turno == 'V':
        print('Boa Tarde!')
    elif turno == 'N':
        print('Boa Noite')
    else:
        print('Valor Inválido!')
if q == 11:
    print(q, '''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.''')
    salario = float(input('Salário do colaborador: '))

    if (salario <= 280):
        percentual = 20
    elif (salario <= 700):
        percentual = 15
    elif (salario <= 1500):
        percentual = 10
    else:
        percentual = 5

    print('Salário original: R$ ', salario)
    print('Percentual: ', percentual, '%')

    percentual = percentual / 100.0
    aumentoSalario = percentual * salario
    novoSalario = salario + aumentoSalario

    print('Aumento: R$ ', aumentoSalario)
    print('Novo salário: R$ ', novoSalario)
if q == 12:
    print(q, '''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
        Desconto do IR:
        Salário Bruto até 900 (inclusive) - isento
        Salário Bruto até 1500 (inclusive) - desconto de 5%
        Salário Bruto até 2500 (inclusive) - desconto de 10%
        Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.''')

    valor_hora = float(input('Digite o valor da hora de trabalho: '))
    qtd_hora_trabalhada = float(input('Digite a quantidade de hora trabalhada no mês: '))

    salario_bruto = valor_hora * qtd_hora_trabalhada

    def descontos(salario_bruto):
        desc_sindicato = (salario_bruto*3)/100
        fgts = (salario_bruto*11)/100
        ir = 0
        if salario_bruto <= 900:
            salario_liquido = salario_bruto - desc_sindicato

        elif salario_bruto <= 1500:
            ir = (salario_bruto*5)/100
            salario_liquido = salario_bruto - desc_sindicato - ir

        elif salario_bruto <= 2500:
            ir = (salario_bruto*10)/100
            salario_liquido = salario_bruto - desc_sindicato - ir

        else:
            ir = (salario_bruto*20)/100
            salario_liquido = salario_bruto - desc_sindicato - ir

        imprime_desconto(salario_bruto, desc_sindicato, ir, fgts, salario_liquido)


    def imprime_desconto(salario_bruto, desc_sindicato, ir, fgts, salario_liquido):
        print('''
        Salario Bruto: %.2f
        Desconto Sindicato: %.2f
        Desconto IR: %.2f
        FGTS: %.2f

        Salario Liquido: %.2f
        ''' % (salario_bruto, desc_sindicato, ir, fgts, salario_liquido))
    descontos(salario_bruto)
if q == 13:
    #Usando função dicionario
    print(q, 'Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.')
    diaSemana = int(input('Informe o dia da semana: '))

    def verDiaSemana(diaSemana):
        dicionario_dia_semana = {1: 'domingo', 2: 'segunda', 3: 'terça', 4: 'quarta', 5: 'quinta', 6: 'sexta', 7: 'sabado'}
        for dia in dicionario_dia_semana.keys():
            if diaSemana == dia:
                print('------', dicionario_dia_semana[dia].capitalize(), '------') #.capitalize() Deixar maisculo
                break
        else:
            print('Dia não encontrando')
    verDiaSemana(diaSemana)
if q == 14:

    print(q, '''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
                Média de Aproveitamento  Conceito
                Entre 9.0 e 10.0        A
                Entre 7.5 e 9.0         B
                Entre 6.0 e 7.5         C
                Entre 4.0 e 6.0         D
                Entre 4.0 e zero        E
                O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.''')
    nota1 = float(input('Informe a primeira nota:'))
    nota2 = float(input('Informe a segunda nota:'))
    media = (nota1 + nota2) / 2
    if media<=10 and media>=9:
        print('1° Nota:', nota1)
        print('2° Nota:', nota2)
        print('Sua média foi de: ', media, '\nEntão sua Médiade Aproveitamento Conceito será A')
    elif media<9 and media>=7.5:
        print('1° Nota:', nota1)
        print('2° Nota:', nota2)
        print('Sua média foi de: ', media, '\nEntão sua Médiade Aproveitamento Conceito será B')
    elif media<7.5 and media>=6:
        print('1° Nota:', nota1)
        print('2° Nota:', nota2)
        print('Sua média foi de: ', media, '\nEntão sua Médiade Aproveitamento Conceito será C')
    elif media<6 and media>=4:
        print('1° Nota:', nota1)
        print('2° Nota:', nota2)
        print('Sua média foi de: ', media, '\nEntão sua Médiade Aproveitamento Conceito será D')
    else:
        print('1° Nota:', nota1)
        print('2° Nota:', nota2)
        print('Sua média foi de: ', media, '\nEntão sua Médiade Aproveitamento Conceito será E')
if q == 15:
    print(q, '''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
                Dicas:
                Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
                Triângulo Equilátero: três lados iguais;
                Triângulo Isósceles: quaisquer dois lados iguais;
                Triângulo Escaleno: três lados diferentes;''')
    x = input('Digite o tamanho do primeiro lado: ')
    y = input('Digite o tamnanho do segundo lado: ')
    z = input('Digite o tamanho do terceiro lado: ')

    if x + y > z:
        if x == y and x == z:
            print('Triângulo Equilátero')
        elif x == y or y == z or x == z:
            print('Triângulo Isósceles')
        elif x != y and z or y != x and z or x != z:
            print('Triângulo Escaleno')
    else:
        print('Não é um triângulo')
if q == 16:
    print(q, '''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
                Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
                Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
                Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
                Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;''')
    import math
    #importando marth para ser possivel utilizar raiz quadrada com math.sqrt(x)
    print('Equaçao do 2° grau da forma: ax² + bx + c')

    a = int(input('Coeficiente a: '))

    if (a == 0):
        print('"a" "deu igual a 0, não é equação do segundo grau.')
    else:
        b = int(input('Coeficiente b: '))
        c = int(input('Coeficiente c: '))
        delta = b * b - (4 * a * c)

        if delta < 0:
            print('Delta deu negativo, a equação não possui raizes reais')
        elif delta == 0:
            raiz = -b / (2 * a)
            print('Delta=0 , raiz = ', raiz)
        else:
            raiz1 = (-b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-b - math.sqrt(delta)) / (2 * a)
            print('Raizes: ', raiz1, ' e ', raiz2)
if q == 17:
    print(q, 'Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.')
    ano = int(input('Informe um ano: '))
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print('>Bissexto<')
    else:
        print('Não é bissexto')
if q == 18:
    print(q, 'Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.')
    dia = int(input('DD: '))
    mes = int(input('MM: '))
    ano = int(input('AAAA: '))

    data = False

    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        if (dia <= 31):
            data = True
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if (dia <= 30):
            data = True
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if (dia <= 29):
                data = True
        elif (dia <= 28):
            data = True

    if (data):
        print('-------Válida-------')
    else:
        print('-------Inválida-------')
if q == 19:
    print(q, '''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
                Observando os termos no plural a colocação do "e", da vírgula entre outros. 
                Exemplo:
                326 = 3 centenas, 2 dezenas e 6 unidades
                12 = 1 dezena e 2 unidades 
                Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16''')
    num = int(input('Digite um numero inteiro positivo: '))

    unidade = num % 10
    num = (num - unidade) / 10
    dezena = num % 10
    num = (num - dezena) / 10
    centena = num
    dezena = int(dezena)
    centena = int(centena)
    print('', centena, '= centena\n', dezena, '= dezena\n', unidade, '= unidade')
if q == 20:
    print(q, '''Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
                A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
                A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
                A mensagem "Aprovado com Distinção", se a média for igual a 10.''')
    nota1 = float(input('Informe a primeira nota:'))
    nota2 = float(input('Informe a segunda nota:'))
    nota3 = float(input('Informe a terceira nota:'))
    media = (nota1 + nota2 + nota3) / 3
    if media == 10:
        print('Sua média foi de: ', media, '\nAprovado com Distinção')
    elif media >= 7:
        print('Sua média foi de: ', media, '\nAprovado')
    elif media < 7:
        print('Sua média foi de: ', media, '\nReprovado')
if q == 21:
    print(q, '''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
                Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
                Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.''')
    numero = int(input('Valor para sacar (Possibilidades 10-600): '))
    cem = int(numero / 100)
    numero = numero % 100
    cinquenta = int(numero / 50)
    numero = numero % 50
    dez = int(numero / 10)
    numero = numero % 10
    cinco = int(numero / 5)
    numero = numero % 5
    um = numero

    print('Notas R$100,00 = ', cem)
    print('Notas R$ 50,00 = ', cinquenta)
    print('Notas R$ 10,00 = ', dez)
    print('Notas R$  5,00 = ', cinco)
    print('Notas R$  1,00 = ', um)
if q == 22:
    print(q, 'Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).')
    x = int(input('Digite um inteiro: '))

    if x % 2: # x%2 é a mesma coisa que (x%2)==0
        print("Ímpar")
    else:
        print("Par")
if q == 23:
    print(q, 'Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.')
    numero = float(input('Digite um numero: '))
    if numero == int:
        print('Inteiro')
    else:
        print('Decimal')
if q == 24:
    print(q, '''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
                par ou ímpar;
                positivo ou negativo;
                inteiro ou decimal.''')
    x = int(input('Digite um numero: '))
    y = int(input('Digite outro numero: '))

    print('Informe a operação')
    operacao = int(input('1 - +\n2 - -\n3- *\n4 - /\n'))
    if operacao == 1:
            op = x + y
    elif operacao == 2:
            op = x - y
    elif operacao == 3:
            op = x * y
    elif operacao == 4:
            op = x / y
    else:
        print('Operação não existe')
        exit()

    print('Resultado = ', op)

    if op % 2 == 0:
         print('Pár')
    else:
         print('Impár')

    if op >= 0:
        print('Positivo')
    else:
        print('Negativo')

    if type(op) == int:
        print('Inteiro')
    else:
        print('Decimal')
if q == 25:
    print(q, '''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
                "Telefonou para a vítima?"
                "Esteve no local do crime?"
                "Mora perto da vítima?"
                "Devia para a vítima?"
                "Já trabalhou com a vítima?" 
                O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
                Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".''')
    resposta = []
    resposta.append(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
    resposta.append(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
    resposta.append(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
    resposta.append(input("Devia para a vítima? 1/Sim ou 0/Não: "))
    resposta.append(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))
    soma_respostas = 0
    for i in resposta:
        soma_respostas += int(i)
    if (soma_respostas < 2):
        print("\nInocente")
    elif (soma_respostas == 2):
        print("\nSuspeita")
    elif (3 <= soma_respostas <= 4):
        print("\nCúmplice")
    elif (soma_respostas == 5):
        print("\nAssassino")
if q == 26:
    print(q, '''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
                Álcool:
                até 20 litros, desconto de 3% por litro
                acima de 20 litros, desconto de 5% por litro
                Gasolina:
                até 20 litros, desconto de 4% por litro
                acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.''')
    litros = float(input('Digite a quantidade em litros: '))
    combustivel = input('Digite o tipo de combustível A-álcool, G-gasolina: ').upper()

    if combustivel == 'A':
        preco = litros * 1.9
        if litros <= 20:
            desconto = litros * ((preco * 3) / 100)
        else:
            desconto = litros * ((preco * 5) / 100)
        print('R$ %.2f' % (preco - desconto))

    elif combustivel == 'G':
        preco = litros * 2.5
        if litros <= 20:
            desconto = litros * ((preco * 4) / 100)
        else:
            desconto = litros * ((preco * 6) / 100)
        print('R$ %.2f' % (preco - desconto))
    else:
        print('Tipo inválido')
if q == 27:
    print(q, '''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
''')
    def calcular_precos():
        count = 0
        calculo_produto = 0
        dados_produto = [("morango", 2.50, 2.20), ("maçã", 1.80, 1.50)]

        while True:
            finalizar = False
            produto = input("Por favor, informe o produto desejado(Morango ou Maçã):")

            for x in range(2):
                if produto.lower() == dados_produto[x][0]:
                    count = x
                    finalizar = True
                    break
                else:
                    if x == 1:
                        finalizar = False
                        print("Valor inválido.", produto)
            if finalizar:
                break
        while True:
            try:
                peso = float(input("Por favor, informe o peso desejado:"))
                if peso > 0:
                    break
                else:
                    continue
            except ValueError:
                print("valor Invalido do peso.")
                continue
        if peso <= 5 and peso > 0:
            calculo_produto = dados_produto[count][1] * peso

        elif peso > 5:
            calculo_produto = dados_produto[count][2] * peso
            if peso > 8 or calculo_produto > 25:
                calculo_produto = (dados_produto[count][2] * peso) - ((dados_produto[count][2] * peso) * 10 / 100)

        print("Valor a pagar:R$%.2f" % calculo_produto)


    calcular_precos()
if q == 28:
    print(q, '''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.''')
    print("1- File Duplo\n2- Alcatra\n3- Picanha\n\n")
    tipo = int(input("Digite o tipo da carne selecionada: "))
    qtd = int(input("Digite a quantidade que será comprada: "))
    resposta = int(input("A compra será realizada com cartao Tabajara? 1 - SIM ||| 2 - NAO: "))

    if tipo == 1:
        nome = "File Duplo"
        if qtd <= 5:
            preco = qtd * 4.9
        else:
            preco = qtd * 5.8

    if tipo == 2:
        nome = "Alcatra"
        if qtd <= 5:
            preco = qtd * 5.9
        else:
            preco = qtd * 6.8

    if tipo == 3:
        nome = "Picanha"
        if qtd <= 5:
            preco = qtd * 6.9
        else:
            preco = qtd * 7.8

    if resposta == 1:
        r = "S"

        desconto = ((preco * 5) / 100)
        total = preco - desconto
    else:
        r = "N"
        total = preco

    print("\n===============================CUPOM FISCAL=========================================")
    print("* Carne.......................................................... %s " % nome)
    print("* Quantidade..................................................... %d kg " % qtd)
    print("* Preço......................................................... %2.f R$ " % preco)
    print("* Cartao Tabajara................................................ %s " % r)
    print("* Total com desconto............................................ %2.f R$ " % total)
    print("===================================================================================")