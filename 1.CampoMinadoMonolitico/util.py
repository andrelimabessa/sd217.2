def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False
