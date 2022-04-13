import login as log
import data as d
des='*'
space=' '
log.login_credentials()
while True:
    print()
    departure_place=input("enter the departure place: ").lower()
    if departure_place in d.places:
        destination_place=input("\nenter the destination place: ").lower()
        if destination_place in d.places:
            print("\nTrain name: "+destination_place+" Express")
            print("\nTotal number of tickets:",d.trains[departure_place][destination_place][0])
            print("\nNumber of available tickets:",d.trains[departure_place][destination_place][1])
            book_ticket=input("Do you want book tickets for your journey in this train. Enter Y for yes and N for no: ")
            if book_ticket=='y':
                num_tickets=int(input("\nenter the number of tickets to be booked: "))
                if num_tickets<=d.trains[departure_place][destination_place][1]:
                    for i in range(1,num_tickets+1):
                        name=input("\nenter the name of the passanger "+str(i)+":").upper()
                        DOB=input("\nenter the date of birth of the passenger "+str(i)+" in the format dd-mm-yyyy: ")
                        verify_num=input("\nenter your adhaar number or pan number: ")
                        print("\nsuccessfully booked ticket for passenger"+str(i)+". Below is the E-Ticket.")
                        print(des*40)
                        print(space*5,"Name:",name)
                        print(space*5,"DOB:",DOB)
                        pnr_user=log.pnr()
                        print(space*5,"PNR Number:",pnr_user,"\n")
                        print(des*40)
                        d.trains[departure_place][destination_place][1]=d.trains[departure_place][destination_place][1]-1
                        opt=input("Do you want to book tickets for your journey once again? If yes enter Y ").lower()
                        if opt=='y':
                            continue
                        else:
                            print("Thanks for booking your tickets through us /n Have a great journey!!!")
                            break
                else:
                    print("All the seats are full at present")
                    break
        else:
            print("There are no direct trains at present")
            opt=input("Do you want to book tickets for your journey once again? If yes enter Y ").lower()
            if opt=='y':
                continue
            else:
                print("Thanks for booking your tickets through us /n Have a great journey!!!")
                break
    else:
        print("There are no trains departing from this place")
        opt=input("Do you want to book tickets for your journey once again? If yes enter Y ").lower()
        if opt=='y':
            continue
        else:
            print("Thanks for booking your tickets through us /n Have a great journey!!!")
            break
    
