import json

# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        listObj = []
        for user in self.list_of_people:
            dictionary = {"name":user.name,"password":user.password,"age":user.age,"friends": user.friendlist,"inbox":user.inbox,"blocked":user.blocked}
            listObj.append(dictionary)
        with open("sample.json", "w") as outfile:
            json.dump(listObj, outfile, indent=4)

        


    ## For more challenge try this
    def reload_social_media(self, network):
        with open("sample.json", "r") as outfile:
            json_object = json.load(outfile)
        for i, (name, password, age, friends, inbox, blocked) in enumerate(json_object):
           network.list_of_people.append(Person("Adam",1293821, 15))




    def  create_account(self):
        
        name = input("Enter username for account: ")
        password = input("Enter password for account: ")
        age = input("Enter age for account: ")
        return name, age, password



class Person:
    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.password = password
        self.friendlist = []
        self.inbox = []
        self.blocked = []

    def add_friend(self, network):
        person_name = input("Enter name of person: ")
        if person_name in [network.list_of_people[n].name for n, i in enumerate(network.list_of_people)]:
            self.friendlist.append(person_name)
            print(person_name + " added.")
        else: 
            print("Person doesn't exist")
        

    def send_message(self, network):
        friend_name = input("Who's the message for: ")
        if friend_name in [network.list_of_people[n].name for n, i in enumerate(network.list_of_people)]:
            message = input("Enter message: ")
            self.inbox.append([self.name, friend_name, message])
            print("The message " + message + " was sent to " + friend_name)
        else: 
            print("Person doesn't exist")

        

    def view_friends(self):
        print(self.friendlist)
    
    def check_messages(self):
        print("==== Recent Messages ===")
        for i in self.inbox:
            print(i)

    def block_friends(self, network):
        friend_name = input("Who you wanna block: ")
        if friend_name in [network.list_of_people[n].name for n, i in enumerate(network.list_of_people)]:
            self.friendlist.remove(friend_name)
            self.blocked.append(friend_name)
            print(friend_name + " blocked")
        else: 
            print("Person doesn't exist")
