class Dado:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
    
class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.numeroDeElementos = 0
    
    def estaVazia(self):
        if self.fim == None and self.inicio == None: return True
        else: return False
        
    def tamanho(self):
        return self.numeroDeElementos
        
    def adicionar(self, pos, valor):
        
        if pos >= 0 and pos <= self.numeroDeElementos:
            
            novoDado = Dado(valor)
            
            if self.estaVazia():
                self.inicio = self.fim = novoDado
            
            elif pos == 0 :
                novoDado.prox = self.inicio
                self.inicio = novoDado
                
            elif pos == self.numeroDeElementos:
                self.fim.prox = novoDado
                self.fim = novoDado
                
            else:
                temp = self.inicio
                for i in range(pos - 1):
                    temp = temp.prox
                novoDado.prox = temp.prox
                temp.prox = novoDado
            
            self.numeroDeElementos += 1
            
        else:
            return f"Posição invalida"
                    
    def remover_V(self, valor):
        if self.estaVazia(): return f"Lista vazia"
        
        lixo = Dado(-1)
        
        if valor == self.inicio.valor and self.numeroDeElementos == 1:
            lixo = self.inicio
            self.inicio = self.fim = None 
            
        if valor == self.inicio.valor:
            
            lixo = self.inicio
            self.inicio = self.inicio.prox
        
        elif valor == self.fim.valor:
            
            lixo = self.fim
            temp = self.inicio
            i = 0
            
            while i < self.numeroDeElementos - 2:
                
                temp = temp.prox
                i += 1
                
            self.fim = temp
            self.fim.prox = None
            
        else:
            temp = self.inicio
            
            while temp.prox != None and valor != temp.prox.valor:
                    temp = temp.prox
                    
            if temp.prox is not None:
                lixo = temp.prox
                temp.prox = temp.prox.prox
            
        self.numeroDeElementos -= 1
        return lixo.valor
    
    def remover_P(self, pos):
    
        if self.estaVazia(): return f"Lista vazia"
        
        lixo = Dado(-1)
        
        if pos == 0 and self.numeroDeElementos == 1:
            lixo = self.inicio
            self.inicio = self.fim = None 
            
        if pos == 0:
            
            lixo = self.inicio
            self.inicio = self.inicio.prox
        
        elif pos == self.numeroDeElementos - 1:
            
            lixo = self.fim
            temp = self.inicio
            
            for i in range(self.numeroDeElementos - 2):
                
                temp = temp.prox
                
            self.fim = temp
            self.fim.prox = None
            
        else:
            temp = self.inicio
            
            for i in range(pos-1) :
                    temp = temp.prox
            
            if temp.prox != None:
                lixo = temp.prox
                temp.prox = temp.prox.prox
        
        self.numeroDeElementos -= 1
        return lixo.valor