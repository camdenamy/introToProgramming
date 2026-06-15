num_pizza = int(input())
PIZZA_PRICE = 14.99
TAX = 0.08

subtotal = num_pizza * PIZZA_PRICE
total = subtotal * TAX + subtotal

print(f"Pizzas: {num_pizza}\nSubtotal: ${subtotal:.2f}\nTotal due: ${total:.2f}")