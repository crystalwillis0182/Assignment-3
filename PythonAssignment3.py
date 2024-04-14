class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
    
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}")


if __name__ == "__main__":
    print("Item 1")
    name = input("Enter the item name:\n")
    price = int(input("Enter the item price:\n"))
    quantity = int(input("Enter the item quantity:\n"))

    item1 = ItemToPurchase()
    item1.item_name = name
    item1.item_price = price
    item1.item_quantity = quantity

    print("\nItem 2")
    name = input("Enter the item name:\n")
    price = float(input("Enter the item price:\n"))
    quantity = int(input("Enter the item quantity:\n"))

    item2 = ItemToPurchase()
    item2.item_name = name
    item2.item_price = price
    item2.item_quantity = quantity

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    total = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity
    print(f"Total: ${total}")