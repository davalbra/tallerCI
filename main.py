import sys

# Tabla de alimentos y sus precios
food_options = {
    "1": {"name": "Spaghetti", "type": "Italian", "price": 8},
    "2": {"name": "Sushi", "type": "Japanese", "price": 10},
    "3": {"name": "Tacos", "type": "Mexican", "price": 6},
}

# Descuentos disponibles
discount_rules = {
    5: 0.1,   
    10: 0.2   
}

# Descuentos especiales basados en la suma total
special_discount_rules = {
    50: 10,   
    100: 25   
}

# Alimentos de categoría especial
special_food_type = ["Chef's Specials"]

# Máximo permitido de alimentos en un pedido
max_items_per_order = 100

def show_menu():
    print("Menu:")
    for key, value in food_options.items():
        print(f"{key}. {value['name']} ({value['type']}): ${value['price']}")

def request_user_input(message):
    try:
        return input(message)
    except KeyboardInterrupt:
        print("\nPedido cancelado.")
        sys.exit()

def check_quantity(amount):
    try:
        amount = int(amount)
        if amount > 0:
            return amount
        else:
            return None
    except ValueError:
        return None

def compute_order_cost(order, food_options):  # Aquí está el cambio
    total_price = 0
    for food, amount in order.items():
        cost = food_options[food]['price']
        total_price += cost * amount

    # Aplicar descuento si aplica
    if len(order) > max(discount_rules.keys()):
        total_price *= (1 - max(discount_rules.values()))

    # Aplicar descuento especial si aplica
    for limit, discount in special_discount_rules.items():
        if total_price > limit:
            total_price -= discount

    # Añadir recargo para comidas especiales
    for food, amount in order.items():
        if food_options[food]['type'] in special_food_type:
            total_price += food_options[food]['price'] * amount * 0.05

    return total_price

def validate_order(order):
    # Verificar si los alimentos seleccionados están en el menú
    for food in order.keys():
        if food not in food_options:
            print(f"Error: '{food}' no es una opción válida.")
            return False

    # Verificar si la cantidad de alimentos es válida
    for amount in order.values():
        if amount is None:
            print("Error: Cantidad inválida.")
            return False

    # Verificar si la cantidad total de alimentos excede el límite
    total_amount = sum(order.values())
    if total_amount > max_items_per_order:
        print(f"Error: Se ha superado el límite de cantidad máxima. Máximo: {max_items_per_order}")
        return False

    return True

def finalize_order(order, total_price):
    print("\nComidas seleccionadas:")
    for food, amount in order.items():
        print(f"{food_options[food]['name']} ({food_options[food]['type']}): {amount} x ${food_options[food]['price']}")

    print(f"\nCosto Total: ${total_price}")

    user_choice = request_user_input("\n¿Confirmar el pedido? (S/N): ").lower()

    if user_choice == 's':
        return total_price
    else:
        print("Pedido cancelado.")
        return -1

def run_order_system():
    show_menu()

    order = {}
    while True:
        food = request_user_input("\nIngrese el número de la comida a pedir (o 'done' para terminar): ")

        if food == 'done':
            break

        amount = request_user_input("Ingrese la cantidad deseada: ")
        amount = check_quantity(amount)

        if amount is None:
            print("Error: Cantidad inválida. Ingrese un entero positivo.")
            continue

        order[food] = amount

    if not validate_order(order):
        return -1

    total_price = compute_order_cost(order, food_options)  # Aquí está el cambio
    return finalize_order(order, total_price)

if __name__ == '__main__':
    order_result = run_order_system()
    if order_result != -1:
        print(f"\n¡Gracias por su pedido! Costo total: ${order_result}")
