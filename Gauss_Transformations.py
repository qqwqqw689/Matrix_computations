import numpy as np

# matrix computations : 3.2.2
def Gauss_Transformations(C: np.ndarray, t: np.ndarray, k: int, n: int) -> np.ndarray:
    """
    n -> the number of rows of C,t , k -> the last number that t[k] equal to 0,
    C -> n*r, t -> n*1
    """
    for i in range(k+1, n):
        C[i,:] = C[i,:] - t[i]*C[k,:]
    return C

if __name__ == "__main__":

    C = np.array([[1,4,7],
                  [2,5,8],
                  [3,6,10]])

    t = np.array([0,1,-1]) # t.shape -> (3,)
    
    t = t.reshape((3,1))   # t.shape -> (3, 3)
    
    print(Gauss_Transformations(C, t, 0, 3))
