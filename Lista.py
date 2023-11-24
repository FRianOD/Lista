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
        
    def adicionar(self, pos, valor):
        
        if pos <= 0 and pos >= self.numeroDeElementos:
            
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
                    
        
         