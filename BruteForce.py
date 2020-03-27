from itertools import product
from string import ascii_letters, digits
import argparse

chars = list(ascii_letters+digits)

parser = argparse.ArgumentParser()
parser.add_argument('--chars', help=f'Put your custom chars, default={"".join(chars)}')
args = parser.parse_args()

if args.chars:
    chars = list(args.chars)
    print('Using:', ''.join(chars))
else:
    print('Using:', ''.join(chars))

password = str(input('Insert a password: '))
while len(password) > 4:
    print('Password too long, try a smaller password')
    password = str(input('Insert a password again: '))
print('Generatin the combination...')
combs = list(product(chars, repeat=len(password)))
print('Starting the BruteForce...')
for c in combs:
    c = ''.join(c)

    if c == password:
        print('FOUND -->', c)
        break

