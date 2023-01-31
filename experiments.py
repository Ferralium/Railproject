import os

# runs automatically
for j in range(1, 5):
    for k in range(1, 5):
        os.system(f'python3 main.py 5000 5 {j} {k}')