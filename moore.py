class MooreAutomata:
    def __init__(self):
        self.estados = {
            'q0': {'salida': 0},
            'q1': {'salida': 1},
            'q2': {'salida': 0}
        }
        
        self.transiciones = {
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q0', '1': 'q2'},
            'q2': {'0': 'q0', '1': 'q1'}
        }
        
        self.estado_actual = 'q0'
        self.historial = []
    
    def procesar_entrada(self, entrada):
        print(f"\n--- Procesando: {entrada} ---")
        print(f"Inicio: q0 (salida 0)")
        
        resultado = []
        estados_recorridos = ['q0']
        
        for i, bit in enumerate(entrada):
            estado_anterior = self.estado_actual
            
            self.estado_actual = self.transiciones[self.estado_actual][bit]
            salida_actual = self.estados[self.estado_actual]['salida']
            
            estados_recorridos.append(self.estado_actual)
            
            if self.estado_actual == 'q2' and len(resultado) > 0:
                resultado[-1] = 0
                resultado.append(0)
                print(f"  Bit {i+1}='{bit}': {estado_anterior}→{self.estado_actual} | salida: [11 -> 00]")
            else:
                resultado.append(salida_actual)
                print(f"  Bit {i+1}='{bit}': {estado_anterior}→{self.estado_actual} | salida: {salida_actual}")
        
        print(f"\nResultado:")
        print(f"  Entrada: {entrada}")
        print(f"  Salida:  {''.join(map(str, resultado))}")
        print(f"  Estados: {' → '.join(estados_recorridos)}")


def main():
    while True:
        automata = MooreAutomata()
        
        while True:
            secuencia = input("\nIngresa secuencia de bits (0/1): ").strip()
            if all(bit in '01' for bit in secuencia):
                break
            print("Error: Solo 0 y 1")
        
        automata.procesar_entrada(secuencia)
        
        continuar = input("\n¿Otra secuencia? (s/n): ").strip().lower()
        if continuar != 's':
            print("Hasta luego!")
            break


if __name__ == "__main__":
    main()

    