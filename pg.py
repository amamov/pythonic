"""
    nodemon pg.py
"""
total = 1

for i in range(1, 30):
    total = i * total

print((4 * total + 120) % 31)
