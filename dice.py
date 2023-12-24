import random



n = 1

while True:
    no = random.randint(1,6)
    
    if no == 1:
        print('''
[       ]            
[   0   ]
[       ]

''')
    elif no == 2:
        print('''
[0      ]            
[       ]
[      0]

''')
    elif no == 3:
        print('''
[0      ]            
[   0   ]
[      0]

''')
    elif no == 4:
        print('''
[0     0]            
[       ]
[0     0]

''')
    elif no == 5:
        print('''
[0     0]            
[   0   ]
[0     0]

''')
    elif no == 6:
        print('''
[0     0]            
[0     0]
[0     0]

''')
        
    ask = input("press y to roll again and n to exit: ")
    if ask == "y":
        continue
    elif ask == "n":
        break

    
