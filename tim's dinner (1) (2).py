# basicallylyl speaking, ,, thiz whole thing iz a variable, yoo dont hav to poot it again, jus type "foodMenu()" and boom
def foodMenu():
    print("»»————-⋅Hi! Welcome to Tim'z Dinner!⋅-————««"
              "\n\n                  Breakfast \n «────── « ⋅ʚ♡ɞ⋅ » ──────»",
              "\n 1. All Day (Large) \t ...£5.50 \n 2. All Day (Small) \t ...£3.50",
              "\n\n \t   Mainz \n «────── « ⋅ʚ♡ɞ⋅ » ──────»",
              "\n 3. Hot Dog  \t \t ...£3.00 \n 4. Burger \t \t ...£4.00 \n 5. Cheese Burger \t ...£4.25 \n 6. Chicken Goujons \t ...£3.50",
              "\n\n \t   Extraz \n «────── « ⋅ʚ♡ɞ⋅ » ──────»",
              "\n 7. Fries \t \t ...£1.75 \n 8. Salad \t \t ...£2.20",
              "\n\n \t   Drinkz \n «────── « ⋅ʚ♡ɞ⋅ » ──────»",
              "\n 9. Milkshake \t ...£2.20 \n 10. Soft Drink \t ...£1.30 \n 11. Still Water \t ...£0.90 \n 12. Sparkling Water \t ...£0.90")
foodMenu()

# menu array so pepl can actualy ordr 
foodItemz = [
                            [1, "All Day (Large)", 5.50],
                            [2, "All Day (Small)", 3.50 ],
                            [3, "Hot Dog", 3.00],
                            [4, "Burger", 4.00],
                            [5, "Cheese Burger", 4.25],
                            [6, "Chicken Goujons", 3.50],
                            [7, "Friez", 1.75],
                            [8, "Salad", 2.20],
                            [9, "Milkshake", 2.20],
                            [10, "Soft Drink", 1.30],
                            [11, "Still Water", 0.90],
                            [12, "Sparkling Water", 0.90]
                    ]
# the order array :]
order = []

# okae, thiz maekz them input tabl numbr, if it not valid (outside 1-10), then yoo repeat again grrr >:[ 
tableNum = int(input("\nPlease input your table number from 1-10: \n"))
print("\nYour table number is:",tableNum)

while tableNum <=0 or tableNum >10:
    print("\nError! Please input a number from 1-10!")
    tableNum = int(input("\nPlease input number from 1-10: \n"))
else:
    order.append(tableNum) # dis jus meanz that the variable "tableNum" iz now [0] of the ordr array, which wuz previously empty

food = int(input("\nPlease enter your itemz from 1-12, press 0 to stop: \n"))
while food != 0:
    order.append(food)
    food = int(input("\nPlease enter your itemz from 1-12, press 0 to stop: \n"))

print("Your order is:\t\n", order)
correctOrder = str(input("Is this correct?\n Reply with Y or N:\n"))

if correctOrder == "Y":
    
