import time
import random

#Classe Nodo de uma estrutura duplamente encadeada(usado na fila)
class Nodo:
    def __init__(self, dado=0,proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    #Printa o nodo e seu proximo
    def __repr__(self):
        return '%s -> %s' %(self.dado,self.proximo)

#Classe Nodo de uma estrutura duplamente encadeada(usado na pilha)
class Nodo2:
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)

#Fila usando estrutura encadeada
class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        
    #Printa a fila, repr retorna a representação como string
    def __repr__(self):
        return "[" + str(self.primeiro) + "]"
    
    #Método inserir, insere no final por ser uma fila
    def insere(self, novo_dado):
        
        #Criação de um novo nodo com um dado para ser armazenado
        novo_nodo = Nodo(novo_dado)
        
        #Se a fila estiver vazia, insere
        if self.primeiro == None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            #Define o nodo novo como o ultimo elemento da fila
            self.ultimo.proximo = novo_nodo
            #Define que o último elemento da fila aponte para o novo nodo
            self.ultimo = novo_nodo
            
    #Método remover, remove no início por ser uma fila
    def remove(self):
        assert self.primeiro != None, "Rua já está vazia."
        self.primeiro = self.primeiro.proximo
        if self.primeiro == None:
            self.ultimo = None

#Pilha usando estrutura encadeada
class Pilha:
    def __init__(self):
        self.topo = None
    #Imprime a pilha numa representação de string
    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def insere(self, novo_dado):
        
        # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo2(novo_dado)
        
        # Faz com que o novo nodo seja o topo da pilha.
        novo_nodo.anterior = self.topo
        
        # Faz com que a cabeça da lista referencie o novo nodo.
        self.topo = novo_nodo
       

    def remove(self):

        assert self.topo, "Impossível remover valor de pilha vazia."

        self.topo = self.topo.anterior

#Cria uma fila
pista1 = Fila()
pista2 = Fila()

#Distribuição de 10 carros de maneira aleatória entra as pistas 1 e 2
for i in range(10):
    x=random.randint(1,2)
            
    if x==1:
        pista1.insere(f"\033[1;96mcarro {i+1}\033[1;96m")
        print(f"\033[0;0mCarro {i+1} entrando na pista {x}:	\033[0;0m {pista1}")
        time.sleep(random.randint(1,5)) #Tempo aleatório de 0 a 5 segundos para os carros entrarem nas pistas
            
    else:
        pista2.insere(f"\033[1;95mcarro {i+1}\033[1;95m")
        print(f"\033[0;0mCarro {i+1} entrando na pista {x}:	\033[0;0m {pista2}")
        time.sleep(random.randint(1,5))
    
print('\n')  

#While "master", condição que faz os semáforos 1 e 2 funcionarem até que ambas as filas estejam vazias
while True: 
    sinal1=True
    sinal2=True
    
    count = 0
    while sinal1: #Semáforo pista 1

        if count < 5: #condição menor que 5 conta os 10 segundos com o sinal verde, pois para os carros saírem leva-se 2 segundos cada. 
        #Sendo assim, é permitido apenas 5 carros saírem da fila a cada vez que o sinal abre já que 2*5=10.
            print("\033[42;1m--green light on (Semáforo 1)--\033[0m")
            if pista1.primeiro != None: #condição que verifica se a pista1 está vazia, se não, o primeiro da fila é liberado.
                time.sleep(2)
                pista1.remove()
                print(f"Carro saiu da pista 1: {pista1}")
                
        elif count < 10: #condição que representa o sinal vermelho
            print("\n\033[41;1m--red light on (Semáforo 1)--\033\n[0m")
            break #caso true, o brake indica que o sinal2 foi aberto e este foi fechado.
        
        time.sleep(1) #tempo para visualização no terminal.
        count += 1 #incrementa-se o contador.
        
    count = 0    
    while sinal2: #Semáforo pista 2
            
        if count < 5: #condição menor que 5 conta os 10 segundos com o sinal verde, pois para os carros saírem leva-se 2 segundos cada. 
        #Sendo assim, é permitido apenas 5 carros saírem da fila a cada vez que o sinal abre já que 2*5=10.
            print("\033[42;1m--green light on (Semáforo 2)--\033[0m")
            if pista2.primeiro != None: #condição que verifica se a pista2 está vazia, se não, o primeiro da fila é liberado.
                time.sleep(2)
                pista2.remove()
                print(f"Carro saiu da pista 2: {pista2}")
        
        elif count < 10: #condição que representa o sinal vermelho
            print("\n\033[41;1m--red light on (Semáforo 2)--\033\n[0m")
            break #caso true, o brake indica que o sinal1 foi aberto e este foi fechado
        
        time.sleep(1) #tempo para visualização no terminal
        count += 1 #incremetando o contador
    
    if pista1.primeiro == None: #após o break do sinal2 o interpretador afere com o IF se ambas as pistas estão vazias
        if pista2.primeiro == None:
            print("\033[1;33m--Todos os carros foram em direção ao estacionamento--\n\033[1;33m")
            break #break que encerra o While "master", indicando que todos os carros saíram em direção ao estacionamento.

