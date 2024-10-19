import threading
import time

def print_numbers():
    for c in range (6):
        print(f" I'm  {c} number")

def print_letters():
    for c in ["a","b","c","d","f"]:
        print(f" letter {c}")

thread_letter = threading.Thread(print_numbers,args=[])
thread_numbers = threading.Thread(print_letters)

thread_letter.