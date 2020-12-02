examples = []
teste = []
tamanho = 0
tipo = 0

#importando do txt - tem que ta na mesma pasta
f = open('/Users/Bianca Morais/Google Drive/Engenharia de Computação/11º Período/Sistemas Inteligentes/3ª Unidade/trabalho/conjunto_teste.txt', 'r')
teste = f.readlines()
k = open('/Users/Bianca Morais/Google Drive/Engenharia de Computação/11º Período/Sistemas Inteligentes/3ª Unidade/trabalho/validar.txt', 'r')
validar = k.readlines()
tamanho = int(input('Insira o quantidade K vizinhos: '))
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
    def __init__(self, comp_sepala, larg_sepala, comp_petala, larg_petala, classe, dist):
        self.comp_sepala = comp_sepala
        self.larg_sepala = larg_sepala
        self.comp_petala = comp_petala
        self.larg_petala = larg_petala
        self.classe = classe
        self.dist = dist

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
        iris1 = iris(float(lista1[i][0]), float(lista1[i][1]), float(lista1[i][2]), float(lista1[i][3]), lista1[i][4], 0)
        examples.append(iris1)

    return examples

def atualiza_distancia(ex):
    global examples
    for x in examples:
        dist = (x.comp_sepala - ex.comp_sepala)*(x.comp_sepala - ex.comp_sepala)
        dist = dist + (x.comp_petala - ex.comp_petala)*(x.comp_petala - ex.comp_petala)
        dist = dist + (x.larg_petala - ex.larg_petala)*(x.larg_petala - ex.larg_petala)
        dist = dist + (x.larg_sepala- ex.larg_sepala)*(x.larg_sepala- ex.larg_sepala)
        x.dist = dist

def taxa_de_acerto(acert, qnt_test):
    taxa = ((acert/qnt_test)*100)
    return taxa

def sensibilidade(tp, fn):
    sensi = (tp/(tp+fn))*100
    return sensi

def especificidade(tn, fp):
    esp = (tn/(tn+fp))*100
    return esp

def classificar(ex):
    global examples
    aux = 0
    aux2 = 0
    global tamanho

    tipo_classe = escolhe_classe()

    atualiza_distancia(ex) #atualiza a distância desse exemplo de validação
    examples.sort(key = lambda s: (s.dist)) #ordena de acordo com ele

    for i in range(0, tamanho): #visita os K vizinhos mais proximos
        if(examples[i].classe == tipo_classe):
            aux += 1
        else:
            aux2 +=1
    
    if(aux>aux2):
        return True
    else:
        return False

def exibe():

    global validar
    acerto = 0
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    lista3 = []
    global tamanho
    examples = insere_no()
    lista3 = insere(validar)
    tipo_classe = escolhe_classe()
    
    for i in range(0,len(lista3)):
        iris1 = iris(float(lista3[i][0]), float(lista3[i][1]), float(lista3[i][2]), float(lista3[i][3]), lista3[i][4], 0)
        pertence = classificar(iris1)
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


    print('\nKNN PARA CLASSE %s\n' %tipo_classe)
    print('Quantidade de K vizinhos: %d' %tamanho)
    print('Quantidade de acertos: %d' %acerto)
    print('Quantidade de true positive: %d' %tp)
    print('Quantidade de true negative: %d' %tn)
    print('Quantidade de false positive: %d' %fp)
    print('Quantidade de false negative: %d' %fn)
    print('Taxa de acerto: %d' %taxa_de_acerto(acerto, len(lista3)))
    print('Especificidade: %d' %especificidade(tn,fp))
    print('Sensibilidade: %d\n' %sensibilidade(tp,fn))

exibe()