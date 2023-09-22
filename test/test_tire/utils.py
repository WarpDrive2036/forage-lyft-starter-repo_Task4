import random

def add_years_to_date(original_date, years_to_add):
    result = original_date.replace(year=original_date.year + years_to_add)
    return result



def TireSesnorArray():
    random_numbers = [random.uniform(0, 1) for _ in range(4)]
    return random_numbers
