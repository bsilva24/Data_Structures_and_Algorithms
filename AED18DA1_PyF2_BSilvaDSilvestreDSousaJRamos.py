#------------------------------------------------------------------------------

"""Inicio de Imports"""

#------------------------------------------------------------------------------

from time import sleep
import pickle
import os.path

#------------------------------------------------------------------------------

"""Fim de Imports"""

#------------------------------------------------------------------------------

"""Inicio de Criação de Classes"""
       
#------------------------------------------------------------------------------

class Queue:   # Definição da classe Queue
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def remove(self, item):
        self.items.remove(item) 
    
    def __repr__(self):
        return str(self.items)
    
#----------------------------------------------------------------------------------------------------------------------------

class Viatura:   # Definição da classe Viatura
    
    def __init__(self,matricula,capacidade):
        self.matricula = matricula
        self.capacidade = capacidade
    
    def __repr__(self):
        return str(self.matricula)
    
#-----------------------------------------------------------------------------------------------------------------------------     

class Camiao(Viatura):   # Definição da subclasse de Viatura Camião
    
    def __init__(self,matricula,capacidade):
        super().__init__(matricula,capacidade)
        
    def __str__(self):
        return self.__class__.__name__ + ' com a matricula ' + str(self.matricula) + ' e capacidade ' + str(self.capacidade)
    
#------------------------------------------------------------------------------

class Automovel(Viatura):   # Definição da subclasse de Viatura Automovel
    
    def __init__(self,matricula,capacidade):
        super().__init__(matricula,capacidade)
    
    def __str__(self):
        return self.__class__.__name__ + ' com a matricula ' + str(self.matricula) + ' e capacidade ' + str(self.capacidade)

#------------------------------------------------------------------------------

class Mota(Viatura):   # Definição da subclasse de Viatura Mota
    
    def __init__(self,matricula,capacidade):
        super().__init__(matricula,capacidade)
    
    def __str__(self):
        return self.__class__.__name__ + ' com a matricula ' + str(self.matricula) + ' e capacidade ' + str(self.capacidade)
                
#------------------------------------------------------------------------------------------------------------------------------------------ 
            
class Condutor:   # Definição da classe Condutor
    
    def __init__(self,numero,nome,telefone,email, veiculo):
        self.numero = numero
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.veiculo = veiculo
     
    def __str__(self):
        return self.__class__.__name__ + ' numero ' + str(self.numero) + ', chamado ' \
            + str(self.nome) + ', telefone ' + str(self.telefone) + ', email ' + str(self.email) + " e motorista de " + str(self.veiculo)
    
    def __repr__(self):
        return str(self.numero)
            
#-------------------------------------------------------------------------------------------------------------------------------------------  

class Cliente:   # Definição da classe Cliente
    
    def __init__(self,numero,nome,morada,telefone,email):    
        self.numero = numero
        self.nome = nome
        self.morada = morada
        self.telefone = telefone
        self.email = email     
    
    def __str__(self):
        return self.__class__.__name__ + ' numero ' + str(self.numero) + ', chamado ' \
            + str(self.nome) + ' residente em ' + str(self.morada) + ', telefone ' + str(self.telefone) + ' e email ' + str(self.email)
    
    def __repr__(self):
        return str(self.numero)
#-----------------------------------------------------------------------------------------------------------------------------------------

class Entrega:   # Definição da classe Entrega
    
    def __init__(self,identificador,ponto_recolha,ponto_entrega,mercadoria_descricao,mercadoria_volume):
        self.identificador = identificador
        self.ponto_recolha = ponto_recolha
        self.ponto_entrega = ponto_entrega
        self.mercadoria_descricao = mercadoria_descricao
        self.mercadoria_volume = mercadoria_volume
    
    def __str__(self):
        return self.__class__.__name__ + ' com o identificador ' + str(self.identificador) + ', ponto de recolha em ' \
            + str(self.ponto_recolha) + ' e ponto de entrega em ' + str(self.ponto_entrega) + '. Descrição da Mercadoria ' \
            + str(self.mercadoria_descricao) + ' e volume da mercadoria ' + str(self.mercadoria_volume)
    
    def __repr__(self):   
        return str(self.identificador)
    

class TreeNode: # Definição da classe TreeNode (Árvore)
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree: # Definição da classe de pesquisa binária na árvore

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False

    def delete(self,key):
      if self.size > 1:
         nodeToRemove = self._get(key,self.root)
         if nodeToRemove:
             self.remove(nodeToRemove)
             self.size = self.size-1
         else:
             raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
      else:
         raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)

    def spliceOut(self):
       if self.isLeaf():
           if self.isLeftChild():
                  self.parent.leftChild = None
           else:
                  self.parent.rightChild = None
       elif self.hasAnyChildren():
           if self.hasLeftChild():
                  if self.isLeftChild():
                     self.parent.leftChild = self.leftChild
                  else:
                     self.parent.rightChild = self.leftChild
                  self.leftChild.parent = self.parent
           else:
                  if self.isLeftChild():
                     self.parent.leftChild = self.rightChild
                  else:
                     self.parent.rightChild = self.rightChild
                  self.rightChild.parent = self.parent

    def findSuccessor(self):
      succ = None
      if self.hasRightChild():
          succ = self.rightChild.findMin()
      else:
          if self.parent:
                 if self.isLeftChild():
                     succ = self.parent
                 else:
                     self.parent.rightChild = None
                     succ = self.parent.findSuccessor()
                     self.parent.rightChild = self
      return succ

    def findMin(self):
      current = self.root
      while current.hasLeftChild():
          current = current.leftChild
      return current

    def remove(self,currentNode):
         if currentNode.isLeaf(): #leaf
           if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
           else:
               currentNode.parent.rightChild = None
         elif currentNode.hasBothChildren(): #interior
           succ = currentNode.findSuccessor()
           succ.spliceOut()
           currentNode.key = succ.key
           currentNode.payload = succ.payload

         else: # this node has one child
           if currentNode.hasLeftChild():
             if currentNode.isLeftChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.leftChild
             elif currentNode.isRightChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.leftChild
             else:
                 currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
           else:
             if currentNode.isLeftChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.rightChild
             elif currentNode.isRightChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.rightChild
             else:
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)
    


