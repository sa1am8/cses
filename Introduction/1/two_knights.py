print('\n'.join(str((i**2*(i**2-1))//2 - 4*(i-1)*(i-2)) for i in range(1, int(input())+1)))