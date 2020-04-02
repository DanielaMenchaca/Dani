#!/usr/bin/env python
# coding: utf-8

# # L01 

# In[1]:


import random


# In[ ]:





# In[2]:


class Celda:
    
    def __init__(self, m,n):
        self.m = m
        self.n = n
        self.ninos_sin_prob = [] 
        self.ninos_prob_card =[]
        self.ninos_prob_resp = []
        self.ninos_ambos_prob = []
        self.adultos_sin_prob = [] 
        self.adultos_prob_card =[]
        self.adultos_prob_resp = []
        self.adultos_ambos_prob = []
        self.ancianos_sin_prob = [] 
        self.ancianos_prob_card =[]
        self.ancianos_prob_resp = []
        self.ancianos_ambos_prob = []
        self.ninos_sin_prob_sanos = [] 
        self.ninos_prob_card_sanos =[]
        self.ninos_prob_resp_sanos = []
        self.ninos_ambos_prob_sanos = []
        self.adultos_sin_prob_sanos = [] 
        self.adultos_prob_card_sanos =[]
        self.adultos_prob_resp_sanos = []
        self.adultos_ambos_prob_sanos = []
        self.ancianos_sin_prob_sanos = [] 
        self.ancianos_prob_card_sanos =[]
        self.ancianos_prob_resp_sanos = []
        self.ancianos_ambos_prob_sanos = []
        self.ninos_sin_prob_influenza = [] 
        self.ninos_prob_card_influenza =[]
        self.ninos_prob_resp_influenza = []
        self.ninos_ambos_prob_influenza = []
        self.adultos_sin_prob_influenza = [] 
        self.adultos_prob_card_influenza =[]
        self.adultos_prob_resp_influenza = []
        self.adultos_ambos_prob_influenza = []
        self.ancianos_sin_prob_influenza = [] 
        self.ancianos_prob_card_influenza =[]
        self.ancianos_prob_resp_influenza = []
        self.ancianos_ambos_prob_influenza = []
        self.ninos_sin_prob_coronavirus = [] 
        self.ninos_prob_card_coronavirus =[]
        self.ninos_prob_resp_coronavirus = []
        self.ninos_ambos_prob_coronavirus = []
        self.adultos_sin_prob_coronavirus = [] 
        self.adultos_prob_card_coronavirus =[]
        self.adultos_prob_resp_coronavirus = []
        self.adultos_ambos_prob_coronavirus = []
        self.ancianos_sin_prob_coronavirus = [] 
        self.ancianos_prob_card_coronavirus =[]
        self.ancianos_prob_resp_coronavirus = []
        self.ancianos_ambos_prob_coronavirus = []
        self.casos_influenza = 0
        self.casos_corona = 0
        self.casos_vacuna = 0

   # esta función calcula todos los casos posibles del total de la ciudad que serán necesarios para guardar 
