# LABTRACK: A Console-Based Computer Laboratory Inventory System
# LABTRACK: A Console-Based Computer Laboratory Inventory System

# ITE 260 - Computer Programming 1

# Group 7


inventory = []



def get_non_empty(prompt):

    """Ask the user for a value that cannot be empty."""

    while True:

        value = input(prompt).strip()


        if value != "":

            return value


        print("Input cannot be empty.")



def get_positive_integer(prompt):

    """Ask the user for a positive whole number."""

    while True:

        try:

            value = int(input(prompt))


            if value > 0:

                return value


            print("Please enter a number greater than 0.")


        except ValueError:

            print("Invalid input. Please enter a whole number.")



def find_item(item_id):

    """Search for an inventory item using its Item ID."""

    for item in inventory:

        if item[0].lower() == item_id.lower():

            return item


    return None



def add_item():

    """Add a new inventory item."""

    print("\n========== ADD INVENTORY ITEM ==========")


    item_id = get_non_empty("Item ID: ")


    if find_item(item_id) is not None:

        print("Item ID already exists.")

        return


    name = get_non_empty("Item name: ")

    category = get_non_empty("Category: ")

    quantity = get_positive_integer("Quantity: ")


    while True:

        condition = get_non_empty(

            "Condition (Good/Damaged/Missing): "

        ).capitalize()


        if condition in ["Good", "Damaged", "Missing"]:

            break


        print("Please enter Good, Damaged, or Missing.")


    location = get_non_empty("Location: ")


    if condition == "Good":

        status = "Available"

    elif condition == "Damaged":

        status = "Damaged"

    else:

        status = "Missing"


    item = [

        item_id,

        name,

        category,

        quantity,

        condition,

        location,

        status

    ]


    inventory.append(item)


    print("\nItem added successfully.")



def display_items(records=None):

    """Display inventory records."""

    if records is None:

        records = inventory


    if len(records) == 0:

        print("\nNo inventory records found.")

        return


    print("\n================ INVENTORY LIST ================")


    print(

        f"{'ID':<10}"

        f"{'Name':<22}"

        f"{'Category':<18}"

        f"{'Qty':<6}"

        f"{'Condition':<14}"

        f"{'Location':<15}"

        f"{'Status':<12}"

    )


    print("-" * 97)


    for item in records:

        print(

            f"{item[0]:<10}"

            f"{item[1][:20]:<22}"

            f"{item[2][:16]:<18}"

            f"{item[3]:<6}"

            f"{item[4]:<14}"

            f"{item[5][:13]:<15}"

            f"{item[6]:<12}"

        )


    print("-" * 97)



def search_item():

    """Search inventory using an ID, name, category, or location."""

    if len(inventory) == 0:

        print("\nNo inventory records found.")

        return


    keyword = get_non_empty("\nEnter search keyword: ").lower()


    results = []


    for item in inventory:

        if (

            keyword in item[0].lower()

            or keyword in item[1].lower()

            or keyword in item[2].lower()

            or keyword in item[5].lower()

        ):

            results.append(item)


    if len(results) > 0:

        print("\nSearch results:")

        display_items(results)

    else:

        print("\nNo matching inventory item found.")



def update_item():

    """Update an existing inventory item."""

    if len(inventory) == 0:

        print("\nNo inventory records to update.")

        return


    display_items()


    item_id = get_non_empty("\nEnter Item ID to update: ")


    item = find_item(item_id)


    if item is None:

        print("Item not found.")

        return


    print("\n========== UPDATE ITEM ==========")

    print("Press Enter to keep the current value.")


    new_name = input(

        f"Item name [{item[1]}]: "

    ).strip()


    if new_name != "":

        item[1] = new_name


    new_category = input(

        f"Category [{item[2]}]: "

    ).strip()


    if new_category != "":

        item[2] = new_category


    while True:

        new_quantity = input(

            f"Quantity [{item[3]}]: "

        ).strip()


        if new_quantity == "":

            break


        try:

            new_quantity = int(new_quantity)


            if new_quantity > 0:

                item[3] = new_quantity

                break

            else:

                print("Quantity must be greater than 0.")


        except ValueError:

            print("Please enter a valid whole number.")


    while True:

        new_condition = input(

            f"Condition [{item[4]}]: "

        ).strip()


        if new_condition == "":

            break


        new_condition = new_condition.capitalize()


        if new_condition in ["Good", "Damaged", "Missing"]:

            item[4] = new_condition


            if new_condition == "Good":

                item[6] = "Available"

            elif new_condition == "Damaged":

                item[6] = "Damaged"

            else:

                item[6] = "Missing"


            break


        print("Please enter Good, Damaged, or Missing.")


    new_location = input(

        f"Location [{item[5]}]: "

    ).strip()


    if new_location != "":

        item[5] = new_location


    print("\nItem updated successfully.")



def delete_item():

    """Delete an inventory item."""

    if len(inventory) == 0:

        print("\nNo inventory records to delete.")

        return


    display_items()


    item_id = get_non_empty(

        "\nEnter Item ID to delete: "

    )


    item = find_item(item_id)


    if item is None:

        print("Item not found.")

        return


    print(f"\nSelected item: {item[1]}")


    confirmation = input(

        "Are you sure you want to delete this item? (Y/N): "

    ).strip().lower()


    if confirmation == "y":

        inventory.remove(item)

        print("Item deleted successfully.")

    else:

        print("Delete cancelled.")



def check_status():

    """Display damaged and missing inventory items."""

    if len(inventory) == 0:

        print("\nNo inventory records found.")

        return


    results = []


    for item in inventory:

        if (

            item[6].lower() == "damaged"

            or item[6].lower() == "missing"

        ):

            results.append(item)


    if len(results) > 0:

        print("\n========== DAMAGED / MISSING ITEMS ==========")

        display_items(results)

    else:

        print("\nNo damaged or missing items found.")



def show_summary():

    """Calculate and display inventory summary."""

    total_quantity = 0

    available_quantity = 0

    damaged_quantity = 0

    missing_quantity = 0


    for item in inventory:

        total_quantity += item[3]


        if item[6].lower() == "available":

            available_quantity += item[3]


        elif item[6].lower() == "damaged":

            damaged_quantity += item[3]


        elif item[6].lower() == "missing":

            missing_quantity += item[3]


    print("\n========== INVENTORY SUMMARY ==========")

    print(f"Different item records : {len(inventory)}")

    print(f"Total quantity         : {total_quantity}")

    print(f"Available quantity     : {available_quantity}")

    print(f"Damaged quantity       : {damaged_quantity}")

    print(f"Missing quantity       : {missing_quantity}")



def show_menu():

    """Display the main menu."""

    print("\n========== LABTRACK ==========")

    print("1. Add Inventory Item")

    print("2. View Inventory")

    print("3. Search Inventory")

    print("4. Update Inventory")

    print("5. Delete Inventory")

    print("6. Check Damaged/Missing")

    print("7. Inventory Summary")

    print("8. Exit")

    print("==============================")



def main():

    """Run the LabTrack system."""

    while True:

        show_menu()


        choice = input(

            "Choose an option (1-8): "

        ).strip()


        if choice == "1":

            add_item()


        elif choice == "2":

            display_items()


        elif choice == "3":

            search_item()


        elif choice == "4":

            update_item()


        elif choice == "5":

            delete_item()


        elif choice == "6":

            check_status()


        elif choice == "7":

            show_summary()


        elif choice == "8":

            print("\nThank you for using LabTrack!")

            break


        else:

            print("Invalid choice. Please select 1-8.")



main()

