from random import choice
import string

test_seq = string.ascii_letters + string.digits + " "


def generate_sequence(size, seq=test_seq, prefix=''):
    return prefix + ''.join(choice(seq) for _ in range(size))
