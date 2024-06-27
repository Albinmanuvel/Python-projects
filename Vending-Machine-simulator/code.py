items = ["apple", "banana", "orange"]
print (items)
while True:
        choice = input("Enter the product name (or 'done' to finish): ").strip()
        if choice.lower() == 'done':
            break
        if choice in products:
            items.append(choice)
        else:
            print("Invalid product name. Please try again.")
    total_cost = calculate_total(items)
        print(f"Total cost: ${total_cost:.2f}")