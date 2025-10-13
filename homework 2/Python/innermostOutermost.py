def infinite_loop():
    return infinite_loop()

def return_first(a, b):
    return a

def test_evaluation_order():
    return return_first(1, infinite_loop())

test_evaluation_order()