#la ciudad al finalizar cada día 

    def casos_categoria(self):       
        for persona in self.ninos_sin_prob:
            if persona.influenza == True:
                self.ninos_sin_prob_influenza.append(persona)
            if persona.corona == True:
                self.ninos_sin_prob_coronavirus.append(persona)
            if persona.influenza == False and persona.corona == False:
                self.ninos_sin_prob_sanos.append(persona)
            
        
        for persona in self.ninos_prob_card:
            if persona.influenza == True: 
                self.ninos_prob_card_influenza.append(persona)                
            if persona.influenza == False and persona.corona == False:
                self.ninos_prob_card_sanos.append(persona)
            if persona.corona == True: 
                self.ninos_prob_card_coronavirus.append(persona)
        
        for persona in self.ninos_prob_resp:
            if persona.influenza == True:
                self.ninos_prob_resp_influenza.append(persona)                
            if persona.influenza == False and persona.corona == False:
                self.ninos_prob_resp_sanos.append(persona)
            if persona.corona == True: 
                self.ninos_prob_resp_coronavirus.append(persona)
        
        for persona in self.ninos_ambos_prob:
            if persona.influenza == True:
                self.ninos_ambos_prob_influenza.append(persona)                
            if persona.influenza == False and persona.corona == False:
                self.ninos_ambos_prob_sanos.append(persona)
            if persona.corona == True:
                self.ninos_ambos_prob_coronavirus.append(persona)
                
        for persona in self.adultos_sin_prob:
            if persona.influenza == True:
                self.adultos_sin_prob_influenza.append(persona)                
            if persona.influenza == False and persona.corona == False:
                self.adultos_sin_prob_sanos.append(persona)
            if persona.corona == True:
                self.adultos_sin_prob_coronavirus.append(persona)
                
        for persona in self.adultos_prob_card:
            if persona.influenza == True:
                self.adultos_prob_card_influenza.append(persona)                
            if persona.influenza == False and persona.corona == False:
                self.adultos_prob_card_sanos.append(persona)
            if persona.corona == True:
                self.adultos_prob_card_coronavirus.append(persona)
            
                
        for persona in self.adultos_prob_resp:
            if persona.influenza == True:
                self.adultos_prob_resp_influenza.append(persona)                
            if persona.influenza == False and persona.corona == False:
                self.adultos_prob_resp_sanos.append(persona)
            if persona.corona == True: 
                self.adultos_prob_resp_coronavirus.append(persona)
                
        for persona in self.adultos_ambos_prob:
            if persona.influenza == True:
                self.adultos_ambos_prob_influenza.append(persona)                
            if persona.influenza == False and persona.corona == False:
                self.adultos_ambos_prob_sanos.append(persona)
            if persona.corona == True:
                self.adultos_ambos_prob_coronavirus.append(persona)
                
        for persona in self.ancianos_sin_prob:
            if persona.influenza == True:
                self.ancianos_sin_prob_influenza.append(persona)                
            if persona.influenza == False and persona.corona == False:
                self.ancianos_sin_prob_sanos.append(persona)
            if persona.corona == True:
                self.ancianos_sin_prob_coronavirus.append(persona)
                
        for persona in self.ancianos_prob_card:
            if persona.influenza == True:
                self.ancianos_prob_card_influenza.append(persona)                
            if persona.influenza == False and persona.corona == False:
                self.ancianos_prob_card_sanos.append(persona)
            if persona.corona == True:
                self.ancianos_prob_card_coronavirus.append(persona)
                
        for persona in self.ancianos_prob_resp:
            if persona.influenza == True:
                self.ancianos_prob_resp_influenza.append(persona)                
            if persona.influenza == False and persona.corona == False:
                self.ancianos_prob_resp_sanos.append(persona)
            if persona.corona == True: 
                self.ancianos_prob_resp_coronavirus.append(persona)
                
        for persona in self.ancianos_ambos_prob:
            if persona.influenza == True:
                self.ancianos_ambos_prob_influenza.append(persona)                
            if persona.influenza == False and persona.corona == False:
                self.ancianos_ambos_prob_sanos.append(persona)
            if persona.corona == True:
                self.ancianos_ambos_prob_coronavirus.append(persona)
                
        return(self.ninos_sin_prob_sanos, self.ninos_prob_card_sanos,self.ninos_prob_resp_sanos ,self.ninos_ambos_prob_sanos,
        self.adultos_sin_prob_sanos ,self.adultos_prob_card_sanos ,self.adultos_prob_resp_sanos,self.adultos_ambos_prob_sanos,self.ancianos_sin_prob_sanos,self.ancianos_prob_card_sanos,
        self.ancianos_prob_resp_sanos,self.ancianos_ambos_prob_sanos,self.ninos_sin_prob_influenza, self.ninos_prob_card_influenza,self.ninos_prob_resp_influenza,self.ninos_ambos_prob_influenza,
        self.adultos_sin_prob_influenza, self.adultos_prob_card_influenza ,self.adultos_prob_resp_influenza,self.adultos_ambos_prob_influenza,self.ancianos_sin_prob_influenza, self.ancianos_prob_card_influenza,
        self.ancianos_prob_resp_influenza,
        self.ancianos_ambos_prob_influenza,
        self.ninos_sin_prob_coronavirus, 
        self.ninos_prob_card_coronavirus,
        self.ninos_prob_resp_coronavirus,
        self.ninos_ambos_prob_coronavirus,
        self.adultos_sin_prob_coronavirus, 
        self.adultos_prob_card_coronavirus,
        self.adultos_prob_resp_coronavirus, 
        self.adultos_ambos_prob_coronavirus,
        self.ancianos_sin_prob_coronavirus, 
        self.ancianos_prob_card_coronavirus,
        self.ancianos_prob_resp_coronavirus,
        self.ancianos_ambos_prob_coronavirus )


# In[3]:


class Persona():
    def __init__(self):
        self.prob_corona = 0
        self.prob_influenza = 0
        self.corona = False
        self.influenza = False
        self.vacuna = False
        self.contador_corona = 0
        self.contador_influenza = 0
        self.inmune_corona = 0
        self.inmune_influenza = 0


# Las siguientes 12 clases heredan de la clase Persona (heredando todos los atributos) y para cada una se calcula su probabilidad de contagio siguiendo las reglas establecidad en el enunciado para contagio zonal, estas incluyen la variacion producida en caso de que la persona se vacune.

# In[4]:


