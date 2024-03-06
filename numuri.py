# Koda paraugs
# returns True if checksum is valid, otherwise returns False
def Luhn_checks_my_card(card_number):
    total_sum = 0
    total_times = 0

    #Kaut kapēc man master kartei jāmaina skaits... savadāk neiet... es nezinu kapēc lmao
    if len(card_number) == 15:
        x = 1
    elif len(card_number) == 13:
        x = 1
    else:
        x = 0

    #Mans super scuffed algoritms... es nemāku programmēt :((((
    for n in card_number:
        # print(int(n)*2)
        if x == 0:
            if len(str(int(n)*2)) == 2:
                funny_solution = str(int(n)*2)                
                total_times = total_times + int(funny_solution[0]) + int(funny_solution[1])
            else:
                total_times = total_times + (int(n)*2)
            x=1
        elif x ==1:
            total_sum = total_sum + int(n)
            x=0

    total = total_sum + total_times
    # may god forgive my sins
    total = str(total)
    # print(total)
    
    if total[1] == "0":
        return True
    else:
        return False

# returns name of card if digits are valid, otherwise returns "INVALID"
def check_card_type(card_number):
    if str(card_number[0]) == "4":
        return("VISA")
    elif str(card_number[:2]) == "34":
        return("AMEX")
    elif str(card_number[:2]) == "37":
        return("AMEX")
    elif str(card_number[:2]) == "51":
        return("MasterCard")
    elif str(card_number[:2]) == "52":
        return("MasterCard")
    elif str(card_number[:2]) == "53":
        return("MasterCard")
    elif str(card_number[:2]) == "54":
        return("MasterCard")    
    elif str(card_number[:2]) == "55":
        return("MasterCard")    
    else:
        return("INVALID")

# main logic
def main():
    card_number = input("Card number: ")
    if Luhn_checks_my_card(card_number):
        print(check_card_type(card_number))
    else:
        print("INVALID")

if __name__ == "__main__" :
    main()
else:
    ...