class Programa:   #  Definição da classe Programa com o método Main()
        def Main():
            return []
    
    
#-------------------------------------------------------------------------------------------------------------------------------------------    
            
"""Fim da Criação de Classes"""

#-------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

"""Início da Criação de Funções"""

#-------------------------------------------------------------------------------------------------------------------------

"""Funções Gerais"""

#-------------------------------------------------------------------------------------------------------------------------

def error(): # Função de imprimir quando opção introduzia é inválida
    print("\nOpção introduzida inválida!")
    sleep(1)
    print("\nPor favor tente novamente!")
    sleep(1)
    

def printList(list_to_print):   # Função para imprimir as listas
    print("""
    +------------------------------------------------------------------------------------+
    |                  LISTA DE ITEMS                                                    |
    +-------+----------------------------------------------------------------------------+
    | ORDEM |           ITEM DA LISTA                                                    |                           
    +-------+----------------------------------------------------------------------------+""")
    for i in range(0, len(list_to_print)):
        print("       [{}]      {}".format(i+1, list_to_print[i]) + "\n")
      
        
def printQueue(queue_to_print):   # Função para imprimir as filas
    cont = queue_to_print.size()
   
    print("""
    +-----------------------------------------------------------+
    |                  QUEUE DE ITEMS                           |
    +-------+---------------------------------------------------+
    | ORDEM |           ITEM DA FILA                            |                           
    +-------+---------------------------------------------------+""")
    for i in range(0, queue_to_print.size()):
        print("       [{}]       {}".format(cont-i, queue_to_print.items[i]))


def mod_or_back():   # Função para modificar o item e regressar ao menu anterior
    print("""
    +---------------------------------------+
    | Modificar Item....................[1] |
    |                                       |
    | Voltar............................[0] |
    +---------------------------------------+
    """)
    
    
def del_or_back():   # Função para apagar o item e regressar ao menu anterior
    print("""
    +---------------------------------------+
    | Eliminar Item.....................[1] |
    |                                       |
    | Voltar............................[0] |
    +---------------------------------------+
    """)
    
    
def back():   # Função para regressar ao menu anterior
    while True:   
        print("""
    +---------------------------------------+
    | Voltar ao menu anterior...........[0] |
    +---------------------------------------+
        """)
        opt = int(input("Selecione uma opção: "))
        if opt == 0:
            break
        else:
            error()


def fromList(lista_pretendida): #Função para guardar elemento da lista numa variável
    esc = int(input("Selecione um item: "))
    temp = lista_pretendida[esc-1]
    return temp


def removeEnqueue(fromqueue, toqueue, item): # Função para remover um item de uma queue e adicionar a outra queue
    fromqueue.remove(item)
    toqueue.enqueue(item)


def appendEnqueue(listToAppend, queueToEnq, item): # Função para adicionar um item a uma lista e adicioná-lo a outra queue
    listToAppend.append(item)
    queueToEnq.enqueue(item)
    
    
def SerializarListaPkl(listaAutomovel, listaCamiao, listaMota, listaCondutor, listaCliente, listaEntrega): #Função de serialização dos dados em ficheiro binário
    with open('EstafetaListas.pkl','wb') as f: 
        pickle.dump(listaAutomovel,f)
        pickle.dump(listaCamiao,f)
        pickle.dump(listaMota,f)
        pickle.dump(listaCondutor,f)
        pickle.dump(listaCliente,f)
        pickle.dump(listaEntrega,f)
    f.close()


def DesserializarListaPkl(listaAutomovel, listaCamiao, listaMota, listaCondutor, listaCliente, listaEntrega): #Função de desserialização dos dados em ficheiro binário
    pickle_off = open("EstafetaListas.pkl","rb")
    
    automovel = pickle.load(pickle_off)
    for i in range(len(automovel)):
        listaAutomovel.append(automovel[i])
        FAutomovel.enqueue(automovel[i])
        
    camiao = pickle.load(pickle_off)
    for i in range(len(camiao)):
        listaCamiao.append(camiao[i])
        FCamiao.enqueue(camiao[i])
        
    mota = pickle.load(pickle_off)
    for i in range(len(mota)):
        listaMota.append(mota[i])
        FMota.enqueue(mota[i])
    
    condutor = pickle.load(pickle_off)
    for i in range(len(condutor)):
        listaCondutor.append(condutor[i])
        
        if condutor[i].veiculo == "Automóvel":
            FCondAutomovel.enqueue(condutor[i])
        
        elif condutor[i].veiculo == "Camião":
            FCondCamiao.enqueue(condutor[i])
        
        elif condutor[i].veiculo == "Mota":
            FCondMota.enqueue(condutor[i])
    
    cliente = pickle.load(pickle_off)
    for i in range(len(cliente)):
        listaCliente.append(cliente[i])
    
    entrega = pickle.load(pickle_off)
    for i in range(len(entrega)):
        listaEntrega.append(entrega[i])
        
        if 80000 < entrega[i].mercadoria_volume <= 120000:
            FEntregaAutomovel.enqueue(entrega[i])
        
        elif entrega[i].mercadoria_volume > 120000:
            FEntregaCamiao.enqueue(entrega[i])
        
        elif entrega[i].mercadoria_volume <= 80000:
            FEntregaMota.enqueue(entrega[i])

   
    
def abrirTxt(): # Função para abrir um ficheiro de texto guardado das Entregasno diretório do ficheiro .py
    if os.path.isfile('./Entregas.txt') is True:
        nometxt = "Entregas.txt"
        os.startfile(nometxt)
        
        
