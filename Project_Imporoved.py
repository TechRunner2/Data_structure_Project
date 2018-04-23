#!/bin/env python3
from linked import LinkedQueue as Queue


def print_queue(*args):
    '''Printing out queues contents'''
    for queue in args:
        print('-------------')
        print(f'Queue {queue[1]}', end='')
        if queue[0].is_empty():
            print('\t is empty')
        else:
            print('')
            queue[0].print_linked()

def main():
    A = Queue()
    B = Queue()
    C = Queue()
    D = Queue()
    customer_number = 0
    for current_time in range(1800):
        if current_time % 300 == 0:
            print_queue((A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'))
        if current_time % 10 == 0:
            if customer_number % 2 == 0:
                A.put(customer_number)
            else:
                B.put(customer_number)
            customer_number += 1
        if current_time % 10 == 0:
            if C._size:
                D.put(C.get())
        if current_time % 20 == 0:
            if A._size:
                C.put(A.get())
        if current_time % 20 == 0:
            if B._size:
                C.put(B.get())
        if current_time % 10 == 0:
            if D._size:
                print('-------------')
                print(f'Order {D.get()} done!', end='\n\n')
    				
if __name__ == '__main__':
    main()
