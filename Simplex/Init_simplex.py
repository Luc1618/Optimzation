import numpy as np
from MetodoDasDuasFases import DuasFases
from MetodoSimplex import Simplex
from Erros import ErrosECondicoes

def init_simplex(A, b, c, x = None):

    # m: Número de restrições / Número de variáveis de folga
    # n: Número de variáveis totais
    # n - m: número de variáveis originais / dimensão do PPL
    (m, n) = A.shape

    # Algumas pré-verificações
    (err, msg) = ErrosECondicoes(A, b, x, m)

    if err:
        return print(msg)
    else:
        print(msg)

    ### Casos do Simplex
    if np.all(x) == None:
        # Caso 0: solução não fornecida ;
        Ib, In = DuasFases(A, b, c)

    elif np.sum(x == 0) >= (n - m):
        # Caso 1: x é uma solução básica viável, degenarada ou não ;
        Ib = np.where(x != 0)[0] # Índices das variáveis básicas
        In = np.where(x == 0)[0] # Índices das variáveis não básicas
    
    elif np.sum(x == 0) < (n - m):
        # Caso 2: x é viável e não básica ;
        Ib = np.arange(0, m+1) # Base arbitrária
        In = np.arange(m+1, n+1)

    print("Base selecionada inicial:")
    print(f"Ib: {Ib}")
    print(f"In: {In}")

    (Zot, Xot, Ibot, Inot) = Simplex(A, b, c, x, Ib, In)
        
    print(f"Valor Ótimo: {Zot}")
    print(f"X*: {Xot}")
    print(f"Base ótima: {Ibot}")

    return print("Fim do Simplex")
