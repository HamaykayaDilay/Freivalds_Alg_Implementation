import numpy as np



n = 1000  #for the matrices to be size of nxn ( n chosen a fairly high number)

results=[] # list to count the True and False results at the end
for _ in range(100): #to try the algorithm more than once, its 100 to create a percentage
    A = np.random.randint(0, 10, (n, n)) #A and B in the loop so that there are
                                                        #different A and B in each calc
    B = np.random.randint(0, 10, (n, n))
    C = A @ B   # every iteration we get a different C
    # Generate a random vector r with entries 0 or 1 to test the multiplication
    r = np.random.randint(0, 2, size=(n, 1))
    #print('r:', r) (tried to check r)
    # try to change C
    # Corrupt two random entries in C
    i, j = np.random.randint(0, n), np.random.randint(0, n)
    k, l = np.random.randint(0, n), np.random.randint(0, n)
    C[i, j] -= 1000
    C[k, l] -= 1000

    # Compute P = A @ (B @ r) and Q = C @ r
    P = A @ (B @ r) - C @ r   #found from wikipedia in 'Freivalds' Algorithm'

    # Check if P equals Q
    result = np.all(P == 0)  # True if no error detected, False if error detected
    results.append(result)

# Analyze the results
fails = results.count(True)  # True means the algorithm failed to detect the error
success_rate = (1 - fails / 100) * 100  # Percentage of successful error detection

print(f"Freivalds' algorithm successfully detected errors in {success_rate:.2f}% of the trials.")

# the version with 0 changes in the members of matrix C has a 100% True which is correct since C stays same.
#the version with one member changed in matrix C has 43% True which means that
# the Freivalds Algorithm fails to detect the error for 43%.
# 2 indices getting changed in C results in 20% True detections which means it fails to detect the error for 20%
