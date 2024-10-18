'''
==================================================
Desarrollado por: Pablo Isai Ortiz Angulo
==================================================
'''


import requests
from os import path
import argparse
import sys

parse = argparse.ArgumentParser()
parse.add_argument('-t', '--target', help='indica el dominio de la vistima')
parse = parse.parse_args()



def main():
    if parse.target:
        if path.exists('subdominios.txt'):
            worldlist = open('subdominios.txt','r')
            worldlist = worldlist.read().split('\n')
            