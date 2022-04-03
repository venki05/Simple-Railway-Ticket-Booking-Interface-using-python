import login as log
import data as d
des='*'
space=' '
log.login_credentials()
while True:
    print()
    departure_place=input("enter the departure place: ").lower()
    if departure_place in d.places:
        print()
        destination_place=input("enter the destination place: ").lower()
        if destination_place in d.places:
            print()
            print("Train name: "+destination_place+" Express")
            print()
            print("Total number of tickets:",d.trains[departure_place][destination_place][0])
            print()
            print("Number of available tickets:",d.trains[departure_place][destination_place][1])
            print()
            book_ticket=input("Do you want book tickets for your journey in this train. Enter Y for yes and N for no: ")
            if book_ticket=='y':
                print()
                num_tickets=int(input("enter the number of tickets to be booked: "))
                if num_tickets<=d.trains[departure_place][destination_place][1]:
                    for i in range(1,num_tickets+1):
                        print()
                        name=input("enter the name of the passanger "+str(i)+":").upper()
                        print()
                        DOB=input("enter the date of birth of the passenger "+str(i)+" in the format dd-mm-yyyy: ")
                        print()
                        verify_num=input("enter your adhaar number or pan number: ")
                        print()
                        print("successfully booked ticket for passenger"+str(i)+". Below is the E-Ticket.")
                        print()
                        print(des*40)
                        print(space*5,"Name:",name)
                        print(space*5,"DOB:",DOB)
                        pnr_user=log.pnr()
                        print(space*5,"PNR Number:",pnr_user)
                        print()
                        print(des*40)
                        d.trains[departure_place][destination_place][1]=d.trains[departure_place][destination_place][1]-1
                else:
                    break
        else:
            print("There are no direct trains at present")
    else:
        print("There are no trains departing from this place")
        departure_place=input("enter the departure place: ").lower()
