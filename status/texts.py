abaixo = abaixo = "Deve-se incluir uma variedade de alimentos saudáveis e nutritivos em sua dieta, como frutas, legumes, grãos integrais, proteínas magras e gorduras saudáveis. Caso precise ganhar peso, deve-se aumentar a ingestão de alimentos calóricos."

normal = "Deve-se ter uma alimentação balanceada, continue consumindo uma variedade de alimentos saudáveis, incluindo frutas, legumes, grãos integrais, proteínas magras e gorduras saudáveis. Garanta que sua dieta seja equilibrada para manter o peso saudável."

acima = "Deve-se reduzir o consumo de alimentos processados, ricos em açúcares adicionados e gorduras saturadas. Concentre-se em alimentos nutritivos, como frutas, legumes, grãos integrais, proteínas magras e gorduras saudáveis. Considere reduzir gradualmente a ingestão de calorias, criando um déficit calórico sustentável. Analise seus hábitos alimentares e verifique se está consumindo uma dieta equilibrada."

obesidade = "Deve-se cortar totalmente o consumo de alimentos processados, ricos em açúcares adicionados, gorduras saturadas e alimentos caloricamente densos. Concentre-se em alimentos nutritivos, como frutas, legumes, grãos integrais, proteínas magras e gorduras saudáveis. Deve-se reduzir completamente a ingestão de calorias para criar um déficit calórico sustentável. Pois nesse estado de massa corporal deve-se cortar ao máximo a ingestão de calorias. Analise seus hábitos alimentares e verifique se está consumindo uma dieta equilibrada."

default = ""

lista = ["", ""]

def IMC(peso, altura):
    if(peso == 0 or altura == 0):
        lista[0] = ""
        lista[1] = ""
        return lista
    else:
        imc = (peso/(altura*altura))
        if(imc < 18):
            lista[0] = "Abaixo do peso"
            lista[1] = abaixo
            return lista
        elif(imc >= 18 and imc < 25):
            lista[0] = "Está no peso certo"
            lista[1] = normal
            return lista
        elif(imc >= 25 and imc < 30):
            lista[0] = "Acima do peso"
            lista[1] = acima
            return lista
        elif(imc >= 30):
            lista[0] = "Obesidade"
            lista[1] = obesidade
            return lista