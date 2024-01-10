import copy


'''
met = metrica ['mink', 'euclid']
cov = bool [covariante o no covariante]
metrica -> (Vector) elemento de Vector multiplicado por el elemento de la métrica
'''
class Vector:
    #metodos de clase
    @classmethod  #webada con caracteristicas especiales que comparten propiedades similares de la misma clase
    def cuadrivector(cls, t:float, x, y, z): #los :float dentro, indica que tipo de variable debería ser y lo castea
        
        return cls(t,-x, -y, -z, met = 'mink',cov = True)
    
    @classmethod
    def vectorCeros(cls, n):
        zeros = []
        for i in range(n):
            zeros.append(0)

        return cls(zeros)
    #contructor

    def __init__(self, *arreglo, met = 'euclid',cov = False) -> None:#la flecha inidica que me va a regresar, *, indefinida de parametros, necesito uno por componente

       # [[]], [()], [1,2,3,4]
        if(len(arreglo) == 1):
            self.data = list(copy.copy(arreglo))
        elif(len(arreglo) > 1):
            self.data = list(copy.copy(arreglo))
        else:
            raise ValueError("El arreglo debe tener al menos un elemento numerico o de tipo lista[]/tupla()")
  
        self.cov = cov
        self.met = met
    #metodo
    def productoInterno(self) -> float:

        producto = 0
        
        for i,j in zip(self, self.metrica()):
            producto += i*j

        return producto
        
        # if len(self.valores) <= 3 or len(self.valores) > 4:
        #     return sum([i**2 for i in self.valores]) 
        # else:
        #    return (self.valores[0]**2 - sum([i**2 for i in self.valores[1:]])) 

    def metrica(self):

        match self.met:
            case 'euclid':
                return self
            case 'mink':
                return self.cuadrivector(self.data[0],self.data[1],self.data[2],self.data[3])
        
        # if len(self.valores) <= 3 or len(self.valores) > 4:
        #     return sum([i**2 for i in self.valores])
        # else:
        #     return (self.valores[0]**2 - sum([i**2 for i in self.valores[1:]]))

    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __str__(self) -> str:

        return str(self.data)
    
    def __len__(self):
        return len(self.data)
    

if __name__ == "__main__":
    vec = Vector.cuadrivector(1,2,3,4)

    print(vec[0])

    vec[0] = 6

    print(vec.productoInterno())
