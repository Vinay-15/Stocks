import csv

class stocks():
    def __init__(self):
        with open('recipe.csv', 'r') as file:  # Opens the file from the same directory
            csv_r = csv.reader(file)           # reads the file
            items = []                         # assigning empty lists
            products = []
            for k in csv_r:                    # for each row in the csv file
                items.append(k[0])             # appending each row's (first element) of csv file to the list
                products.append(k[1:])         # appending the ingredients
            self.menu = {}                     # assigning an empty dictionary
            for i in range(len(items)):
                self.menu[items[i]] = products[i]     # assigning product name with the ingredients needed ti the dictionary
            print(f"Menu : {list(self.menu.keys())}") # printing thr dictionary keys (product names)

        with open('sku.csv', 'r') as pre:      # opening another csv file sku
            csv_pre = csv.reader(pre)
            self.sku = []                      # assigning an empty list
            for l in csv_pre:                  # for each row in the csv file
                self.sku.append(l[0])          # appending its first element to the list
            self.sku.sort()                    # sorting the sku in alphabetical order
            #print(f"Stock keeping units : {self.sku}")


    def stock_order(self):                     # This function tells you the quantity of ingredients required to make the a Product
        inp = input("Enter list of product and quantity in the format (Product-quantity,Product-Quantity) : ").split(',')
        for m in inp:
            prod = m.split('-')[0]             # splitting to get the product name
            quantity = int(m.split('-')[1])    # splitting to get the quantity
            print(f"Ingredients needed to make {quantity} {prod}'s are:")
            print('-' * 30)                    # for table like view
            print("%-20s %-9s" %('Product','Quantity'))
            print('-' * 30)
            for p in self.menu:                # checking for the products in the recipe list
                if p==prod:
                    val = self.menu[p]         # getting the ingredients of the product
                    for i in val:
                        ite = i.split('-')[0]  # splitting the ingredients and the quantity
                        l = i.split('-')[1]    # contains the units
                        m = int(l.split(' ')[0]) # contains the quantity (integer value)
                        quant = str(m*quantity)+l.split(' ')[1] # multiplying it with the quantity required
                        print("%-20s %-4s" %(ite,quant))
            print('-' * 30)


    def add_recipe(self):                      # This functions adds the recipe's to the csv file
        item_name = input('Enter the item name to be added : ')  # input of the product name
        n = int(input('Enter the number of ingridients:'))  # number of ingredients required to make that product
        recipe_items=[]                        # assigning empty lists
        recipe_name=[]
        item_ele=[]
        count=0
        for i in range(n):
            ing_name=input("Enter the ingredient's name : " )  # takes the ingredient name
            ing_quant=input("Enter the quantity ex(100 g) : ") # takes the quantity along with units
            recipe_name.append(ing_name)       # appending the ingredients name
            item = ing_name+'-'+ing_quant      # ingredient name and quantity in a format
            recipe_items.append(item)          # appending the item
        for j in recipe_name:                  # iterating through the ingredient names
            if j not in self.sku:              # checking whether they are present in the list of sku's
                print(f"{j} is not in the Stock")
                count+=1                       # incrementing count
            else:
                item_ele=[item_name]+recipe_items # if ingredient is in sku then added to the list item_ele
        if count==0:                           # checking if the count is 0 (i.e, all ingredients are in sku)
            with open('recipe.csv', 'a', newline='') as f: # opening a csv file named recipe
                writer = csv.writer(f)
                writer.writerow(item_ele)      # writing the whole item_ele into the new line of csv file



obj = stocks()                                 # creating an object of the class stocks()

obj.stock_order()                              # function to get the stock order of certain products
obj.add_recipe()                               # function to write recipes to the csv file
#print(obj.sku)                                # to print the sku's in alphabetical order


