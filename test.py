# -*- coding: utf-8 -*-
"""
Created on 7/24/2022

@author: kunz5
"""

def main():

    step = 0

    #run through the steps of getting the user's address/zipcode
    while(1):

        if(step==0):
            #let the user decide whether they'd like to use a zip code or full address
            while(1):
                #display the command options and get input from the user
                print("\n1) Find location via zip code")
                print("2) Find location via address")
                print("3) Quit")
                uin = input("Please enter corresponding number of the option you'd like: ")

                #run the correct command
                if(uin != "" and uin[0] == '1'):
                    use_address = False
                    step = 4
                    break
                elif(uin != "" and uin[0] == '2'):
                    use_address = True
                    step = 1
                    break
                elif(uin != "" and uin[0] == '3'):
                    return
                else:
                    print("Invalid input. Please enter a valid command")

        elif(step == 1):
            #get the user's street address
            street = input("\nPlease enter your street address (or enter \"back\" to return to the previous step): ")

            #run the correct command
            if(street != "" and street == "back"):
                step -= 1
            else:
                step += 1

        elif(step == 2):
            #get the user's city
            city = input("\nPlease enter your city (or enter \"back\" to return to the previous step): ")

            #run the correct command
            if(city != "" and city == "back"):
                step -= 1
            else:
                step += 1

        elif(step == 3):
            #get the user's state
            state = input("\nPlease enter your state (or enter \"back\" to return to the previous step): ")

            #run the correct command
            if(state != "" and state == "back"):
                step -= 1
            else:
                step += 1

        elif(step == 4):
            #get the user's zip code
            zipcode = input("\nPlease enter your zipcode (or enter \"back\" to return to the previous step): ")

            #run the correct command
            if(zipcode != "" and zipcode == "back"):
                if(use_address):
                    step = 3
                else:
                    step = 0
            else:
                step += 1

        else:
            break

    #display results
    print("\nHere are the 5 closest locations to you:")
    print("1234 Super St. Corvallis, OR 97331")
    print("5969 Crazy Frog Ln. Albany, OR 92786")
    print("1279 Ducks-Suck Ave. Eugene, OR 80085")
    print("4464 Parkington Ln. Beaverton, OR 28678")
    print("9034 Beach Dr. Astoria, OR 98254")

main()