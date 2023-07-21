import Code

def test_check_quantity_positive():
    result = Code.check_quantity("5")
    assert (result == 5)

def test_check_quantity_negative():
    result = Code.check_quantity("-5")
    assert (result is None)

def test_compute_order_cost_empty():
    result = Code.compute_order_cost({})
    assert (result == 0)

def test_compute_order_cost_over_100_quantity():
    result = Code.compute_order_cost({"1": 101})
    assert (result == -1)

def test_compute_order_cost_over_5_quantity():
    result = Code.compute_order_cost({"1": 6})
    assert (result == 8*6*(1-0.1)) # applying discount

def test_compute_order_cost_over_10_quantity():
    result = Code.compute_order_cost({"2": 11})
    assert (result == 10*11*(1-0.2)) # applying discount

def test_compute_order_cost_over_cost_over_50():
    result = Code.compute_order_cost({"1": 7, "2": 6}) # Order total over 50
    assert (result == (7*8 + 6*10 - 10)) # applying discount

def test_compute_order_cost_over_cost_over_100():
    result = Code.compute_order_cost({"1": 20}) # Order total over 100
    assert (result == 20*8 - 25) # applying discount

# Assuming "Spaghetti" is a "Chef's Specials"
def test_compute_order_cost_special_meal():
    Code.special_food_type.append("Italian") # Make "Italian" a special category
    result = Code.compute_order_cost({"1": 11}) # 11 orders of Spaghetti
    assert (result == 11*8*1.05 - 25) # applying special category charge and special discount

# Clean up after tests
def test_cleanup():
    Code.special_food_type.remove("Italian")
