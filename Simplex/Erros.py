import numpy as np

def ErrosECondicoes(A, b, x, m):

    if np.all(x) != None:
        # Só faz as verificações caso passado uma solução básica viável
        # ou uma soluação viável, caso contrario, segue para o método
        # das duas fases.
        
        # Veficação do posto
        if np.linalg.matrix_rank(A) != m:
            print("Matriz de posto incompleto.")
        else:
            print("Matriz de posto completo.")

        # Verificação se x >=0
        if np.any(x < 0):
            return (True, "Alguma componente de x é negativa")
        
        # Verficação da viabilidade da solução
        if np.any(A@x != b):
            return (True, "Solução não viável")

    return (False, "Iniciando simplex...")
    