def restock_inventory(available_items, inventory_records, current_day):
    if not current_day % 7 == 0: # Will only run the function on a restock day
        return available_items
    restocked_items = 2000 - available_items
    available_items = 2000
    inventory_records.append(current_day,0,restocked_items,available_items) # Adds the required information to the record for that day

    return available_items
