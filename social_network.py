"""The program works for the most part, but I didn't bother adding a login function,
 also the saving and reloading seems a bit buggy but works for the most part.
"""
from  social_network_classes import SocialNetwork,Person
import social_network_ui

ai_social_network = SocialNetwork()
with open("sample.json", 'r') as file:
    if file.read(2) != '[]':
        ai_social_network.reload_social_media(ai_social_network)

guy1 = Person("Adam",1293821, 15)
guy2 = Person("James",129837, 22)
guy3 = Person("Bruh", 12312, 22)
guy4 = Person("Ham", 12309, 50)
ai_social_network.list_of_people.append(guy1)
ai_social_network.list_of_people.append(guy2)
ai_social_network.list_of_people.append(guy3)
ai_social_network.list_of_people.append(guy4)


#Create instance of main social network object

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            name, age, password = ai_social_network.create_account()
            account = Person(name, age, password)
            ai_social_network.list_of_people.append(account)

        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == "1":
                    edit_details_choice = social_network_ui.editDetailsMenu()    
                    if edit_details_choice == "1":
                        account.name = input("Enter new username: ")
                    elif edit_details_choice == "2":
                        account.age = input("Enter new age: ")
                    elif edit_details_choice == "3":
                        account.password = input("Enter new password: ")
                    elif edit_details_choice == "4":
                        break
                elif inner_menu_choice == "2":
                    account.add_friend(ai_social_network)
                elif inner_menu_choice == "3":
                    account.view_friends()
                elif inner_menu_choice == "4":
                    account.check_messages()
                elif inner_menu_choice == "5":
                    account.send_message(ai_social_network)
                elif inner_menu_choice == "6":
                    account.block_friends(ai_social_network)
                elif inner_menu_choice == "7":
                    break
                break
                

        elif choice == "3":
            print("Thank you for visiting. Goodbye!")
            ai_social_network.save_social_media()
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