class Nino_sin_prob(Persona):
    
    def __init__ (self):
        Persona.__init__(self)
    
    def prob_de_contagio(self, corona_celda, influenza_celda, poblacion_total):
        self.prob_influenza = influenza_celda/poblacion_total
        if self.corona == False and self.influenza == False:
            self.prob_corona = corona_celda/poblacion_total
        if self.influenza == True and self.corona == False:
            self.prob_corona == 1.1*(corona_celda/poblacion_total) 
        if self.vacuna == True:
            self.prob_corona = self.prob_corona/2  
        return (self.prob_corona)
            
class Nino_prob_resp(Persona):
    
    def __init__ (self):
        Persona.__init__(self)
    
    def prob_de_contagio(self, corona_celda, influenza_celda, poblacion_total):
        self.prob_influenza = influenza_celda/poblacion_total
        if self.corona == False and self.influenza == False: 
            self.prob_corona = 1.1*(corona_celda/poblacion_total)
        if self.influenza == True and self.corona == False:
            self.prob_corona == 1.1*1.1*(corona_celda/poblacion_total)
        if self.vacuna == True:
            self.prob_corona = self.prob_corona/2 
        return (self.prob_corona)

class Nino_prob_card(Persona):
    
    def __init__ (self):
        Persona.__init__(self)
    
    def prob_de_contagio(self, corona_celda, influenza_celda, poblacion_total):
        self.prob_influenza = influenza_celda/poblacion_total
        if self.corona == False and self.influenza == False:
            self.prob_corona = 1.1*(corona_celda/poblacion_total)
        if self.influenza == True and self.corona == False:
            self.prob_corona == 1.1*1.1*(corona_celda/poblacion_total)
        if self.vacuna == True:
            self.prob_corona = self.prob_corona/2 
        return (self.prob_corona)
    
class Nino_ambos_prob(Persona):
    def __init__ (self):
        Persona.__init__(self)
    
    def prob_de_contagio(self, corona_celda, influenza_celda, poblacion_total):
        self.prob_influenza = influenza_celda/poblacion_total
        if self.corona == False and self.influenza == False:
            self.prob_corona = 1.1*1.1*(corona_celda/poblacion_total)
        if self.influenza == True and self.corona == False:
            self.prob_corona == 1.1*1.1*1.1*(corona_celda/poblacion_total)
        if self.vacuna == True:
            self.prob_corona = self.prob_corona/2 
        return (self.prob_corona)
    
class Adulto_sin_prob(Persona):
    def __init__ (self):
        Persona.__init__(self)
    
    def prob_de_contagio(self, corona_celda, influenza_celda, poblacion_total):
        self.prob_influenza = influenza_celda/poblacion_total
        if self.corona == False and self.influenza == False:
            self.prob_corona = 1.3*(corona_celda/poblacion_total)
        if self.influenza == True and self.corona == False:
            self.prob_corona == 1.1*1.3*(corona_celda/poblacion_total)
        if self.vacuna == True:
            self.prob_corona = self.prob_corona/2   
        return (self.prob_corona)
             

class Adulto_prob_resp(Persona):
    def __init__ (self):
        Persona.__init__(self)
    
    def prob_de_contagio(self, corona_celda, influenza_celda, poblacion_total):
        self.prob_influenza = influenza_celda/poblacion_total
        if self.corona== False and self.influenza == False:
            self.prob_corona = 2*(corona_celda/poblacion_total)
        if self.influenza == True and self.corona == False:
            self.prob_corona == 1.1*2*(corona_celda/poblacion_total)
        if self.vacuna == True:
            self.prob_corona = self.prob_corona/2  
        return (self.prob_corona)

class Adulto_prob_card(Persona):
    def __init__ (self):
        Persona.__init__(self)
    
    def prob_de_contagio(self, corona_celda, influenza_celda, poblacion_total):
        self.prob_influenza = influenza_celda/poblacion_total
        if self.corona== False and self.influenza == False:
            self.prob_corona = 2*(corona_celda/poblacion_total)
        if self.influenza == True and self.corona == False:
            self.prob_corona == 1.1*2*(corona_celda/poblacion_total)
        if self.vacuna == True:
            self.prob_corona = self.prob_corona/2  
        return (self.prob_corona)
    
class Adulto_ambos_prob(Persona):
    def __init__ (self):
        Persona.__init__(self)
    
    def prob_de_contagio(self, corona_celda, influenza_celda, poblacion_total):
        self.prob_influenza = influenza_celda/poblacion_total
        if self.corona == False and self.influenza == False:
            self.prob_corona = 1.1*2*(corona_celda/poblacion_total)
        if self.influenza == True and self.corona == False:
            self.prob_corona == 1.1*1.1*2*(corona_celda/poblacion_total)
        if self.vacuna == True:
            self.prob_corona = self.prob_corona/2  
        return (self.prob_corona)
    