#Cria Pilha
estacionamento = Pilha()

#Insere os carros no estacionamento,vale ressaltar que independente do nº do mesmo no estacionameto, aqui esse é estabelecido de acordo com a ordem de chegada.
for i in range(5):
    estacionamento.insere(f"\033[1;34mcarro {i+1}\033[1;34m")
    print(f"\033[0;0mCarro {i+1} entrando no estacionamento: \033[0;0m{estacionamento}")
    time.sleep(2)
    
print('\n')

print("\033[1;33m--O estacionamento está lotado.--\n\033[1;33m")
print(estacionamento)

#Diz qual dos carros sera removido aleatoriamente
y=random.randint(1,5)
print(f"\033[0;0mO carro a ser removido é o carro\033[0;0m {y}\n")

#Remove o conjunto de carros e os devolve a pista 1 de acordo com o valor aleatorio gerado
if(y == 1):
    print("Os carros a serem removidos antes do carro 1 são [carro2 -> carro3 -> carro4 -> carro5].")
    for i in range(5):
        estacionamento.remove()
        time.sleep(2)
        pista1.insere(f"\033[1;96mcarro {i+1}\033[1;96m")
        print(f"\033[0;0mCarro {i+1} voltou para a pista 1:\033[0;0m {pista1}")

elif(y == 2):
    print("Os carros a serem removidos antes do carro 2 são [carro3 -> carro4 -> carro5].")
    for i in range(4):
        estacionamento.remove()
        time.sleep(2)
        pista1.insere(f"\033[1;96mcarro {i+3}\033[1;96m")
        print(f"\033[0;0mCarro {i+3} voltou para a pista 1:\033[0;0m {pista1}")

elif(y == 3):
    print("Os carros a serem removidos antes do carro 3 são [carro4 -> carro5].")
    for i in range(3):
        estacionamento.remove()
        time.sleep(2)
        pista1.insere(f"\033[1;96mcarro {5-i}\033[1;96m")
        print(f"\033[0;0mCarro {5-i} voltou para a pista 1:\033[0;0m {pista1}")

elif(y == 4):
    print("O carro a ser removido antes do carro 4 é o [carro5].")
    for i in range(2):
        estacionamento.remove()
        time.sleep(2)
        pista1.insere(f"\033[1;96mcarro {5-i}\033[1;96m")
        print(f"\033[0;0mCarro {5-i} voltou para a pista 1:\033[0;0m {pista1}")

else:
    print("O carro 5 é o último então pode sair direto.")
    estacionamento.remove()
    time.sleep(2)
    pista1.insere(f"\033[1;96mcarro {5}\033[1;96m")
    print(f"\033[0;0mCarro {5} voltou para a pista 1:\033[0;0m {pista1}")

