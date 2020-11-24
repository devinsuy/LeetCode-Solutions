from math import factorial

# Implentation of nCr
def combo(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n-r)))

# Map param tuples -> num_kills, avoid redudant processing
cache = {}

def rpg_util(N, M, dmg, depth):
    # Memoization
    params = (N, M, dmg, depth)
    if params in cache:
        # print("Cache hit")
        return cache[params]  

    # Base case
    if depth == 0:
        # Dmg reached in <= K hits, DID kill
        if dmg >= N:
             return 1 
        # Decision path tree selected all K of its values, did NOT kill
        else: 
            return 0

    # Recurse and sum each possible path at the next depth
    num_kills = 0
    for i in range(0, M+1): 
        num_kills += rpg_util(N, M, dmg+i, depth-1)
    
    # Cache results for lookup
    cache[params] = num_kills
    return num_kills

def rpg(N, M, K):
    total_prob = 0

    # Values can only assume {0,1}, use binomial distribution
    if M == 1:
        total_prob = 0
        for num_hits in range(N, K+1):
            total_prob += combo(K, num_hits) * pow(0.5, num_hits) * pow(0.5, (K-num_hits))
    
    # Recurse solution using decision tree
    else:
        total_combos = pow(M+1, K)
        num_kills = rpg_util(N, M, 0, K)
        total_prob = num_kills / total_combos
        print("\nTotal:", total_combos)
        print("Kills:", num_kills)

    return round(total_prob, 3)


def test():
    # Expected: 0.5
    N = 2
    M = 1
    K = 3
    print("For (N =", N, "M =", M, "K =", str(K) + ")")
    print("P(Kill) =", rpg(N,M,K))
    print("----------------------End Test Case----------------------\n")

    # Expected: 23/27 = 0.85
    N = 2
    M = 2
    K = 3
    print("For (N =", N, "M =", M, "K =", str(K) + ")")
    print("P(Kill) =", rpg(N,M,K))
    print("----------------------End Test Case----------------------\n")

    # Expected: 17/27 = 0.63
    N = 3
    M = 2
    K = 3
    print("For (N =", N, "M =", M, "K =", str(K) + ")")
    print("P(Kill) =", rpg(N,M,K))
    print("----------------------End Test Case----------------------\n")

    # Expected: 10/27 = 0.37
    N = 4
    M = 2
    K = 3
    print("For (N =", N, "M =", M, "K =", str(K) + ")")
    print("P(Kill) =", rpg(N,M,K))
    print("----------------------End Test Case----------------------\n")

test()



# Use if path outputs desired
# def rpg_util_show_paths(N, M, dmg, depth, path):
#     # Base case
#     if depth == 0:
#         # Dmg reached in <= K hits, DID kill
#         if dmg >= N:
#             print("Killed:", path)        
#             return 1 
#         # Decision path tree selected all K of its values, did NOT kill
#         else:
#             print("\nFailed:", path, "\n")
#             return 0

#     num_kills = 0
#     for i in range(0, M+1):
#         new_path = [x for x in path]
#         new_path.append(i)
#         num_kills += rpg_util(N, M, dmg+i, depth-1, new_path)
    
#     return num_kills

# Sample output: rpg_util_show_paths()  
'''
For (N = 2 M = 2 K = 3)

Failed: [0, 0, 0]      


Failed: [0, 0, 1]      

Killed: [0, 0, 2]      

Failed: [0, 1, 0]      

Killed: [0, 1, 1]      
Killed: [0, 1, 2]      
Killed: [0, 2, 0]
Killed: [0, 2, 1]
Killed: [0, 2, 2]

Failed: [1, 0, 0]

Killed: [1, 0, 1]
Killed: [1, 0, 2]
Killed: [1, 1, 0]
Killed: [1, 1, 1]
Killed: [1, 1, 2]
Killed: [1, 2, 0]
Killed: [1, 2, 1]
Killed: [1, 2, 2]
Killed: [2, 0, 0]
Killed: [2, 0, 1]
Killed: [2, 0, 2]
Killed: [2, 1, 0]
Killed: [2, 1, 1]
Killed: [2, 1, 2]
Killed: [2, 2, 0]
Killed: [2, 2, 1]
Killed: [2, 2, 2]

Total: 27
Kills: 23
P(Kill) = 0.852
'''