"""
Finds the store with the cheapest prices for the food you need
"""
import turtle as t
from tkinter import *
import time
t.tracer(0, 0)
t.ht()

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.main_window()

    # Creation of main_window
    def main_window(self):
        # changing the title of our master widget
        self.master.title("Shopping List")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        QuitButton = Button(self, text="Quit", bg="orange", command=self.quit_gui)
        ShoppingListButton = Button(self, text="Enter Items", bg="orange", command=self.enteritem_window)
        ItemButton = Button(self, text="Items", bg="orange", command=self.item_button)
        LoginButton = Button(self, text="Login", bg="orange", command=self.login_button)
        QuitButton.config(height=1, width=15)
        ShoppingListButton.config(height=10, width=15)
        ItemButton.config(height=1, width=5)
        LoginButton.config(height=1, width=5)
        # placing the button on my window
        ShoppingListButton.place(x=140, y=80)
        QuitButton.place(x=140, y=250)
        ItemButton.place(x=140, y=40)
        LoginButton.place(x=230, y=40)



    def quit_gui(self):
        exit()

    def enteritem_window(self):
        self.main_window()
        get_grocery_list(False)
        # Function for Enter Items Button

    def login_button(self):
        t.setworldcoordinates(0,0,100,100)
        user_pass, user_order = file_reader()
        user, user_pass, new = get_user_name(user_pass)
        quick = False
        if not new:
            # The user isn't new and is asked if they want to use their quick order
            print_quick(user_order[user])
            quick = check_yes(t.textinput("Quick Order", "Would you use your quick order?"))
        if not new and quick:
            # if the user is not new and wants to use their quick order
            order = user_order[user]
            order = format_order(order)
            main(order)
            t.up()
            t.goto(50, 95)
            t.write("Prices Printed", align='center', font=("Arial", 32, "normal"))
        else:
            items('store_items.txt')
            get_grocery_list(True, user, user_pass, user_order)


    def item_button(self):
        items('store_items.txt')

        # Function for Item Button


def items(string):
    t.reset()
    t.up()
    item_file = open(string)
    t.setworldcoordinates(0, 1, 100, 100)
    y = 97
    t.up()
    z = 0
    x = 0
    for line in item_file:
        if z == 33:
            x += 33
            y = 97
            z = 0
        t.goto(x, y)
        t.write(line, font=('Arial', 16, 'normal'))
        y -= 3
        z += 1
    t.goto(-100, -100)
    t.update()


def print_quick(lst):
    t.reset()
    t.up()
    y = 80
    x = 0
    z = 0
    t.goto(50, 90)
    t.write("Your Quick Order:", align='center', font=("Arial", 24, "normal"))
    for item in lst:
        if z == 25:
            z = 0
            y = 80
            x += 33
        t.goto(x, y)
        t.write(item + '\n', font=("Arial", 16, "normal"))
        z += 1
        y -= 3
    t.goto(-100, -100)
    t.update()


def format_order(order):
    dct = dict()
    for item in order:
        item = item.split()
        string = (' '.join(item[:-1])).upper()
        dct[string] = float(item[-1])
    return dct


def get_grocery_list(save, user='', user_pass={}, user_order={}):
    dct = dict()
    foods = food_dict()
    string = ''
    while True:
        item = t.textinput("Grocery List", string + "Enter item name, or enter 'stop' when all items entered:")
        string = ''
        item = item.upper()
        if item == 'STOP':
            main(dct)
            t.reset()
            t.setworldcoordinates(0, 0, 100, 100)
            t.goto(50, 50)
            t.write("Prices Printed", align='center', font=("Arial", 32, "normal"))
            t.goto(-100, -100)
            if save:
                if check_yes(t.textinput("Save Order", "Would you like to save this order to quick order?")):
                    dct = dict_format(dct)
                    user_order[user] = dct
                    save_order(user, user_pass, user_order)
            return
        if item in foods:
            if foods[item] == 'LB':
                quantity = t.numinput("Quantity", "Enter the amount in lbs you would like:", 1, 0, 100000000000000)
                dct[item] = quantity
            elif foods[item] == 'OZ':
                quantity = t.numinput("Quantity", "Enter the amount in oz you would like:", 1, 0, 100000000000000)
                dct[item] = quantity
            else:
                quantity = t.numinput("Quantity", "Enter the quantity  you would like:", 1, 0, 100000000000000)
                dct[item] = quantity
        else:
            string = "Item not found. "


def dict_format(dct):
    items = []
    for key, value in dct.items():
        items.append(str(key) + ' ' + str(value))
    return str(items)[1:-1]


def food_dict():
    item_file = open('store_items.txt')
    dct = dict()
    for line in item_file:
        line= line.split()
        dct[' '.join(line[:-1])] = line[-1]
    return dct


def store_prices(string):
    """
    This function takes the lists of items from each store and converts it into a dictionary
    :param string: store file name
    :return: dictionary of store items and prices
    """
    file = open(string)
    dct = dict()
    for line in file:
        line = line.split()
        string = (' '.join(line[:-1])).upper()
        dct[string] = float(line[-1])
    return dct


def save_order(user, user_pass, user_order):
    file = open("users.txt", 'w')
    x = len(user_pass)
    file.write(str(x) + "\n")
    for key, value in user_pass.items():
        file.write(key + '\n')
        file.write(value + '\n')
        string = str(user_order[key])
        if key != user:
            string = string[1:-1]
        print(string)
        file.write(string + '\n')


