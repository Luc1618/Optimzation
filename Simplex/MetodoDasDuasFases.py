
import numpy as np
from MetodoSimplex import Simplex

def DuasFases(A, b, c):
    
    (m, n) = A.shape
    I = np.identity(m)

    ## PROBLEMA AUXILIAR
    C_mdf = np.ones(m)
    A_mdf = np.concatenate((A, I), axis = 1)
    # Tomando base conhecida para o problema auxiliar
    In_mdf = np.arange(0, n) # Colunas de 0 até n-1
    Ib_mdf = np.arange(n, m+n) # Colunas de n até até m+n-1

    ## FASE 1
    (z, Ib, In) = Simplex(A_mdf, b, C_mdf, Ib_mdf, In_mdf)

    ##### CONDIÇÕES SOBRE Z

    return Ib, In