def GuardarFicheiroTexto(imprimeAutomovel, imprimeCamiao, imprimeMota): #Função de guardar dados da matriz em ficheiro de texto
    ficheirotexto = open("Entregas.txt", "w")
    ficheirotexto.write("+---------------------------------------------------------------------------------------------------+\n")
    ficheirotexto.write("                                     Estafeta – Gestão de Frota")
    ficheirotexto.write("\n+---------------------------------------------------------------------------------------------------+")
    
    for i in range(imprimeAutomovel.size()):
        ficheirotexto.write("\n{} ".format(imprimeAutomovel.items[i]))
    
    
    for i in range(imprimeCamiao.size()):
        ficheirotexto.write("\n{} ".format(imprimeCamiao.items[i]))
   
    
    for i in range(imprimeMota.size()):
        ficheirotexto.write("\n{} ".format(imprimeMota.items[i]))
    ficheirotexto.close()
    
def delItem(queue, lista, item): # Função de eliminar item do programa (remover da lista e remover da queue)
    queue.remove(item)
    lista.remove(item)
    
def pesquisaBinaria(): # Função de execução da pesquisa binária em árvore (BST)

    for i in range(len(listaCliente)):
        cliTree.put(listaCliente[i].nome, listaCliente[i].numero)
        
    nome = str(input("Introduza o nome do(a) cliente que deseja pesquisar [Nome/Apelido]: ").strip().title())
    encontrou = "O(A) cliente com o nome " + nome + " não foi encontrado(a)"
    while cliTree.length() > 0:
        node = cliTree.findMin()
        if node.key == nome:
            encontrou = "\nEncontrou o(a) cliente com o nome " + nome + " e o numero " + str(node.payload)
        cliTree.delete(node.key)
    print(encontrou)      
    
#-------------------------------------------------------------------------------------------------------------------------
"""Funções da Viatura"""

def nova_Viatura(): #Função para criação de nova viatura
    
    matricula = str(input('Matricula do Veículo: '))
    capacidade = int(input('Capacidade de carga: '))
    
    if 80000 < capacidade <= 120000:
        veiculo = Automovel(matricula, capacidade)
        appendEnqueue(listaAutomovel, FAutomovel, veiculo)
        
    elif capacidade <= 80000:
        veiculo = Mota(matricula, capacidade)
        appendEnqueue(listaMota, FMota, veiculo)
        
    elif capacidade > 120000:
        veiculo = Camiao(matricula, capacidade)
        appendEnqueue(listaCamiao, FCamiao, veiculo)
        
        
def modificarViatura_Menu(): #Menu Modificar Viatura
    while True:
        print("""
                        +-----------------------------+
                        |      MODIFICAR VIATURA      |
                        +-----------------------------+
                        |                             |
                        | Automóveis..............[1] |
                        |                             |
                        | Camiões.................[2] |
                        |                             |
                        | Motas...................[3] |
                        |                             |
                        | Voltar..................[0] |
                        |                             |
                        +-----------------------------+
                """)
        
        opt1 = int(input("Insira a opção: "))
        if opt1 == 1:
            selectModificarViatura_Menu(listaAutomovel)
            break
        elif opt1 == 2:
            selectModificarViatura_Menu(listaCamiao)
            break
        elif opt1 == 3:
            selectModificarViatura_Menu(listaMota)
            break
        elif opt1 == 0:
            break        

def subSelectModificarMenu_Lista(alist):
    while True:
        itemEscolhido = fromList(alist)
        print("""
                    +-----------------------------+
                    | VIATURA - MODIFICAR ATRIBUTO|
                    +-----------------------------+
                    |                             |
                    | Matrícula...............[1] |
                    |                             |
                    | Capacidade..............[2] |
                    |                             |
                    | Voltar..................[0] |
                    |                             |
                    +-----------------------------+
            """)
        
        opt2 = int(input("Insira a opção: "))
        
        if opt2 == 1:
            itemEscolhido.matricula = str(input("Insira a nova matrícula: "))
            break
            
            
        elif opt2 == 2:
            while True:
                if itemEscolhido.__class__.__name__ == "Automovel":
                    new = int(input("Insira a nova capacidade: "))
                    if 80000 < new <= 120000:
                       itemEscolhido.capacidade = new
                       break
                   
                    else:
                        error()
                    
                elif itemEscolhido.__class__.__name__ == "Mota":
                    new = int(input("Insira a nova capacidade: "))
                    if  new < 80000:
                       itemEscolhido.capacidade = new
                       break
                   
                    else:
                        error()
                    
    
                elif itemEscolhido.__class__.__name__ == "Camiao":
                    new = int(input("Insira a nova capacidade: "))
                    if  new > 120000:
                       itemEscolhido.capacidade = new
                       break
                   
                    else:
                        error()
            break
    
        elif opt2 == 0:
            break
        
        else:
            error()
        break
    

def selectModificarViatura_Menu(alist): #Menu Modificar Atributo Viatura
    while True:
        printList(alist)
        mod_or_back()
        opc1 = int(input("Selecione uma opção: "))
        if opc1 == 1:
            subSelectModificarMenu_Lista(alist)
            break
        elif opc1 == 0:
            break
#----------------------------------------------------------------------------------------------------------------------------------------------------------------           

"""Funções do Condutor"""

#----------------------------------------------------------------------------------------------------------------------------------------------------------------     
        
def novo_Condutor(): # Função para criar novo condutor
    numero = int(input('Numero do Condutor: '))
    nome = str(input('Nome do Condutor: '))
    telefone = int(input('Telefone: '))
    email = str(input('Email: '))
    veiculo = str(input('Tipo de Veiculo [Mota/Automovel/Camião]:  ').strip().title())
    
    while veiculo != "Camiao" and veiculo != "Camião" and veiculo != "Mota" and veiculo != "Automovel" and veiculo != "Automóvel":
        veiculo = str(input('Tipo de Veiculo [Mota/Automovel/Camião]:  ').strip().title())
    
    condutor = Condutor(numero,nome,telefone,email, veiculo)
    

    if veiculo == "Mota":
        appendEnqueue(listaCondutor, FCondMota, condutor)

    elif veiculo == "Automovel" or "Automóvel":
        appendEnqueue(listaCondutor, FCondAutomovel, condutor)

    elif veiculo == "Camiao" or "Camião":
        appendEnqueue(listaCondutor, FCondCamiao, condutor)
   
    else:
        error()


