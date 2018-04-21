#!/bin/env python3
from queue import Queue

A = Queue()
B = Queue()
C = Queue()
D = Queue()

def print_queue(x, name):
    y = x
    print('-------------')
    print(f'Queue {name}', end='')
    if y.qsize() == 0:
        print('\tIs empty')
    else:
        print('')
    for value in range(y.qsize()):
        print(y.get(), end=', ')
    print('')

def main():
    customer_number = 0
    for current_time in range(1800):
        if current_time % 300 == 0:
            print_queue(A, 'A')
            print_queue(B, 'B')
            print_queue(C, 'C')
            print_queue(D, 'D')
        if current_time % 10 == 0:
            if customer_number % 2 == 0:
                A.put(customer_number)
            else:
                B.put(customer_number)
            customer_number += 1
        if current_time % 10 == 0:
            if C.qsize():
                D.put(C.get())
        if current_time % 20 == 0:
            if A.qsize():
                C.put(A.get())
        if current_time % 20 == 0:
            if B.qsize():
                C.put(B.get())
        if current_time % 10 == 0:
            if D.qsize():
                print('-------------')
                print(f'Order {D.get()} done!', end='\n\n')
    				
if __name__ == '__main__':
    main()
