chess = input().split('/')

for fen in chess:
    for index, val in enumerate(fen):
        if val.isdigit():
            for _ in range(int(val)):
                print('O', end = ' ')
        else:
            if fen[len(fen) - 1] == index:
                print(val, end = '')
            else: 
                print(val, end = ' ')
    print()
    