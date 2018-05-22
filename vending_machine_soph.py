#!/usr/bin/python

vending_items = {"Doritos":75, "Gum":25, "Reeses":20, "Mints":15, "Turkey Sandwich":90}
money_value = {"Penny":1, "Nickel": 5, "Dime":10, "Quarter":25}
vending_money_amt = {"Penny":10, "Nickel": 10, "Dime":10, "Quarter":10}

print "1: Item Selection"
print "2: Item Counts"
print "3: Diagnostic Info"
menu_selection = int(raw_input("\nInput your Selection:"))


class Vending_Machine:
    def transaction(self):
        pennies_paid = int(raw_input("Number of pennies:\n"))
        nickels_paid = int(raw_input("Number of nickels:\n"))
        dimes_paid = int(raw_input("Number of dimes:\n"))
        quarters_paid = int(raw_input("Number of quarters:\n"))
        print "Thank you for your purchase!\nDispensing item now..."
        return pennies_paid, nickels_paid, dimes_paid, quarters_paid

    def cash_calculation(self, pennies_paid, nickels_paid, dimes_paid, quarters_paid):
        if pennies_paid != 0:
            vending_money_amt["Penny"] -= pennies_paid
        if nickels_paid != 0:
            vending_money_amt["Nickel"] -= nickels_paid
        if dimes_paid != 0:
            vending_money_amt["Dime"] -= dimes_paid
        if quarters_paid != 0:
            vending_money_amt["Quarter"] -= quarters_paid

    if (menu_selection == 1):
        print "Doritos: 75 cents"
        print "Gum: 25 cents"
        print "Reeses: 20 cents"
        print "Mints: 15 cents"
        print "Turkey Sandwich: 90 cents"
        item_selection = raw_input("Choose your item:")
        if (item_selection == "Doritos"):
            print "Please enter your change\n"
            transaction()
            cash_calculation()
            vending_items["Doritos"] -=1
        elif (item_selection == "Gum"):
            print "Please enter your change\n"
            transaction()
            cash_calculation()
            vending_items["Gum"] -=1
        elif (item_selection == "Reeses"):
            print "Please enter your change\n"
            transaction()
            cash_calculation()
            vending_items["Reeses"] -=1
        elif (item_selection == "Mints"):
            print "Please enter your change\n"
            transaction()
            cash_calculation()
            vending_items["Mints"] -=1
        elif (item_selection == "Turkey Sandwich"):
            print "Please enter your change\n"
            transaction()
            cash_calculation()
            vending_items["Turkey Sandwich"] -=1
        else:
            print "That is not a valid item.\n Please try again."