class Anciano_sin_prob(Persona):
    def __init__ (self):
        Persona.__init__(self)
    
    def prob_de_contagio(self, corona_celda, influenza_celda, poblacion_total):
        self.prob_influenza = influenza_celda/poblacion_total
        if self.corona == False and self.influenza == False:
            self.prob_corona = 1.5*(corona_celda/poblacion_total)
        if self.influenza == True and self.corona == False:
            self.prob_corona == 1.1*1.5*(corona_celda/poblacion_total)
        if self.vacuna == True:
            self.prob_corona = self.prob_corona/2     
        return (self.prob_corona)
            
    
class Anciano_prob_resp(Persona):
    def __init__ (self):
        Persona.__init__(self)
    
    def prob_de_contagio(self, corona_celda, influenza_celda, poblacion_total):
        self.prob_influenza = influenza_celda/poblacion_total
        if self.corona == False and self.influenza == False:
            self.prob_corona = 3*(corona_celda/poblacion_total)
        if self.influenza == True and self.corona == False:
            self.prob_corona == 1.1*3*(corona_celda/poblacion_total)
        if self.vacuna == True:
            self.prob_corona = self.prob_corona/2  
        return (self.prob_corona)
            

class Anciano_prob_card(Persona):  
    def __init__ (self):
        Persona.__init__(self)
    
    def prob_de_contagio(self, corona_celda, influenza_celda, poblacion_total):
        self.prob_influenza = influenza_celda/poblacion_total
        if self.corona == False and self.influenza == False:
            self.prob_corona = 2*(corona_celda/poblacion_total)
        if self.influenza == True and self.corona == False:
            self.prob_corona == 1.1*2*(corona_celda/poblacion_total)
        if self.vacuna == True:
            self.prob_corona = self.prob_corona/2   
        return (self.prob_corona)
            
    
class Anciano_ambos_prob(Persona): 
    def __init__ (self):
        Persona.__init__(self)
    
    def prob_de_contagio(self, corona_celda, influenza_celda, poblacion_total):
        self.prob_influenza = influenza_celda/poblacion_total
        if self.corona== False and self.influenza == False:
            self.prob_corona = 12*(corona_celda/poblacion_total)
        if self.influenza == True and self.corona == False:
            self.prob_corona == 1.1*12*(corona_celda/poblacion_total)
        if self.vacuna == True:
            self.prob_corona = self.prob_corona/2
        return (self.prob_corona)


# In[5]:


class Ciudad():
    def __init__(self,M, N, poblacion_total):
        self.M = M
        self.N = N
        self.poblacion_total = poblacion_total
        self.ciudad = []
        self.poblacion_celda = []

        ## en este método se crea una matriz para ciudad, en donde cada celda va a tener un objeto Celda(i,j)
    def inicializar_ciudad(self):        
        for i in range(self.M):
            self.ciudad.append([])
            for j in range (self.N):
                self.ciudad[i].append(Celda(i,j))
      
    ##    al poblar la ciudad se permite recibir un parámetro externo que se asume como una lista que contiene todos 
    ## los objetos Celda correspondientes al tamaño a evaluar.
    
    def poblar_ciudad(self,parametros=[]):
        #esto ocurre solo en el caso de ingresar el parámetro especificado
        if parametros != []:
            for i in range (self.M):
                for j in range(self.N):
                    ind = parametros.index(Celda(i,j))
                    self.ciudad[i][j] = parametros[ind]
        
######### matriz con la poblacion total por celda, se determina de forma aleatoria siguiendo una distribución 
######## triangular la cantidad de personas que habrá en cada zona o celda
        pob = self.poblacion_total
        for i in range (self.M):
            self.poblacion_celda.append([])
            for j in range(self.N):
                if i == (self.M-1) and j == (self.N-1):
                    self.poblacion_celda[i].append(pob)
                else:
                    a = int(random.triangular(0.8*(self.poblacion_total/(self.M*self.N)),((self.poblacion_total/(self.M*self.N - 1))*1.1),self.poblacion_total/(self.M*self.N)))
                    pob -= a
                    self.poblacion_celda[i].append(a)