def modificarCondutor_Menu(): # Função de impressao do menu de modificação do condutor
    while True:
        printList(listaCondutor)
        mod_or_back()
        opt1 = int(input("Insira a opção: "))
        
        if opt1 == 1:
            selectModificarCondutor_Menu()
        elif opt1 == 0:
            break
        else:
            error()

def selectModificarCondutor_Menu(): # Função de impressão do menu de modificação dos atributos do condutor
    while True:
        itemEscolhido = fromList(listaCondutor)
        oldtype = itemEscolhido.veiculo
        print("""
                    +-----------------------------+
                    |CONDUTOR - MODIFICAR ATRIBUTO|
                    +-----------------------------+
                    |                             |
                    | Numero..................[1] |
                    |                             |
                    | Nome....................[2] |
                    |                             |
                    | Telefone................[3] |
                    |                             |
                    | Email...................[4] |
                    |                             |
                    | Veiculo.................[5] |
                    |                             |
                    | Voltar..................[0] |
                    |                             |
                    +-----------------------------+
            """)
        
        opt2 = int(input("Insira a opção: "))
        
        if opt2 == 1:
            itemEscolhido.numero = int(input("Insira o novo número: "))
            break
            
        elif opt2 == 2:
            itemEscolhido.nome = str(input("Insira o novo nome: "))
            break
            
        elif opt2 == 3:
            itemEscolhido.telefone = int(input("Insira o novo número de telefone: "))
            break
            
        elif opt2 == 4:
            itemEscolhido.email = str(input("Insira o novo email: "))
            break
            
        elif opt2 == 5:
            print("""
            +-----------------------------+
            | MODIFICAR VEÍCULO - CONDUTOR|
            +-----------------------------+
            |                             |
            | Automóvel...............[1] |
            |                             |
            | Mota....................[2] |
            |                             |
            | Camião..................[3] |
            |                             |
            | Voltar..................[0] |
            |                             |
            +-----------------------------+
            """)
            novotipo = int(input("Selecione o novo tipo de veículo para o cundutor: "))
            
            
            
            
            if novotipo == 1:
                newtype = "Automóvel"
                itemEscolhido.veiculo = newtype
                
                if oldtype == "Mota":
                    removeEnqueue(FCondMota, FCondAutomovel, itemEscolhido)
                
                elif oldtype == "Camião":
                    removeEnqueue(FCondCamiao, FCondAutomovel, itemEscolhido)
                
            elif novotipo == 2:
                 newtype = "Mota"
                 itemEscolhido.veiculo = newtype
                
                 if oldtype == "Automóvel":
                    removeEnqueue(FCondAutomovel, FCondMota, itemEscolhido)
                
                 elif oldtype == "Camião":
                    removeEnqueue(FCondCamiao, FCondMota, itemEscolhido)
                    
                    
            elif novotipo == 3:
                newtype = "Camião"
                itemEscolhido.veiculo = newtype
                
                if oldtype == "Automóvel":
                    removeEnqueue(FCondAutomovel, FCondCamiao, itemEscolhido)
                
                elif oldtype == "Mota":
                    removeEnqueue(FCondMota, FCondCamiao, itemEscolhido)
            
            
            break
            
        elif opt2 == 0:
            break
        
        else:
           error()
           

#----------------------------------------------------------------------------------------------------------------------------------------------------------------           

"""Funções do Cliente"""

#----------------------------------------------------------------------------------------------------------------------------------------------------------------     
 

def novo_Cliente(): # Função de criação de novo cliente
    numero = int(input('Numero do Cliente: '))
    nome = str(input('Nome do Cliente: ').strip().title())
    morada = str(input('Morada: '))
    telefone = int(input('Telefone: '))
    email = str(input('Email: '))
    
    cliente = Cliente(numero,nome,morada,telefone,email)
    listaCliente.append(cliente)
    cliTree.put(cliente.nome, cliente.numero)
    
def modificarCliente_Menu(): # Função de impressao do menu de modificação do condutor
    while True:
        printList(listaCliente)
        mod_or_back()
        opt1 = int(input("Insira a opção: "))
        
        if opt1 == 1:
            selectModificarCliente_Menu()
            
        elif opt1 == 0:
            break
        else:
            error()    
    
def selectModificarCliente_Menu(): # Função de impressão do menu de modificação dos atributos do cliente
    while True:
        itemEscolhido = fromList(listaCliente)
        print("""
                    +-----------------------------+
                    | CLIENTE - MODIFICAR ATRIBUTO|
                    +-----------------------------+
                    |                             |
                    | Número..................[1] |
                    |                             |
                    | Nome....................[2] |
                    |                             |
                    | Morada..................[3] |
                    |                             |
                    | Telefone................[4] |
                    |                             |
                    | E-mail..................[5] |
                    |                             |
                    | Voltar..................[0] |
                    |                             |
                    +-----------------------------+
            """)
        
        opt = int(input("Insira a opção: "))
        
        if opt == 1:
            itemEscolhido.numero = int(input("Insira novo número de cliente: "))
            break
        elif opt == 2:
            itemEscolhido.nome = str(input("Insira novo nome de cliente: "))
            break
        elif opt == 3:
            itemEscolhido.morada = int(input("Insira nova morada de cliente: "))
            break
        elif opt == 4:
            itemEscolhido.telefone = int(input("Insira novo número de telefone de cliente: "))
            break
        elif opt == 5:
            itemEscolhido.email = int(input("Insira novo e-mail de cliente: "))
            break
        elif opt == 0:
            break
        else:
           error()
           

