import numpy as np

def Simplex(A, b, c, x, Ib, In):

    flag = True

    while flag:

        xb = x[Ib]
        B = A[:, Ib]
        N = A[:, In]
        cb = c[Ib]
        cn = c[In]
        Binv = np.linalg.inv(B)

        custoRed = cb@Binv@N - cn # Custo reduzido

        if np.all(custoRed >= 0) & np.all(xb >= 0):
            print("Solução ótima encontrada")
            flag = False

        else:
            # Regra de Bland
            k = max(In[np.where(custoRed < 0)[0]]) # Índice de quem entrará na base
            kind = np.where(In == k)[0][0] # Índice python para matriz N ou B^-1N
            Xi = Binv@b
            Yik = (Binv@N)[:, kind]

            # Equivalente a dizer que L é vázio.
            if np.all(A[:, k] <= 0):
                print("Problema Ilimitado")
                return
        
            Xi_Yik = np.divide(Xi, Yik, out=np.full_like(Xi, np.inf), where=Yik > 0)
            i = Ib[np.argmin(Xi_Yik)] # índice de quem esta na base e sairá
            x[k] = min(Xi_Yik)
            x[i] = 0
            
            ### AJEITAR ÍNDICES
            # Troca de base
            Ib = np.where(Ib == i, k, Ib)
            In = np.where(In == k, i, In)

    return (np.dot(c, x), x, Ib, In)