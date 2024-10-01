import random

def daily_sales(available_items, inventory_records, current_day):
    if current_day % 7 == 0: # Will only run the function on a sell day
        return available_items
    items_sold = random.randint(0,200) # The amount of items sold is a random integer up to 200
    available_items = available_items - items_sold
    inventory_records.append([current_day,items_sold,0,available_items]) # Adds the required information to the record for that day
    
    return available_items