#----------------------------------------------------------------------------------------------------------------------------------------------------------------           

"""Funções da Entrega"""

#----------------------------------------------------------------------------------------------------------------------------------------------------------------     
 

def nova_Entrega(): # Função de criação de nova entrega
    identificador = int(input('Identificador: '))
    ponto_recolha = str(input('Ponto de recolha: '))
    ponto_entrega = str(input('Ponto de entrega: '))
    mercadoria_descricao = str(input('Descrição da Mercadoria: '))
    mercadoria_volume = int(input('Volume da mercadoria: '))
    
    
    if mercadoria_volume <= 80000:
        entrega = Entrega(identificador,ponto_recolha,ponto_entrega,mercadoria_descricao,mercadoria_volume)
        listaEntrega.append(entrega)
        FEntregaMota.enqueue(entrega)
        
    elif 80000 < mercadoria_volume <= 120000:
        entrega = Entrega(identificador,ponto_recolha,ponto_entrega,mercadoria_descricao,mercadoria_volume)
        listaEntrega.append(entrega)
        FEntregaAutomovel.enqueue(entrega)
        
    elif mercadoria_volume > 120000:
        entrega = Entrega(identificador,ponto_recolha,ponto_entrega,mercadoria_descricao,mercadoria_volume)
        listaEntrega.append(entrega)
        FEntregaCamiao.enqueue(entrega)

def modificarEntrega_Menu():
    while True:
        printList(listaEntrega)
        mod_or_back()
        opt1 = int(input("Insira a opção: "))
        
        if opt1 == 1:
            selectModificarEntrega_Menu()
            
        elif opt1 == 0:
            break
        else:
            error()    
    
def selectModificarEntrega_Menu(): # Função de impressão do menu de modificação dos atributos da entrega
    while True:
        itemEscolhido = fromList(listaEntrega)
        oldVolume = itemEscolhido.mercadoria_volume
        print("""
                    +-----------------------------+
                    | ENTREGA - MODIFICAR ATRIBUTO|
                    +-----------------------------+
                    |                             |
                    | Identificador...........[1] |
                    |                             |
                    | Ponto de Recolha........[2] |
                    |                             |
                    | Ponto de Entrega........[3] |
                    |                             |
                    | Desc. da Mercadoria.....[4] |
                    |                             |
                    | Volume da Mercadoria....[5] |
                    |                             |
                    | Voltar..................[0] |
                    |                             |
                    +-----------------------------+
            """)
        
        opt = int(input("Insira a opção: "))
        
        if opt == 1:
            itemEscolhido.identificador = int(input('Insira o novo identificador: '))
            break
        elif opt == 2:
            itemEscolhido.ponto_recolha = str(input('Insira o novo ponto de recolha: '))
            break
        elif opt == 3:
            itemEscolhido.ponto_entrega = str(input('Insira o novo ponto de entrega: '))
            break
        elif opt == 4:
            itemEscolhido.mercadoria_descricao = str(input('Insira a nova descrição de mercadoria: '))
            break
        elif opt == 5:
            newVolume = int(input('Insira o novo volume da mercadoria: '))
            itemEscolhido.mercadoria_volume = newVolume
            
            
            if oldVolume <= 80000:
                
                if 80000 < newVolume <= 120000:
                    removeEnqueue(FEntregaMota, FEntregaAutomovel, itemEscolhido)
                
                elif newVolume > 120000:
                    removeEnqueue(FEntregaMota, FEntregaCamiao, itemEscolhido)
        
        
            elif 80000 < oldVolume <= 120000:
            
                if newVolume <= 80000:
                    removeEnqueue(FEntregaAutomovel, FEntregaMota, itemEscolhido)
                
                elif newVolume > 120000:
                    removeEnqueue(FEntregaAutomovel, FEntregaCamiao, itemEscolhido)
            
            
            elif oldVolume > 120000:
                if newVolume <= 80000:
                    removeEnqueue(FEntregaCamiao, FEntregaMota, itemEscolhido)
                
                elif 80000 < newVolume <= 120000:
                    removeEnqueue(FEntregaCamiao, FEntregaAutomovel, itemEscolhido)
            
            else:
                error()
            break
        
        elif opt == 0:
            break
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
 
"""Funções de Criação dos menus"""
               
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def delete_Menu(): # Função de impressão do menu de eliminar um item
    while True:
            print("""
                        +-----------------------------+
                        |        ELIMINAR ITEM        |
                        +-----------------------------+
                        |                             |
                        | Viatura.................[1] |
                        |                             |
                        | Condutor................[2] |
                        |                             |
                        | Cliente.................[3] |
                        |                             |
                        | Entrega.................[4] |
                        |                             |
                        | Voltar..................[0] |
                        |                             |
                        +-----------------------------+
            """)
            opc = int(input("Selecione uma opção: "))
            if opc == 1:
                deleteViatura_Menu()
            elif opc == 2:
                deleteCondutor_Menu()
            elif opc == 3:
                deleteCliente_Menu()
                
            elif opc == 4:
                deleteEntrega_Menu()

            elif opc == 0:
                break
            else:
                error()


def deleteViatura_Menu(): #Menu de eliminação da viatura
    while True:
        print("""
                        +-----------------------------+
                        |      ELIMINAR VIATURA       |
                        +-----------------------------+
                        |                             |
                        | Automóvel...............[1] |
                        |                             |
                        | Camião..................[2] |
                        |                             |
                        | Mota....................[3] |
                        |                             |
                        | Voltar..................[0] |
                        |                             |
                        +-----------------------------+
                """)
        
        opt1 = int(input("Insira a opção: "))
        if opt1 == 1:
            while True:
                printList(listaAutomovel)
                del_or_back()
                opt2 = int(input("Selecione uma opção: "))
                
                if opt2 == 1:
                    item = fromList(listaAutomovel)
                    delItem(FAutomovel, listaAutomovel, item)
                    break
                
                elif opt2 == 0:
                    break
            
            
        elif opt1 == 2:
            while True:
                printList(listaCamiao)
                del_or_back()
                opt2 = int(input("Selecione uma opção: "))
                if opt2 == 1:
                    item = fromList(listaCamiao)
                    delItem(FCamiao, listaCamiao, item)
                elif opt2 == 0:
                    break
            
            
        elif opt1 == 3:
            while True:
                printList(listaMota)
                del_or_back()
                opt2 = int(input("Selecione uma opção: "))                
                if opt2 == 1:
                    item = fromList(listaMota)
                    delItem(FMota, listaMota, item)
                elif opt2 == 0:
                    break
        
        
        elif opt1 == 0:
                break
        
        else:
            error()

