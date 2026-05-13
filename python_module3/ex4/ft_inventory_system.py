import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        parts = arg.split(':')
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name, qty_str = parts
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            qty = int(qty_str)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue
        inventory[name] = qty
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    total = sum(inventory.values())
    print(
        f"Total quantity of the {len(inventory)} items: {total}")
    for i in inventory:
        print(
            f"Item {i} represents {round(inventory[i]/ total * 100, 1)}%")
    keys = list(inventory.keys())
    most = keys[0]
    least = keys[0]
    for k in keys:
        if inventory[k] > inventory[most]:
            most = k
        if inventory[k] < inventory[least]:
            least = k
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
