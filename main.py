import pymongo
from profiledb import ProfileDB
from wishlistdb import WishlistDB 

def main():
    profile_db = ProfileDB()
    wishlist_db = WishlistDB()

    print("\nWelcome to WishMate! ------")
    user_input = input("Existing or New User: ") #inputs either E or N

    #Asks new users to create a profile.
    if user_input == "N":
        x = True
        while x:
            #Profile info
            print("\nCreate Your Profile ------")
            username = input("Username: ")
            password = input("Password: ")
            firstname = input("First Name: ")
            lastname = input("Last Name: ")
            zipcode = int(input("ZipCode: "))

            if profile_db.createAccount(username, password, firstname, lastname, zipcode):
                x = False
                print(f"Hi {firstname}! Your profile has been created.")
            
            else:
                print("Username Taken. Try Again.")

    elif user_input == "E":
        y = True
        while y:
            username = input("\nEnter Username: ")
            password = input("Enter Password: ")
        
            if profile_db.userLogin(username, password):
                y = False
                print("Login in Successful.")
        
            else:
                print("Invalid Username and/or Password. Try Again")

    check = True
    while check:

        print("\nChoice ------ ")
        print("1. Create New Wishlist")
        print("2. Add to Existing Wishlist")
        print("3. Remove Item from Existing Wishlist")
        print("4. Show My Wishlist")
        print("5. Show Wishlists Near Me")
        print("6. Links")
        print("7. Exit Program\n")

        user_choice = int(input("Enter choice: "))

        #Creates new wishlist.
        if user_choice == 1:
            new_wishlist = input("New Wishlist: ")
            wishlist_db.createWishlist(username, new_wishlist)

        #Adds item to existing wishlist.
        elif user_choice == 2:
            existing_wishlist = input("Existing Wishlist: ")

            items = []
            print("Items to Add (Enter Twice to Finish):")
            while True:
                item = input()
                if item == "":
                    break
                items.append(item)
            
            wishlist_db.addItems(username, existing_wishlist, items)
        
        #Removes item from existing wishlist.
        elif user_choice == 3:
            existing_wishlist = input("Existing Wishlist: ")
            remove_item = input("Item to Remove: ")
            wishlist_db.removeItem(username, existing_wishlist, remove_item)

        #Prints existing wishlist.
        elif user_choice == 4:
            #existing_wishlist = input("Existing Wishlist: ")
            wishlist_db.showWishlist(username)
        
        #Find public wishlists in the same area.
        elif user_choice == 5:
            wishlist_db.wishlistNearMe(username)

        elif user_choice == 6:
            existing_wishlist = input("Existing Wishlist: ")
            filepath = open("link_n_wishlist.txt", "r")

            for line in filepath:
                line_len = len(line)
                new_line = line[1:line_len - 1].split(",")
                new_line_len = len(new_line)
                item_string = new_line[0]
                item_string += ": " + ", ".join(new_line[1: new_line_len - 1])

                item = [item_string]

                wishlist_db.addItems(username, existing_wishlist, item)

        #Exists program.
        elif user_choice == 7:
            check = False
            print("Exiting WishMate ... :)")
    
        #Invalid inputs.
        else:
            print("Invalid input. Please try again :)\n")

if __name__ == "__main__":
    main()
