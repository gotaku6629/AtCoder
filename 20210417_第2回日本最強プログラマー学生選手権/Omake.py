#!/usr/bin/env python
# coding: utf-8

import math

# 素数を求める「エラトステネスのふるい」
# 1～targetの中から素因数を取り出す
def sieve_of_eratosthenes(target):
    dest = int(math.sqrt(target)) # √N
    target_list = list(range(2, target + 1)) # start～target
    prime_list = []

    while True:
        num_min = min(target_list)
        
        if num_min >= dest:
            prime_list.extend(target_list)
            break
            
        prime_list.append(num_min)
        i = 0
        while True: # num_minで割り切れるものをふるいにかける
            if i >= len(target_list): # target-1
                break
            elif target_list[i] % num_min == 0:
                target_list.pop(i)
            i += 1
    print(prime_list)
    return prime_list

def main():
    A, B =  map(int, input().split())
    S = sieve_of_eratosthenes(B)