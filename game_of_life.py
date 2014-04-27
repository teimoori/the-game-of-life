from scipy import sparse
from numpy import array,concatenate


def demo(case):
    #these patterns have been imported from wikipedia
    if case==1:
        print "Pattern:Blinker (period 2)"
        I=array([2,2,2])
        J=array([0,1,2])
    elif case==2:
        print "Pattern: Toad (period 2)"
        I=array([2,3,3,2,2,3])
        J=array([3,2,3,4,5,4])
    elif case==3:
        print "Pattern: Spaceships"
        I=array([1,2,2,3,3])
        J=array([1,2,3,1,2])


    ##This part is essential to have a frame of 0 around the data
    if 0 in I:
        I+=1
    if 0 in J:
        J+=1
    dimension=max(max(I),max(J))+3
    M=sparse.csr_matrix(([1]*len(I),(I,J)),(dimension,dimension))    
    return M

def surrounding_matrix_calculator(M):
    #This function helps to calculate the surrounding number for interested nodes
    I,J=M.nonzero()
    I=concatenate([I-1,I+1,I,I,I-1,I+1,I+1,I-1])
    J=concatenate([J,J,J+1,J-1,J-1,J+1,J-1,J+1])
    ##This part is essential to have a frame of 0 around the data
    if 1 not in I and 0 not in I:
        I=I-1
    if 1 not in J and 0 not in J:
        J=J-1
    MS=sparse.csr_matrix(([1]*len(I),(I,J)),M.shape)
    return MS

def find_next_generation(surrounding_matrix,M):
    # Here we evaluate the candidates and select the next generation
    current_alive=M.multiply(surrounding_matrix)
    current_dead=surrounding_matrix-current_alive
    current_alive.data=array((map((lambda x: 1 if x==2 or x==3 else 0 ), current_alive.data)))
    current_dead.data=array((map((lambda x: 1 if x==3 else 0 ), current_dead.data)))
    return current_dead+current_alive

def game_of_life(M):
    #This is the main function who gets a Matrix and returns the next generation one
    surrounding_matrix=surrounding_matrix_calculator(M)
    M=find_next_generation(surrounding_matrix,M)
    return M 
    
    
if __name__=="__main__":

    
    M=demo(3)  # valid values : 1,2,3
    print "initial\n", M.todense()
    for i in range(1,10):  # we run it for 10 iterations
        M=game_of_life(M)
        print "Iteration :",i
        print M.todense()







