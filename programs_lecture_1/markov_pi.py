import random

# +
x, y = 1.0, 1.0
delta = 0.1
n_trials = 500
n_hits = 0

for i in range(n_trials):
    
    print('====trail', i, '=======')
    del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
    
    print(del_x, del_y, x+del_x, y+del_y)
    
    if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
        x, y = x + del_x, y + del_y
    else: print("outside heliport fence")    
    
    if x**2 + y**2 < 1.0: n_hits += 1
    print(x**2 + y**2)
    print(n_hits)
        
        
print(4.0 * n_hits / float(n_trials))
