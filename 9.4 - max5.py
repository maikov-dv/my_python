def max_sequence(seq):
    '''
    Функция ищет пять соседних элементов списка, сумма значений которых максимальна.
    >>> max_sequence([1, 3, 1, 1, 4, 4, 3, 1, 4, 4, 4, 3, 4, 4, 1, 3, 2, 4, 4, 4])
    [4, 4, 4, 3, 4]
    >>> max_sequence([1, 5, 7, 2, 9, 2, 9, 2, 5, 3, 7, 6, 3, 3, 7, 4, 4, 1, 9, 5])
    [7, 2, 9, 2, 9]
    '''
    max_summa = sum(seq[0:5])
    for i in range(1, len(seq)):
        next_summa = sum(seq[i:i+5])
        if i <= len(seq) - 5:
            if next_summa > max_summa:
                max_summa = sum(seq[i:i+5])
                seq1 = seq[i:i+5]
        elif i > len(seq) - 5:
                break
    return seq1

import doctest
doctest.testmod()
