import numpy as np
import matplotlib.pyplot as plt

data = [
    ('Единая Россия', 324, '#0039A6'),
    ('КПРФ', 57, '#EE1C25'),
    ('Справедливая Россия - За Правду', 27, '#FF9E1B'), 
    ('ЛДПР', 21, '#1E3C8C'),  
    ('Новые Люди', 13, '#56C5D0'), 
    ('Гражданская Платформа', 1, '#652D90'),  
    ('Партия Роста', 1, '#99D9EA'),  
    ('Партия Родина', 1, '#EE1C25'), 
    ('Независимые депутаты', 5, '#A7A9AC')  
]

def generate_hemicycle(n_seats, n_rows=8):
    seats = []
    phi = np.pi * 0.8 
    
  
    seats_per_row = []
    remaining = n_seats
    for row in range(n_rows):
        seats_in_this_row = remaining // (n_rows - row)
        seats_per_row.append(seats_in_this_row)
        remaining -= seats_in_this_row
    
    
    for row, n in enumerate(seats_per_row):
        radius = 7 + row * 0.8
        angles = np.linspace(np.pi/2 + phi/2, np.pi/2 - phi/2, n)
        x = radius * np.cos(angles)
        y = radius * np.sin(angles)
        seats.extend(list(zip(x, y)))
    
    return seats

positions = generate_hemicycle(450)

start_idx = 0
for party, seats, color in data:
    end_idx = start_idx + seats
    x = [p[0] for p in positions[start_idx:end_idx]]
    y = [p[1] for p in positions[start_idx:end_idx]]
    plt.scatter(x, y, c=color, s=40, label=f'{party} ({seats})')
    start_idx = end_idx

plt.text(0, 1, '450', fontsize=24, fontweight='bold', ha='center')

plt.axis('equal')
plt.axis('off')
plt.legend(bbox_to_anchor=(1.25, 1), loc='right')
plt.subplots_adjust(right=0.75)
plt.show()

