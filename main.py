def paritate_m(l: list[int]) -> int:
    count = 0
    for i in l:
        if i % 2 == 0:
            count += 1
    return count

def intersect(l1: list[int], l2: list[int]) -> list[int]:
    l_final = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                l_final.append(l1[i])
    return l_final

def palind(l1: list[int], l2: list[int]) -> list[int]:
    if len(l1) < len(l2):
        lenmin = len(l1)
    else:
        lenmin = len(l2)
    listaf = []
    for i in range(l2):
        if l1[i] == l1[i::-1]:
            listaf.append(l1+l2)
    return listaf
def citire_lista(lista_string: list[int]) -> list[int]:
    lista = []
    len_lista = lista_string.split(',')
    for x in len_lista:
        lista.append(int(x))
    return(lista)

def meniu():
    print('''
    1 -> Citire 2 mulțimi cu numere întregi.
    2 -> Afișare egalitate număr de elemente pare dintre cele 2 mulțimi.
    3 -> Afișare elemente intersectate dintre cele 2 multimi.
    4 -> Afișare palindroame multimi.
    x -> Închide
    '''
    )

def main():
    while True:
        meniu()
        optiune = input('Alege una dintre opțiunile afișate mai sus: ')
        if optiune == '1':
            sir = input('Mulțimea A: ')
            A = citire_lista(sir)
            sir = input('Mulțimea B: ')
            B = citire_lista(sir)
        elif optiune == '2':
            if(paritate_m(A) == paritate_m(B)):
                print('Cele doua mulțimi au un număr egal de elemente pare.')
            else:
                print('Cele două mulțimi NU au un număr egal de elemente pare.')
        elif optiune == '3':
            inter = intersect(A, B)
            if len(inter) > 0:
                print(f'Intersectia dintre multimile A si B este: {inter}.')
            else: print('Multimile A si B nu au elemente intersectate.')
        elif optiune == '4':
            l_palind = palind(A,B)
            if len(l_palind) > 0:

        elif optiune == '5':

        elif optiune == 'x':
            break
        else:
            print('Opțiunea pe care ați ales-o nu există! Reîncercați.')

if __name__ == '__main__':
    main()