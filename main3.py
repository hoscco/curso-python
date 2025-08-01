from dataclasses import dataclass

@dataclass
class Numero:
    numero: int 
        
    def evaluarNumero(self):
        if self.numero & 1:
            print("impar")
            if self.numero == 7:
                print("\nEl número es un comodin")
        else:
            print("par")
            if self.numero == 10:
                print("\nEl número ingresado es 10")
                
    def sumar(self,numerosumar):
        return self.numero + numerosumar


if __name__ == "__main__":
    
    numeroaevaluar = Numero(int(input("Ingrese un número: \n")))
    numeroaevaluar.evaluarNumero()
    sumarealizada = numeroaevaluar.sumar(2)
    print("\nLa suma realizada es: ",sumarealizada)



    
    
    
    
    