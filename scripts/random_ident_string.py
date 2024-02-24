import random
import string
import streamlit as st

def generate_random_string():
    # Create a pool of characters (letters and digits)
    char_pool = string.ascii_lowercase + string.digits
    random_chars1 = ''.join(random.choices(char_pool, k=3))
    random_chars2 = ''.join(random.choices(char_pool, k=3))
    is_example=False
    return [random_chars1,random_chars2,is_example]