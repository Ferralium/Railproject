import os

os.system(f'python3 main.py 5000 1')
os.system(f'python3 main.py 5000 2')

# Runs automatically
for i in range(1, 3):
    for j in range(1, 5):
        for k in range(1, 5):
            os.system(f'python3 main.py 5000 {i + 2} {j} {k}')