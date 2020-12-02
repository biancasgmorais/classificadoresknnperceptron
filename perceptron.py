import random
examples = []
teste = []
w1 = 0.5
w2 = 0.5
w3 = 0.5
w4 = 0.5
bias = 0.5

tipo = 0

#importando do txt - tem que ta na mesma pasta
f = open('/Users/Bianca Morais/Google Drive/Engenharia de Computação/11º Período/Sistemas Inteligentes/3ª Unidade/trabalho/conjunto_teste.txt', 'r')
teste = f.readlines()
k = open('/Users/Bianca Morais/Google Drive/Engenharia de Computação/11º Período/Sistemas Inteligentes/3ª Unidade/trabalho/validar.txt', 'r')
validar = k.readlines()
print('\nInsira qual classe vc quer trabalhar:\n[1] SETOSA \n[2]VIRGINICA \n[3]VERSICOLOR:')
tipo = int(input())
k.close()
f.close()

def escolhe_classe():
    global tipo
    tipo_classe = ""
    if(tipo == 1):
        tipo_classe = "Iris-setosa"
    if(tipo == 2):
        tipo_classe = "Iris-virginica"
    if(tipo == 3):
        tipo_classe = "Iris-versicolor"
    
    return tipo_classe

class iris:
    def __init__(self,c1,c2,c3,c4,classe):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.classe = classe

def insere(texto): #transforma um texto de arquivo em lista
    x = 0
    while x < len(texto):
        if texto[x] == "\n":
            local = texto.index(texto[x])
            texto.pop(local)

        else:
            texto[x] = texto[x].split(',')
            x+=1

    # Esse for abaixo aqui é só para tirar o "\n"     
    for i in texto:
        local = texto.index(i) # Local do i em texto
        for b in i:
            local2 = texto[local].index(b) # Local2 do b em i ( local )
            if "\n" in b:
                texto[local][local2] = b.replace("\n",'') # Substitui o valor de acordo com "local" e "local2"

    return texto

def insere_no(): #Insere os conjuntos de teste no example
    global teste
    global examples

    lista1 = []
    lista1 = insere(teste)

    for i in range(0,len(lista1)):
        iris1 = iris(float(lista1[i][0]), float(lista1[i][1]), float(lista1[i][2]), float(lista1[i][3]), lista1[i][4])
        examples.append(iris1)

    return examples


def classifica(ex):
    total = w1*ex.c1 + w2*ex.c2 + w3*ex.c3 + w4*ex.c4 + 1*bias

    if(total < 0):
        return False
    
    return True

def taxa_de_acerto(acert, qnt_test):
    taxa = (acert/qnt_test)*100
    return taxa

def sensibilidade(tp, fn):
    sensi = (tp/(tp+fn))*100
    return sensi

def especificidade(tn, fp):
    esp = (tn/(tn+fp))*100
    return esp

def treinar():
    global w1
    global w2
    global w3
    global w4
    global bias

    examples = insere_no()
    alpha = 0.001
    tipo_classe = escolhe_classe()

    for i in range(100000):
        
        ex = examples[random.randint(0, len(examples)-1)]
        obtido = classifica(ex)

        if(ex.classe == tipo_classe):
            esperado = 1
        else: 
            esperado = 0

        erro = esperado - obtido

        w1 += alpha*erro*ex.c1
        w2 += alpha*erro*ex.c2
        w3 += alpha*erro*ex.c3
        w4 += alpha*erro*ex.c4

        bias += alpha*erro*1

def exibe():

    global validar
    acerto = 0
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    lista3 = []
    
    treinar()
    lista3 = insere(validar)
    tipo_classe = escolhe_classe()

    for i in range(0,len(lista3)):
        iris1 = iris(float(lista3[i][0]), float(lista3[i][1]), float(lista3[i][2]), float(lista3[i][3]), lista3[i][4])
        pertence = classifica(iris1)
        if(pertence):
            if(iris1.classe == tipo_classe):
                tp += 1
                acerto += 1
            else:
                fp += 1
        else:
            if(iris1.classe == tipo_classe):
                fn += 1
            else:
                tn += 1
                acerto += 1


    print('\nPERCEPTRON PARA A CLASSE %s\n' %tipo_classe)
    print('Quantidade de acertos: %d' %acerto)
    print('Quantidade de true positive: %d' %tp)
    print('Quantidade de true negative: %d' %tn)
    print('Quantidade de false positive: %d' %fp)
    print('Quantidade de false negative: %d' %fn)
    print('Taxa de acerto: %d' %taxa_de_acerto(acerto, len(lista3)))
    print('Especificidade: %d' %especificidade(tn,fp))
    print('Sensibilidade: %d\n' %sensibilidade(tp,fn))

exibe()