def deleteCliente_Menu(): # Função de impressão do menu de eliminar condutor
    while True:
        printList(listaCliente)
        del_or_back()
        opt = int(input("Selecione uma opção: "))
        
        if opt == 1:
            item = fromList(listaCliente)
            listaCliente.remove(item)
       
        elif opt == 0:
            break
        
        else:
            error()

def deleteCondutor_Menu(): # Função de impressão do menu de eliminar condutor
    while True:
        printList(listaCondutor)
        del_or_back()
        opt = int(input("Selecione uma opção: "))
        
        if opt == 1:
            item = fromList(listaCondutor)
            
            if item.veiculo == "Automóvel":
                delItem(FCondAutomovel, listaCondutor, item)
            elif item.veiculo == "Mota":
                delItem(FCondMota, listaCondutor, item)
            elif item.veiculo == "Camião":
                delItem(FCondCamiao, listaCondutor, item)
       
        elif opt == 0:
            break
        
        else:
            error()

def deleteEntrega_Menu(): # Função de impressão do menu de eliminar entrega
    while True:
        printList(listaEntrega)
        del_or_back()
        opt = int(input("Selecione uma opção: "))
        
        if opt == 1:
            item = fromList(listaEntrega)
            if 80000 < item.mercadoria_volume <= 120000:
                delItem(FEntregaAutomovel, listaEntrega, item)
                
            elif item.mercadoria_volume > 120000:
                delItem(FEntregaCamiao, listaEntrega, item)
            
            elif item.mercadoria_volume <= 80000:
                delItem(FEntregaMota, listaEntrega, item)
        
        elif opt == 0:
            break
    
        else:
            error()
            
def menu_Inicial(): # Função de impressão do primeiro menu do programa
    print("""
                    
    
    +-------------------------------------------------------------------+
    |                                                                   |
    |      ----+  ----+  ----+  ----+  ----+  ----+  ----+  ----+ ®     |
    | ✪   |___   |___     |    |___|  |___   |___     |    |___|    ✪ |
    |      |___   ____|    |    |   |  |      |___     |    |   |       |
    |                                                                   |
    +-------------------------------------------------------------------+
           
                 +-------------------------------------------+                        
                 |                                           |
                 | Utilizar Dados Existentes.............[1] |
                 |                                           |
                 | Criar Novos Dados.....................[2] |
                 |                                           |
                 | Fechar Programa.......................[0] |
                 |                                           |
                 +-------------------------------------------+
            
            """)
    

    opc = int(input("Selecione uma opção: "))
    while True:
        if opc == 1:
            if os.path.isfile('./EstafetaListas.pkl') is False: #inicio ondição de verificação da existencia de um ficheiro binário com os dados das startups
                cam1 = Camiao("AB-CD-01", 130000)
                cam2 = Camiao("EF-GH-02", 140000)
                listaCamiao.extend([cam1, cam2])
                FCamiao.enqueue(cam1)
                FCamiao.enqueue(cam2)
                
                aut1 = Automovel("HI-JK-03", 90000)
                aut2 = Automovel("LM-NO-04", 100000)
                listaAutomovel.extend([aut1, aut2])
                FAutomovel.enqueue(aut1)
                FAutomovel.enqueue(aut2)
                
                mot1 = Mota("PQ-RS-05", 70000)
                mot2 = Mota("TU-VX-06", 60000)
                listaMota.extend([mot1, mot2])
                FMota.enqueue(mot1)
                FMota.enqueue(mot2)
                
                condCam1 = Condutor(1234, "José Santos", 963692581, "jsantos@gmail.com", "Camião")
                condCam2 = Condutor(5678, "Manuel Silva", 912581473, "msilva@gmail.com", "Camião")
                condAut1 = Condutor(9876, "Diogo Sousa", 926548732, "dsousa@gmail.com", "Automóvel")
                condAut2 = Condutor(5432, "Daniel Silvestre", 964598764, "dsilvestre@gmail.com", "Automóvel")
                condMot1 = Condutor(2457, "Bruno Silva", 912582563, "bsilva@gmail.com", "Mota")
                condMot2 = Condutor(8521, "João Ramos", 912581473, "jramos@gmail.com", "Mota")
                listaCondutor.extend([condCam1, condCam2, condAut1, condAut2, condMot1, condMot2, ])
                FCondCamiao.enqueue(condCam1)
                FCondCamiao.enqueue(condCam2)
                FCondAutomovel.enqueue(condAut1)
                FCondAutomovel.enqueue(condAut2)
                FCondMota.enqueue(condMot1)
                FCondMota.enqueue(condMot2)
                
                cli1 = Cliente(9637, "Paulo Neves", "Rua das Flores N.56 1D, 1500-000 Lisboa", 210258142, "pneves@gmail.com")
                cli2 = Cliente(1587, "Maria Antunes", "Rua Certa, 1500-500 Lisboa", 217894561, "mantunes@gmail.com")
                listaCliente.extend([cli1, cli2])
                cliTree.put(cli1.nome, cli1.numero)
                cliTree.put(cli2.nome, cli2.numero)
                
                
                ent1 = Entrega(525, "Loja", "Morada do Cliente", "Livros", 30000)
                ent2 = Entrega(242, "Fábrica", "Morada do Cliente", "Mobiliário", 130000)
                ent3 = Entrega(118, "Centro de Recolha", "Morada do Cliente", "Material Informático", 100000)
                listaEntrega.extend([ent1, ent2, ent3])
                FEntregaMota.enqueue(ent1)
                FEntregaCamiao.enqueue(ent2)
                FEntregaAutomovel.enqueue(ent3)
                
            else:
                DesserializarListaPkl(listaAutomovel, listaCamiao, listaMota, listaCondutor, listaCliente, listaEntrega)
            sleep(1)
            main_Menu()
            break
        elif opc == 2:
            main_Menu()
            break
        elif opc == 0:
            print("Obrigado pela visita! Volte Sempre.")
            sleep(1)
            break            

