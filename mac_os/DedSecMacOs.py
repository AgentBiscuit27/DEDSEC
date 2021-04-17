from subprocess import run, PIPE
from time import sleep


def generate_message():
    p = run(['grep', 'T'], stdout=PIPE,
            input='THIS IS DEDSEC! There is no escape!', encoding='ascii')
    return p.stdout.strip()


for spam in range(1, 101):
    print(spam, generate_message())
    sleep(1)
