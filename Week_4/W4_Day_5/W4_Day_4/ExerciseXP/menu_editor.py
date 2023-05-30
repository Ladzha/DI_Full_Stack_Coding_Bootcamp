from menu_manager import MenuManager
from menu_item import MenuItem

def show_user_menu():
    user_choice= input(
'''What do you want to do?
View an Item (V)
Add an Item (A)
Delete an Item (D)
Update an Item (U)
Show the Menu (S)
''').lower()
    while True:
        if user_choice == 'v':
            MenuManager.get_by_name('Salat')
            break      
        elif user_choice == 'a':
            add_item_to_menu()
            break
        elif user_choice == 'd':
            remove_item_from_menu()
            break
        elif user_choice == 'u':
            update_item_from_menu()
            break
        elif user_choice == 's':
            show_restaurant_menu()
            break
        else:
            print('Try again')
            user_choice= input(
'''What do you want to do?
View an Item (V)
Add an Item (A)
Delete an Item (D)
Update an Item (U)
Show the Menu (S)
''').lower()

def add_item_to_menu():
    user_item=input("Put item and price, sepatated by space: ") 
    user_list = user_item.split()
    try:
        user_list[1] = int(user_list[1])
        user_item = MenuItem(user_list[0], user_list[1])
        user_item.save()
        print('Item was added successfully')
    except:
        print('Wrong value')
    finally:
        show_user_menu()
    
def remove_item_from_menu():
    user_item=input("Put the name of item to delete: ")
    
    user_item = MenuItem(user_item)
    if user_item:
        user_item.delete()
        print('Item was deleted successfully')
    else:
        print('Wrong value')

    show_user_menu()

def update_item_from_menu():
    user_item_name=input("Put item name: ")
    user_item_price=input("Put item price: ")  
    try:
        user_item = MenuItem(user_item_name, user_item_price)
        user_item.update(user_item_name, user_item_price)
        print('Item was added successfully')
    except:
        print('Wrong value')
    finally:
        show_user_menu()

def show_restaurant_menu():
    
    items_menu = MenuManager.all_items()
    if items_menu:
        print("Restaurant Menu:")
        for item in items_menu:
            print(f"{item[0]}: ${item[1]}")
show_user_menu()