def main_Menu(): # Função de impressão do menu principal do programa
    while True:
            print("""
                        +------------------------------
                        | .-*-.-*-.-ESTAFETA-.-*-.-*-.|
                        +-----------------------------+                    
                        |       GESTÃO DE FROTA       |
                        +-----------------------------+
                        |                             |
                        | Visualizar..............[1] |
                        |                             |
                        | Adicionar...............[2] |
                        |                             |
                        | Modificar...............[3] |
                        |                             |
                        | Eliminar................[4] |
                        |                             |
                        | Fechar Programa.........[5] |
                        |                             |
                        +-----------------------------+
                    """)
    
            opc = int(input("Selecione uma opção: "))
            if opc == 1:
                visualizar_Menu()
            elif opc == 2:
                adicionar_Menu()
            elif opc == 3:
                modificar_Menu()
            elif opc == 4:
                delete_Menu()
            elif opc == 5:
                while True:
                   print("""
                  +------------------------------------------+
                  |                                          |
                  | Sair e Guardar.......................[1] |
                  |                                          |
                  | Sair Sem Guardar.....................[2] |
                  |                                          |
                  | Voltar...............................[0] |
                  |                                          |
                  +------------------------------------------+
                """) 
                   opc2 = int(input("Selecione uma opção: "))
                   if opc2 == 1:
                     SerializarListaPkl(listaAutomovel, listaCamiao, listaMota, listaCondutor, listaCliente, listaEntrega)
                     sleep(1)
                     print("Obrigado pela visita! Volte Sempre.")
                     break
                   elif opc2 == 2:
                       sleep(1)
                       print("Obrigado pela visita! Volte Sempre.")
                       break
                   elif opc2 == 0:
                       break
                   else:
                       error()

                if opc2 == 1 or opc2 == 2:
                    break
            else:
               error()


def visualizar_Menu(): # Função de impressão do menu de vizualização
    while True:
            print("""
                        +-----------------------------+
                        |         VISUALIZAR          |
                        +-----------------------------+
                        |                             |
                        | Listas..................[1] |
                        |                             |
                        | Filas...................[2] |
                        |                             |
                        | Pesquisar Cliente.......[3] |
                        |                             |
                        | Voltar..................[0] |
                        |                             |
                        +-----------------------------+
            """)
            
            opc = int(input("Selecione uma opção: "))
            if opc == 1:
                visualizarListas_Menu()
            elif opc == 2:
                visualizarFilas_Menu()
            elif opc == 3:
                pesquisaBinaria()
            elif opc == 0:
                break
            else:
                error()

def visualizarListas_Menu(): # Função de impressão do menu de vizualização de listas
    while True:
            print("""
                        +-----------------------------+
                        |      VISUALIZAR LISTAS      |
                        +-----------------------------+
                        |                             |
                        | Automóveis..............[1] |
                        |                             |
                        | Camiões.................[2] |
                        |                             |
                        | Motas...................[3] |
                        |                             |
                        | Condutores..............[4] |
                        |                             |
                        | Clientes................[5] |
                        |                             |
                        | Entregas................[6] |
                        |                             |
                        | Voltar..................[0] |
                        |                             |
                        +-----------------------------+
            """)
            opc= int(input("Selecione uma opção: "))
            if opc == 1:
                while True:
                    printList(listaAutomovel)
                    mod_or_back()
                    opc2 = int(input("Selecione uma opção: "))
                    if opc2 == 1:
                       subSelectModificarMenu_Lista(listaAutomovel)
                    elif opc2 == 0:
                        break
                    else:
                        error()
                    
            elif opc == 2:
                while True:
                    printList(listaCamiao)
                    mod_or_back()
                    opc2 = int(input("Selecione uma opção: "))
                    if opc2 == 1:
                        subSelectModificarMenu_Lista(listaCamiao)
                    elif opc2 == 0:
                        break
                    else:
                        error()
            elif opc == 3:
                while True:
                    printList(listaMota)
                    mod_or_back()
                    opc2 = int(input("Selecione uma opção: "))
                    if opc2 == 1:
                        subSelectModificarMenu_Lista(listaMota)
                    elif opc2 == 0:
                        break
                    else:
                        error()
            elif opc == 4:
                while True:
                    printList(listaCondutor)
                    mod_or_back()
                    opc2 = int(input("Selecione uma opção: "))
                    if opc2 == 1:
                        selectModificarCondutor_Menu()
                    elif opc2 == 0:
                        break
                    else:
                        error()
            elif opc == 5:
                while True:
                    printList(listaCliente)
                    mod_or_back()
                    opc2 = int(input("Selecione uma opção: "))
                    if opc2 == 1:
                        selectModificarCliente_Menu()
                    elif opc2 == 0:
                        break
                    else:
                        error()
            elif opc == 6:
                while True:
                    printList(listaEntrega)
                    mod_or_back()
                    opc2 = int(input("Selecione uma opção: "))
                    if opc2 == 1:
                        selectModificarEntrega_Menu()
                    
                    elif opc2 == 0:
                        break
                    
                    else:
                        error()
            elif opc == 0:
                break
            else:
                error()

