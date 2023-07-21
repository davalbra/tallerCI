from main import compute_order_cost

def test_compute_order_cost_under_5_quantity():
    food_options = {
        "1": {"name": "Spaghetti", "type": "Italian", "price": 5},
        "2": {"name": "Sushi", "type": "Japanese", "price": 5},
    }
    order = {"1": 3, "2": 1}  
    assert compute_order_cost(order, food_options) == 20

def test_compute_order_cost_over_5_quantity():
    food_options = {
        "1": {"name": "Spaghetti", "type": "Italian", "price": 5},
        "2": {"name": "Sushi", "type": "Japanese", "price": 5},
    }
    order = {"1": 4, "2": 2}  
    assert compute_order_cost(order, food_options) == 30

def test_compute_order_cost_over_10_quantity():
    food_options = {
        "1": {"name": "Spaghetti", "type": "Italian", "price": 5},
        "2": {"name": "Sushi", "type": "Japanese", "price": 5},
    }
    order = {"1": 6, "2": 5}  
    assert compute_order_cost(order, food_options) == 45

def test_compute_order_cost_special_meal():
    food_options = {
        "1": {"name": "Spaghetti", "type": "Italian", "price": 5},
        "2": {"name": "Sushi", "type": "Japanese", "price": 5},
        "3": {"name": "Chef's Special", "type": "Chef's Specials", "price": 10}
    }
    order = {"1": 3, "3": 2}  
    assert compute_order_cost(order, food_options) == 36.0  

def test_compute_order_cost_total_over_50():
    food_options = {
        "1": {"name": "Spaghetti", "type": "Italian", "price": 10},
        "2": {"name": "Sushi", "type": "Japanese", "price": 15},
    }
    order = {"1": 3, "2": 4}  
    assert compute_order_cost(order, food_options) == 80

def test_compute_order_cost_total_over_100():
    food_options = {
        "1": {"name": "Spaghetti", "type": "Italian", "price": 15},
        "2": {"name": "Sushi", "type": "Japanese", "price": 20},
    }
    order = {"1": 4, "2": 5}  
    assert compute_order_cost(order, food_options) == 125
# hello