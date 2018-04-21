#!/bin/env python3
from linked import LinkedQueue as Queue


def print_queue(x, name):
    '''Printing out queues contents'''
    print('-------------')
    print(f'Queue {name}', end='')
    if x.is_empty():
        print('\t is empty')
    else:
        print('')
        x.print_linked()

def main():
    A = Queue()
    B = Queue()
    C = Queue()
    D = Queue()
    customer_number = 0
    for current_time in range(1800):
        if current_time % 300 == 0:
            print_queue(A, 'A')
            print_queue(B, 'B')
            print_queue(C, 'C')
            print_queue(D, 'D')
        if current_time % 10 == 0:
            '''Customers arriving'''
            if customer_number % 2 == 0:
                A.put(customer_number)
            else:
                B.put(customer_number)
            customer_number += 1
        if current_time % 30 == 0:
            '''Processing Payment'''
            if C._size:
                D.put(C.get())
        if current_time % 30 == 0:
            '''Queue A processing order'''
            if A._size:
                C.put(A.get())
        if current_time % 20 == 0:
            '''Queue B processing order'''
            if B._size:
                C.put(B.get())
        if current_time % 20 == 0:
            '''Delivering food'''
            if D._size:
                print('-------------')
                print(f'Order {D.get()} done!', end='\n\n')
    				
if __name__ == '__main__':
    main()