def visualizarFilas_Menu(): # Função de impressão do menu de vizualização de filas
    while True:
        print("""
                        +-----------------------------+
                        |      VISUALIZAR FILAS       |
                        +-----------------------------+
                        |                             |
                        | Automóveis..............[1] |
                        |                             |
                        | Camiões.................[2] |
                        |                             |
                        | Motas...................[3] |
                        |                             |
                        | Condutores..............[4] |
                        |                             |
                        | Entregas................[5] |
                        |                             |
                        | Voltar..................[0] |
                        |                             |
                        +-----------------------------+
            """)
        
        opc= int(input("Selecione uma opção: "))
        if opc == 1:
            printQueue(FAutomovel)
            back()
        elif opc == 2:
            printQueue(FCamiao)
            back()
        elif opc == 3:
            printQueue(FMota)
            back()
        elif opc == 4:
            visualizarFilasCondutor_Menu()
        elif opc == 5:
            visualizarFilasEntrega_Menu()
        elif opc == 0:
            break
        else:
            error()
                
def visualizarFilasCondutor_Menu(): # Função de impressão do menu de vizualização de filas do condutor        
    while True:
        print("""
                        +-----------------------------+
                        |  VISUALIZAR FILAS CONDUTOR  |
                        +-----------------------------+
                        |                             |
                        | Automóveis..............[1] |
                        |                             |
                        | Camiões.................[2] |
                        |                             |
                        | Motas...................[3] |
                        |                             |
                        | Voltar..................[0] |
                        |                             |
                        +-----------------------------+
            """)
        opc = int(input("Selecione uma opção: "))
        if opc == 1:
            printQueue(FCondAutomovel)
            back()
        elif opc == 2:
            printQueue(FCondCamiao)
            back()
        elif opc == 3:
            printQueue(FCondMota)
            back()
        elif opc == 0:
            break
        else:
            error()
            
def visualizarFilasEntrega_Menu(): # Função de impressão do menu de vizualização de filas das entregas
    while True:
        print("""
                        +-----------------------------+
                        |  VISUALIZAR FILAS ENTREGA   |
                        +-----------------------------+
                        |                             |
                        | Automóveis..............[1] |
                        |                             |
                        | Camiões.................[2] |
                        |                             |
                        | Motas...................[3] |
                        |                             |
                        | Ver Ficheiro Filas......[4] |            
                        |                             |
                        | Voltar..................[0] |
                        |                             |
                        +-----------------------------+
            """)
        
        opc= int(input("Selecione uma opção: "))
        if opc == 1:
            printQueue(FEntregaAutomovel)
            back()
        elif opc == 2:
            printQueue(FEntregaCamiao)
            back()
        elif opc == 3:
            printQueue(FEntregaMota)
            back()
        elif opc == 4:
            GuardarFicheiroTexto(FEntregaAutomovel, FEntregaCamiao, FEntregaMota)
            abrirTxt()
        elif opc == 0:
            break
        else:
            error()
                


def adicionar_Menu(): # Função de impressão do menu de adição de um novo item
    while True:
        print("""
                       +------------------------------+
                       |          ADICIONAR           |
                       +------------------------------+
                       |                              |
                       | Viatura..................[1] |
                       |                              |
                       | Condutor.................[2] |
                       |                              |
                       | Cliente..................[3] |
                       |                              |
                       | Entrega..................[4] |
                       |                              |
                       | Voltar...................[0] |
                       |                              |
                       +------------------------------+
        """)
        opc= int(input("Selecione uma opção: "))
        if opc == 1:
            nova_Viatura()
            sleep(1)
            print("\nViatura adicionada com sucesso!\n")
            sleep(1)
            break
        elif opc == 2:
            novo_Condutor()
            sleep(1)
            print("\nCondutor adicionado com sucesso!\n")
            sleep(1)
            break
        elif opc == 3:
            novo_Cliente()
            sleep(1)
            print("\nCliente adicionado com sucesso!\n")
            sleep(1)
            break
        elif opc == 4:
            nova_Entrega()
            GuardarFicheiroTexto(FEntregaAutomovel, FEntregaCamiao, FEntregaMota)
            sleep(1)
            print("\nEntrega adicionada com sucesso!\n")
            sleep(1)
            break
        elif opc == 0:
            break
        else:
            error()


def modificar_Menu(): # Função de impressão do menu de modificação
    while True:
        print("""
                        +-----------------------------+
                        |          MODIFICAR          |
                        +-----------------------------+
                        |                             |
                        | Viatura.................[1] |
                        |                             |
                        | Condutor................[2] |
                        |                             |
                        | Cliente.................[3] |
                        |                             |
                        | Entrega.................[4] |
                        |                             |
                        | Voltar..................[0] |
                        |                             |
                        +-----------------------------+
        """)
        opc= int(input("Selecione uma opção: "))
        if opc == 1:
            modificarViatura_Menu()
        elif opc == 2:
            modificarCondutor_Menu()
        elif opc == 3:
            modificarCliente_Menu()
        elif opc == 4:
            modificarEntrega_Menu()
        elif opc == 0:
            break
        else:
            error()


 
    
    
if __name__ == "__main__":
     
    listaAutomovel = Programa.Main()
    listaCamiao = Programa.Main()
    listaMota = Programa.Main()                # Criação das listas através da classe Programa com método Main()
    listaCondutor = Programa.Main()
    listaCliente = Programa.Main()
    listaEntrega = Programa.Main()
    
    
    FCamiao = Queue()
    FAutomovel = Queue()                       
    FMota = Queue()
    
    FCondCamiao = Queue()
    FCondAutomovel = Queue()                   # Criação das filas através da classe Queue()
    FCondMota = Queue()
    
    FEntregaCamiao = Queue()
    FEntregaAutomovel = Queue()
    FEntregaMota = Queue()
    
    cliTree = BinarySearchTree()              # Criação de Binary Search Tree
    
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    """Execução do Programa Estafetas"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------   
    
    menu_Inicial()                            # Função para execução total do programa (arranque)
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------