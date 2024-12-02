import numpy as np



n = 1000
A = np.random.randint(0,10, (n, n))
B = np.random.randint(0,10, (n,n))
C = A @ B

for _ in range(10):
    # Generate a random vector r with entries 0 or 1
    r = np.random.randint(0, 2, size=(n, 1))

    # Compute P = A @ (B @ r) and Q = C @ r
    P = A @ (B @ r)
    Q = C @ r

    # Check if P equals Q
    if not np.array_equal(P, Q):
        print(f'false')
    else:
        print(f'true')

