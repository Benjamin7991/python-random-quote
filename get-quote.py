#!/usr/bin/env python3

import random
#def random_quote():
list = []
with open("quotes.txt", "r") as f:
    f_contents = f.readlines()

print(random.choice(f_contents))