################# Se de termina de forma aleatoria de que clase va a ser cada persona antes de poblar la ciudad 
################ con la cantidad establecida en la matriz anterior. Una ves que se determina , se crea el objeto de esa clase y se 
############### ingresa en la celda como parte de su atributo correspondiente 
        for n in self.ciudad:
            for i in n:
                for j in range (self.poblacion_celda[i.m][i.n]):
                    a = random.choices(('nino_sin_prob','nino_prob_resp', 'nino_prob_card', 'nino_ambos_prob','adulto_sin_prob', 'adulto_prob_card', 'adulto_prob_resp', 'adulto_ambos_prob','anciano_sin_prob', 'anciano_prob_card', 'anciano_prob_resp', 'anciano_ambos_prob'),[10,7,7,4,9,9,9,8,5,10,9,11])
                    if a[0] == 'nino_sin_prob':
                        nsp = [Nino_sin_prob()]
                        l = i.ninos_sin_prob
                        l.extend(nsp)
                    elif a[0] == 'nino_prob_card':
                        npc = [Nino_prob_card()]
                        l=i.ninos_prob_card
                        l.extend(npc)
                    elif a[0] == 'nino_prob_resp':
                        p = [Nino_prob_resp()]
                        l=i.ninos_prob_resp
                        l.extend(p)
                    elif a[0] == 'nino_ambos_prob':
                        p = [Nino_ambos_prob()]
                        l=i.ninos_ambos_prob
                        l.extend(p)
                    elif a[0] == 'adulto_sin_prob':
                        p = [Adulto_sin_prob()]
                        l=i.adultos_sin_prob
                        l.extend(p)
                    elif a[0] == 'adulto_prob_card':
                        p =[Adulto_prob_card()]
                        l=i.adultos_prob_card
                        l.extend(p)
                    elif a[0] == 'adulto_prob_resp':
                        p = [Adulto_prob_resp()]
                        l=i.adultos_prob_resp
                        l.extend(p)
                    elif a[0] == 'adulto_ambos_prob':
                        p = [Adulto_ambos_prob()]
                        l=i.adultos_ambos_prob
                        l.extend(p)
                    elif a[0] == 'anciano_sin_prob':
                        p = [Anciano_sin_prob()]
                        l=i.ancianos_sin_prob
                        l.extend(p)
                    elif a[0] == 'anciano_prob_card':
                        p = [Adulto_prob_card()]
                        l=i.ancianos_prob_card
                        l.extend(p)
                    elif a[0] == 'anciano_prob_resp':
                        p = [Anciano_prob_resp()]
                        l=i.ancianos_prob_resp
                        l.extend(p)
                    elif a[0] == 'anciano_ambos_prob':
                        p = [Anciano_ambos_prob()]
                        l=i.ancianos_ambos_prob
                        l.extend(p)
        
    def paciente_cero(self):
        m0 = random.randrange(self.M) # se elige fila aleatoria
        n0 = random.randrange(self.N) # columna aleatoria
        cat = random.choice((self.ciudad[m0][n0].ninos_sin_prob, self.ciudad[m0][n0].ninos_prob_resp, self.ciudad[m0][n0].ninos_prob_card, self.ciudad[m0][n0].ninos_ambos_prob, self.ciudad[m0][n0].adultos_sin_prob, self.ciudad[m0][n0].adultos_prob_card, self.ciudad[m0][n0].adultos_prob_resp, self.ciudad[m0][n0].adultos_ambos_prob, self.ciudad[m0][n0].ancianos_sin_prob, self.ciudad[m0][n0].ancianos_prob_card, self.ciudad[m0][n0].ancianos_prob_resp, self.ciudad[m0][n0].ancianos_ambos_prob))
        # cat es la categoría o lista aleatoria de la persona para la celda correspondiente
        while len(cat) == 0: #solo por si por la aleatoridad una categoria de una celda está vacía 
            cat = random.choice((self.ciudad[m0][n0].ninos_sin_prob, self.ciudad[m0][n0].ninos_prob_resp, self.ciudad[m0][n0].ninos_prob_card, self.ciudad[m0][n0].ninos_ambos_prob, self.ciudad[m0][n0].adultos_sin_prob, self.ciudad[m0][n0].adultos_prob_card, self.ciudad[m0][n0].adultos_prob_resp, self.ciudad[m0][n0].adultos_ambos_prob, self.ciudad[m0][n0].ancianos_sin_prob, self.ciudad[m0][n0].ancianos_prob_card, self.ciudad[m0][n0].ancianos_prob_resp, self.ciudad[m0][n0].ancianos_ambos_prob))
        persona = random.randrange(len(cat))        
        cat[persona].corona = True # cambia la salud de la persona
        cat[persona].contador_corona += 1
        self.ciudad[m0][n0].casos_corona += 1  
        
        # mismo procedimiento para la influenza
        m0 = random.randrange(self.M)
        n0 = random.randrange(self.N)        
        icat = random.choice((self.ciudad[m0][n0].ninos_sin_prob, self.ciudad[m0][n0].ninos_prob_resp, self.ciudad[m0][n0].ninos_prob_card, self.ciudad[m0][n0].ninos_ambos_prob, self.ciudad[m0][n0].adultos_sin_prob, self.ciudad[m0][n0].adultos_prob_card, self.ciudad[m0][n0].adultos_prob_resp, self.ciudad[m0][n0].adultos_ambos_prob, self.ciudad[m0][n0].ancianos_sin_prob, self.ciudad[m0][n0].ancianos_prob_card, self.ciudad[m0][n0].ancianos_prob_resp, self.ciudad[m0][n0].ancianos_ambos_prob))
        while len(icat) == 0:
            icat = random.choice((self.ciudad[m0][n0].ninos_sin_prob, self.ciudad[m0][n0].ninos_prob_resp, self.ciudad[m0][n0].ninos_prob_card, self.ciudad[m0][n0].ninos_ambos_prob, self.ciudad[m0][n0].adultos_sin_prob, self.ciudad[m0][n0].adultos_prob_card, self.ciudad[m0][n0].adultos_prob_resp, self.ciudad[m0][n0].adultos_ambos_prob, self.ciudad[m0][n0].ancianos_sin_prob, self.ciudad[m0][n0].ancianos_prob_card, self.ciudad[m0][n0].ancianos_prob_resp, self.ciudad[m0][n0].ancianos_ambos_prob))        
        persona = random.randrange(len(icat))
        icat[persona].influenza = True
        icat[persona].contador_influenza += 1
        self.ciudad[m0][n0].casos_influenza += 1
        
        
    def guardar_ciudad(self): ## retorna una lista con los objetos en las listas especificadas en el enunciado
        lista_ciudad = []       
        for i in self.ciudad:
            for celda in i:
                lista_celda =[]
                lista_celda.append(celda.m)
                lista_celda.append(celda.n)
                condicion = celda.casos_categoria()
                lista_celda.extend(condicion)
                lista_ciudad.append(lista_celda)
                
        return (lista_ciudad)
                


