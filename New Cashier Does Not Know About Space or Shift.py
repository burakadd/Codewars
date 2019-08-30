def get_order(order):
    menu = {
    "burger": 1,
    "fries": 2,
    "chicken": 3, 
    "pizza": 4,
    "sandwich": 5,
    "onionrings": 6,
    "milkshake": 7,
    "coke": 8}
    for dish in menu:
        order = order.replace(dish, f'{dish} ')    
    return " ".join(map(lambda word: word.capitalize(), (sorted(order.strip().split(), key=menu.get))))