def check_yes(x):
    """
    checks to see if a string is 'yes'
    :param x: the string
    :return: true if the string is yes, false otherwise
    """
    try:
        x = x.upper()
    except:
        exit()
    if x != 'YES':
        return False
    return True


def find_total_price(dct, groceries):
    """

    :param dct: the dictionary of all items in that store
    :param groceries: the dictionary of groceries needed, and in what amounts
    :return: the total price, and all items not found
    """
    price = 0
    not_found = []
    for key, value in groceries.items():
        if key in dct:
            price += dct[key]*value
        else:
            not_found.append(key)
    return price, not_found


def output(string, price, not_found, outputfile):
    """
    creates a file displaying the information from the program
    :param string: Store name
    :param price: the total price of the items found
    :param not_found: a list of the items that were not found
    :param outputfile: the output file being printed to
    :return: An output file containing the store's information
    """
    outputfile.write(string + ":\n")
    outputfile.write("Total Price: $" + price + '\n')
    if not_found:
        outputfile.write("Items Not Found:\n")
    for item in not_found:
        outputfile.write(item + '\n')
    outputfile.write('\n')


def formatter(price):
    """
    formats the price of each score
    :param price: the price as a float
    :return: the price formatter correctly
    """
    price = str(price)
    for x in range(len(price)):
        if price[x] == '.':
            if len(price[x:]) > 3:
                return price[:x+3]
            elif len(price[x:]) < 3:
                price += '0'
    return price


def file_reader():
    """
    reads the file and creates the dictionaries that contain all the users' information
    :return: the dictionaries containing the users' information
    """
    file = open("users.txt")
    user_pass = {}
    user_order = {}
    Users = file.readline()
    num_users = int(Users[:-1])
    for US in range(num_users):
        name = file.readline()
        name = name[:-1]
        password = file.readline()
        user_pass[name] = password[:-1]
        user_order[name] = all_string(file.readline())
    return user_pass, user_order


def all_string(string):
    """

    :param string: The line that contains the last order
    :return:
    """
    pos = 0
    order = []
    temp = ''
    for x in range(len(string)):
        if string[pos] == ',':
            pos += 2
            order.append(temp)
            temp = ''
        elif string[pos] == "'" or string[pos] == '"':
            pos += 1
        else:
            temp += string[pos]
            pos += 1
        if pos >= len(string)-1:
            order.append(temp)
            break
    return order


def get_user_name(user_pass):
    """
    Users will enter in their usernames
    :return: the updated dictionary of user names and passwords
    """
    check = True
    new = False
    try:
        while check:
            name = t.textinput("Login", "Enter your name, if you're new enter 'new' to make a username")
            clear_error_text()
            if name.upper() == 'NEW':
                user_pass, name, new = new_user(user_pass)
            if len(name) > 20:
                check = True
            elif name not in user_pass:
                error_text("Username not found.")
            else:
                password = t.textinput(name, "Enter your password")
                if password == user_pass[name]:
                    user = name
                    check = False
                else:
                    error_text("Incorrect password.")
        return user,  user_pass, new
    except TypeError:
        exit()


def new_user(user_pass):
    """
    This function is for creating a new username and password
    :return: an updated dictionary of usernames and passwords
    """
    t.clearscreen()
    check = True
    try:
        while check:
            name = t.textinput("Username", "Enter the username you would like, between 1 and 20 characters.\nEnter 'back' to go back")
            clear_error_text()
            if name.upper() == 'BACK':
                return user_pass, "Ignore this name because I said so", False
            if 0 >= len(name) > 20:
                error_text("Name must be between 1 and 20 characters")
            elif name in user_pass:
                error_text("Name taken, choose a different username.")
            elif name.upper() == 'NEW':
                error_text("Nice try but I already thought of that.")
            else:
                password = t.textinput('Password', "Enter in what you would like your password to be.")
                user_pass[name] = password
                return user_pass, name, True
    except TypeError:
        exit()


def error_text(string):
    """
    The text printed on screen to convey a message to the user.
    :param string: The line being printed
    """
    clear_error_text()
    t.up()
    t.goto(50, 50)
    t.write(string, align='center', font=("OCR-A", 16, "normal"))
    t.goto(-100, -100)
    t.update()


def clear_error_text():
    """
    Clears the text written by error_text.
    """
    t.up()
    t.goto(0, 50)
    t.fillcolor("white")
    t.begin_fill()
    for x in range(2):
        t.forward(100)
        t.left(90)
        t.forward(36)
        t.left(90)
    t.end_fill()
    t.goto(-100, -100)
    t.update()


def main(groceries):
    """
    main method that will call all other functions in the program
    """
    stores = dict()
    stores['Wegmans'] = store_prices('wegmans.txt')
    stores['Walmart'] = store_prices('walmart.txt')
    stores['Whole Foods'] = store_prices('wholefoods.txt')
    stores['Price Right'] = store_prices('priceright.txt')
    outputfile = open("groceries.txt", 'w')
    for key, value in stores.items():
        price, not_found = find_total_price(value, groceries)
        price = formatter(price)
        output(key, price, not_found, outputfile)


root = Tk()
root.geometry('400x300')
app = Window(root)
root.mainloop()