# # Simulación

# Para la simulacion es necesario considerar que se utilizaron distintos citerios de parada y que no imprime nada al menos que se incluya despues. 
# Es necesario ingresar un valor de días en el que ocurra la simulacio por si se quiere hacer el estudio de un período sepuede modificar la variable dias_termino en la celda continua y tambian el tamaño de la celda en donde M son las filas y N las columnas, o la población total de la ciudad. Sin embargo, siempre va a parar cuando toda la poblacion se contagie de coronavirus (se considera que este es el virus más relevante, se se estimara conveniente se puede agregar un criterio de parada para la influenza).

# In[6]:


dias_termino = 30

poblacion_ciudad = 100000
N=5
M=5


# In[7]:


ciudad=Ciudad(M,N,poblacion_ciudad)
ciudad.inicializar_ciudad()
ciudad.poblar_ciudad()

ciudad.paciente_cero()


# como se sabe que al ejecutar paciente_cero() se agrega SOLO 1 contagiado de coronavirus e influenza , se comienza a contabilizar desde este
casos_coronavirus = 1
casos_totales_influenza =1
sanados_influenza = 0
sanados_coronavirus = 0
dias = 0
while dias < dias_termino and casos_coronavirus < ciudad.poblacion_total:
 ## se evalua si se puede liberar la vacuna, eligendo una persona con el mismo procedimiento que en paciente_cero()     
    if casos_coronavirus > 0.5* ciudad.poblacion_total:
        m0 = random.randrange(ciudad.M)
        n0 = random.randrange(ciudad.N)
        cat = random.choice((ciudad.ciudad[m0][n0].ninos_sin_prob, ciudad.ciudad[m0][n0].ninos_prob_resp, ciudad.ciudad[m0][n0].ninos_prob_card, ciudad.ciudad[m0][n0].ninos_ambos_prob, ciudad.ciudad[m0][n0].adultos_sin_prob, ciudad.ciudad[m0][n0].adultos_prob_card, ciudad.ciudad[m0][n0].adultos_prob_resp, ciudad.ciudad[m0][n0].adultos_ambos_prob, ciudad.ciudad[m0][n0].ancianos_sin_prob, ciudad.ciudad[m0][n0].ancianos_prob_card, ciudad.ciudad[m0][n0].ancianos_prob_resp, ciudad.ciudad[m0][n0].ancianos_ambos_prob))
        while len(cat) == 0:
            cat = random.choice((ciudad.ciudad[m0][n0].ninos_sin_prob, ciudad.ciudad[m0][n0].ninos_prob_resp, ciudad.ciudad[m0][n0].ninos_prob_card, ciudad.ciudad[m0][n0].ninos_ambos_prob, ciudad.ciudad[m0][n0].adultos_sin_prob, ciudad.ciudad[m0][n0].adultos_prob_card, ciudad.ciudad[m0][n0].adultos_prob_resp, ciudad.ciudad[m0][n0].adultos_ambos_prob, ciudad.ciudad[m0][n0].ancianos_sin_prob, ciudad.ciudad[m0][n0].ancianos_prob_card, ciudad.ciudad[m0][n0].ancianos_prob_resp, ciudad.ciudad[m0][n0].ancianos_ambos_prob))
            
        persona = random.randrange(len(cat))        
        cat[persona].vacuna = True
        ciudad.ciudad[m0][n0].casos_vacuna += 1
     
    ### se crea una lista con las listas de todas las persoas en la celda
    for  i in ciudad.ciudad:
        for zona in i:
            lista_personas = [zona.ninos_sin_prob, zona.ninos_prob_resp, zona.ninos_prob_card, zona.ninos_ambos_prob, zona.adultos_sin_prob, zona.adultos_prob_card, zona.adultos_prob_resp, zona.adultos_ambos_prob, zona.ancianos_sin_prob, zona.ancianos_prob_card, zona.ancianos_prob_resp, zona.ancianos_ambos_prob]

            for lista in lista_personas:
                for persona in lista:
                    if persona.vacuna == False:
                        if persona.inmune_corona:
                            prob_v = persona.prob_de_contagio(zona.casos_corona, zona.casos_influenza,ciudad.poblacion_celda[zona.m][zona.n])               
                            #### A continuación se aplican las reglas de contagio inter zonal
                            if (((zona.m - 1)>=0 and (zona.n - 1)>= 0) and (ciudad.ciudad[(zona.m-1)][(zona.n-1)].casos_vacuna>= 0.6*ciudad.poblacion_celda[(zona.m-1)][(zona.n-1)])): 
                                prob_v +=0.1
                            if (((zona.m + 1)<=(ciudad.M-1) and (zona.n + 1)<=(ciudad.N-1)) and (ciudad.ciudad[(zona.m+1)][(zona.n+1)].casos_vacuna>= 0.6*ciudad.poblacion_celda[(zona.m+1)][(zona.n+1)])):
                                prob_v += 0.1
                            if (((zona.m + 1)<=(ciudad.M-1) and (zona.n - 1)>= 0) and (ciudad.ciudad[(zona.m+1)][(zona.n-1)].casos_vacuna>= 0.6*ciudad.poblacion_celda[(zona.m+1)][(zona.n-1)])):
                                prob_v += 0.1
                            if (((zona.m - 1)>=0 and (zona.n + 1)<=(ciudad.N-1)) and (ciudad.ciudad[(zona.m-1)][(zona.n+1)].casos_vacuna>= 0.6*ciudad.poblacion_celda[(zona.m-1)][(zona.n+1)])) or (((zona.m - 1)>=0 and (zona.n)>= 0) and (ciudad.ciudad[(zona.m-1)][zona.n].casos_vacuna>= 0.6*ciudad.poblacion_celda[(zona.m-1)][zona.n])) or ((zona.m>=0 and (zona.n - 1)>= 0) and (ciudad.ciudad[zona.m][(zona.n-1)].casos_vacuna>= 0.6*ciudad.poblacion_celda[zona.m][(zona.n-1)])) or (((zona.m + 1)<=(ciudad.M-1) and (zona.n)>= 0) and (ciudad.ciudad[(zona.m+1)][zona.n].casos_vacuna>= 0.6*ciudad.poblacion_celda[(zona.m+1)][zona.n])) or (((zona.m)>=0 and (zona.n + 1)<=(ciudad.N-1)) and (ciudad.ciudad[zona.m][(zona.n+1)].casos_vacuna>= 0.6*ciudad.poblacion_celda[zona.m][(zona.n+1)])):
                                prob_v += 0.1
                            cond = random.choices((True,False),[prob_v,(1 - prob_v)])
                            persona.vacuna = cond[0]
        
        #### se sigue el mismo procedimiento, agregando las condiciones de inmunidad. Es lo mismo para influenza y después coronavirus      
            for lista in lista_personas:
                for persona in lista:
                    if persona.influenza == False:
                        if persona.inmune_influenza == False:
                            prob_i = zona.casos_influenza/ciudad.poblacion_celda[zona.m][zona.n]
                            if (((zona.m - 1)>=0 and (zona.n - 1)>= 0) and (ciudad.ciudad[(zona.m-1)][(zona.n-1)].casos_influenza>= 0.6*ciudad.poblacion_celda[(zona.m-1)][(zona.n-1)])): 
                                prob_i += 0.1
                            if (((zona.m + 1)<=(ciudad.M-1) and (zona.n + 1)<=(ciudad.N-1)) and (ciudad.ciudad[(zona.m+1)][(zona.n+1)].casos_influenza>= 0.6*ciudad.poblacion_celda[(zona.m+1)][(zona.n+1)])):
                                prob_i += 0.1
                            if (((zona.m + 1)<=(ciudad.M-1) and (zona.n - 1)>= 0) and (ciudad.ciudad[(zona.m+1)][(zona.n-1)].casos_influenza>= 0.6*ciudad.poblacion_celda[(zona.m+1)][(zona.n-1)])):
                                prob_i += 0.1
                            if (((zona.m - 1)>=0 and (zona.n + 1)<=(ciudad.N-1)) and (ciudad.ciudad[(zona.m-1)][(zona.n+1)].casos_influenza>= 0.6*ciudad.poblacion_celda[(zona.m-1)][(zona.n+1)])) or (((zona.m - 1)>=0 and (zona.n)>= 0) and (ciudad.ciudad[(zona.m-1)][zona.n].casos_influenza>= 0.6*ciudad.poblacion_celda[(zona.m-1)][zona.n])) or ((zona.m>=0 and (zona.n - 1)>= 0) and (ciudad.ciudad[zona.m][(zona.n-1)].casos_influenza>= 0.6*ciudad.poblacion_celda[zona.m][(zona.n-1)])) or (((zona.m + 1)<=(ciudad.M-1) and (zona.n)>= 0) and (ciudad.ciudad[(zona.m+1)][zona.n].casos_influenza>= 0.6*ciudad.poblacion_celda[(zona.m+1)][zona.n])) or (((zona.m)>=0 and (zona.n + 1)<=(ciudad.N-1)) and (ciudad.ciudad[zona.m][(zona.n+1)].casos_influenza>= 0.6*ciudad.poblacion_celda[zona.m][(zona.n+1)])):
                                prob_i += 0.1
                            cond = random.choices((True,False),[prob_i,(1-prob_i)])
                            if cond[0] == True:
                                persona.influenza = cond[0]
                                persona.contador_influenza += 1
                                zona.casos_influenza += 1
                                casos_totales_influenza += 1
                    else:
                        if persona.contador_influenza == 10:
                            persona.influenza = False
                            persona.inmune_influenza = True
                            sanados_influenza += 1
                        else:
                            persona.contador_influenza += 1

            for lista in lista_personas:
                for persona in lista:
                    if persona.corona == False:
                        if persona.inmune_corona == False:
                            prob = persona.prob_de_contagio(zona.casos_corona, zona.casos_influenza,ciudad.poblacion_celda[zona.m][zona.n])
                            if (((zona.m - 1)>=0 and (zona.n - 1)>= 0) and (ciudad.ciudad[(zona.m-1)][(zona.n-1)].casos_corona>= 0.6*ciudad.poblacion_celda[(zona.m-1)][(zona.n-1)])): 
                                prob += 0.1
                            if (((zona.m + 1)<=(ciudad.M-1) and (zona.n + 1)<=(ciudad.N-1)) and (ciudad.ciudad[(zona.m+1)][(zona.n+1)].casos_corona>= 0.6*ciudad.poblacion_celda[(zona.m+1)][(zona.n+1)])):
                                prob += 0.1
                            if (((zona.m + 1)<=(ciudad.M-1) and (zona.n - 1)>= 0) and (ciudad.ciudad[(zona.m+1)][(zona.n-1)].casos_corona>= 0.6*ciudad.poblacion_celda[(zona.m+1)][(zona.n-1)])):
                                prob += 0.1
                            if (((zona.m - 1)>=0 and (zona.n + 1)<=(ciudad.N-1)) and (ciudad.ciudad[(zona.m-1)][(zona.n+1)].casos_corona>= 0.6*ciudad.poblacion_celda[(zona.m-1)][(zona.n+1)])) or (((zona.m - 1)>=0 and (zona.n)>= 0) and (ciudad.ciudad[(zona.m-1)][zona.n].casos_corona>= 0.6*ciudad.poblacion_celda[(zona.m-1)][zona.n])) or ((zona.m>=0 and (zona.n - 1)>= 0) and (ciudad.ciudad[zona.m][(zona.n-1)].casos_corona>= 0.6*ciudad.poblacion_celda[zona.m][(zona.n-1)])) or (((zona.m + 1)<=(ciudad.M-1) and (zona.n)>= 0) and (ciudad.ciudad[(zona.m+1)][zona.n].casos_corona>= 0.6*ciudad.poblacion_celda[(zona.m+1)][zona.n])) or (((zona.m)>=0 and (zona.n + 1)<=(ciudad.N-1)) and (ciudad.ciudad[zona.m][(zona.n+1)].casos_corona>= 0.6*ciudad.poblacion_celda[zona.m][(zona.n+1)])):
                                prob += 0.1
                            cond = random.choices((True,False),[prob,(1-prob)])
                            if cond[0] == True:
                                persona.corona = cond[0]
                                persona.contador_corona += 1
                                zona.casos_corona += 1
                                casos_coronavirus += 1
                    else:
                        if persona.contador_corona == 14:
                            persona.corona = False
                            persona.inmune_corona = True
                            sanados_coronavirus += 1
                        else:
                            persona.contador_corona += 1

    condicion_ciudad = ciudad.guardar_ciudad() # guarda la condicion de la ciudad para cada dia, es necesaio recordar que si se imprime solo se ven objetos y no números siguiendo lo establecid en el enunciado
    dias += 1

