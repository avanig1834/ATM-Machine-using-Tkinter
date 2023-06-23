import os
from tkinter import *
from PIL import ImageTk, Image


class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM")
        self.root.geometry("700x500")
        
        self.show_welcome_page()
        
    def show_welcome_page(self):
        # Welcome Message
        self.welcome_label = Label(root, text="OOPS PROJECT: ATM MAHCINE GUI USING TKINTER", font=("Arial", 18, "bold"))
        self.welcome_label.pack(pady=50)


    
    def register(self):
    # variables
    # stringvar initializes an empty string variable so that it can be used somewhere
        global temp_name
        global temp_age
        global temp_gender
        global temp_password
        global temp_phone
        global notif

        self.temp_name = StringVar()
        temp_age = StringVar()
        temp_gender = StringVar()
        temp_password = StringVar()
        temp_phone = StringVar()
     
        register_screen = Toplevel(master)
        register_screen.title("register")

    # labels for registration function
        self.l1 = Label(register_screen, text="please enter your details below", font=('Calibri,12')).grid(row=0,sticky=N,pady=10)
        self.l2 = Label(register_screen, text="Username", font=('Calibri,12')).grid(row=1,sticky=W)
        self.l3 = Label(register_screen, text="Age", font=('Calibri,12')).grid(row=2,sticky=W)
        self.l4 = Label(register_screen, text="Gender", font=('Calibri,12')).grid(row=3,sticky=W)
        self.l4 = Label(register_screen, text="Password", font=('Calibri,12')).grid(row=4,sticky=W)
        self.l5 = Label(register_screen, text="Phone no.", font=('Calibri,12')).grid(row=5,sticky=W)
        notif = Label(register_screen, font=('Calibri,12'))
        notif.grid(row=7 ,sticky=N,pady=10)

    # entries for registration function
        Entry(register_screen, textvariable=temp_name).grid(row=1, column=0, sticky=E)
        Entry(register_screen, textvariable=temp_age).grid(row=2, column=0, sticky=E)
        Entry(register_screen, textvariable=temp_gender).grid(row=3, column=0, sticky=E)
        Entry(register_screen, textvariable=temp_password, show="*").grid(row=4, column=0, sticky=E)
        Entry(register_screen, textvariable=temp_phone).grid(row=5, column=0, sticky=E)

    # buttons for registration function
        Button(register_screen, text="Register", command=finish_reg, font=('Calibri,12')).grid(row=6,sticky=N,pady=10)












root = Tk()
atm = ATM(root)
root.mainloop()

master = Tk()
master.title("ATM Machine")

#  functions
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    phone = temp_phone.get()
    all_accounts = os.listdir()
    print(all_accounts)
    
    if name == "" or age == "" or gender == "" or password == "" or phone == "":
        notif.config(fg="red",text="all fields required")
        return 
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red", text="Account already exists")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write(phone+'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green", text="Account has been created")
            

def register():
    # variables
    # stringvar initializes an empty string variable so that it can be used somewhere
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global temp_phone
    global notif

    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    temp_phone = StringVar()
     
    register_screen = Toplevel(master)
    register_screen.title("register")

    # labels for registration function
    Label(register_screen, text="please enter your details below", font=('Calibri,12')).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Username", font=('Calibri,12')).grid(row=1,sticky=W)
    Label(register_screen, text="Age", font=('Calibri,12')).grid(row=2,sticky=W)
    Label(register_screen, text="Gender", font=('Calibri,12')).grid(row=3,sticky=W)
    Label(register_screen, text="Password", font=('Calibri,12')).grid(row=4,sticky=W)
    Label(register_screen, text="Phone no.", font=('Calibri,12')).grid(row=5,sticky=W)
    notif = Label(register_screen, font=('Calibri,12'))
    notif.grid(row=7 ,sticky=N,pady=10)

    # entries for registration function
    Entry(register_screen, textvariable=temp_name).grid(row=1, column=0, sticky=E)
    Entry(register_screen, textvariable=temp_age).grid(row=2, column=0, sticky=E)
    Entry(register_screen, textvariable=temp_gender).grid(row=3, column=0, sticky=E)
    Entry(register_screen, textvariable=temp_password, show="*").grid(row=4, column=0, sticky=E)
    Entry(register_screen, textvariable=temp_phone).grid(row=5, column=0, sticky=E)

    # buttons for registration function
    Button(register_screen, text="Register", command=finish_reg, font=('Calibri,12')).grid(row=6,sticky=N,pady=10)


def login_session():
    global login_name
    print("session")
    all_accounts = os.listdir()
    print(all_accounts)
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all_accounts:
        if name == login_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            print(file_data)
            password = file_data[1]

            # account dashboard
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title("Dashboard")

                # labels
                Label(account_dashboard, text="Account Dashboard", font=('Calibri,12')).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard, text="Welcome "+name, font=('Calibri,12')).grid(row=1,sticky=N,pady=5)

                # button
                Button(account_dashboard, text="Personal details", font=('Calibri,12'),width=30, command = personal_details).grid(row=2,sticky=N,padx=10)
                Button(account_dashboard, text="Deposit", font=('Calibri,12'),width=30, command =deposit).grid(row=3,sticky=N,padx=10)
                Button(account_dashboard, text="Withdraw", font=('Calibri,12'),width=30, command = withdraw).grid(row=4,sticky=N,padx=10)
                Button(account_dashboard, text="Update mobile number", font=('Calibri,12'),width=30, command = update).grid(row=5,sticky=N,padx=10)
                Button(account_dashboard, text="Transfer Funds", font=('Calibri,12'),width=30, command = transfer_fund).grid(row=6,sticky=N,padx=10)
                Label(account_dashboard).grid(row=7,sticky=N,pady=10)
                return
            else:
                login_notif.config(fg="red", text="Password incorrect")
                return
    login_notif.config(fg="red", text="No account found")    

# function for transferring funds
def transfer_fund():
    print("done")
    global amount
    global transfer_notif
    global current
    global account_no

    amount = StringVar()
    account_no = StringVar()

    file = open(login_name,"r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[5]

    #  deposit
    transfer_screen = Toplevel(master)
    transfer_screen.title("deposit")

    # labels
    Label(transfer_screen, text="fund transfer", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    current = Label(transfer_screen, text="Current Balance : "+details_balance, font=('Calibri',12))
    current.grid(row=1,sticky=W)

    Label(transfer_screen, text="Amount", font=('Calibri',12)).grid(row=2,sticky=W)
    Label(transfer_screen, text="enter account number", font=('Calibri',12)).grid(row=3,sticky=W)
    transfer_notif = Label(transfer_screen, font=('calibri',12))
    transfer_notif.grid(row=5,sticky=N,pady=5)
    
    # entry
    Entry(transfer_screen, textvariable = amount).grid(row=2,column=1)
    Entry(transfer_screen, textvariable = account_no).grid(row=3,column=1)

    # button
    Button(transfer_screen, text="Finish", font=('Calibri',12),command=finish_transfer).grid(row=4,sticky=W,pady=5)

def finish_transfer():
    if amount.get() == "":
        transfer_notif.config(text="Amount is required",fg="red")
        return
    if account_no.get() == "":
        transfer_notif.config(text="account number requied",fg="red")
        return
    if float(amount.get()) <= 0:
        transfer_notif.config(text="enter valid amount",fg="red")   
        return
    
    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current = details[5]
    updated = current
    updated = float(updated) - float(amount.get())
    file_data = file_data.replace(current,str(updated))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    
    transfer_notif.config(text="transfer successful", fg="green")    
# function for updating mobile number
def update():
    global new_mob_no
    global existing
    global update_notif
    global pin_no
    
    new_mob_no = StringVar()
    pin_no = StringVar()
    file = open(login_name, "r")
    file_data = file.read()
    mobile = file_data.split('\n')
    old_mob_no = mobile[4]

    # update window
    update_screen = Toplevel(master)
    update_screen.title("change mobile number")
    
    # labels
    Label(update_screen, text="mobile number updation", font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    existing = Label(update_screen, text="existing number: "+old_mob_no, font=('Calibri', 12))
    existing.grid(row=1,sticky=W)
    
    Label(update_screen, text="enter new number", font=('Calibri',12)).grid(row=2,sticky=W,pady=10)
    Label(update_screen, text="password", font=('Calibri',12)).grid(row=3,sticky=W,pady=10)
    update_notif = Label(update_screen, font=('Calibri',12))
    update_notif.grid(row=5,sticky=N,pady=5)

    # entry
    Entry(update_screen, textvariable=new_mob_no).grid(row=2, column=1)
    Entry(update_screen, textvariable=pin_no).grid(row=3, column=1)
    
    # Button
    Button(update_screen, text="Finish", font=('Calibri',12),command=check_number).grid(row=4,sticky=W,pady=5)


# check the password entered is correct or not at time of changing mobile number
def check_number():
    
    if new_mob_no.get() == "":
        update_notif.config(text="enter mobile number", fg="red")
        return 
    
    if pin_no.get() != "1834":
        
        print("enter correct pin")
    else:
        print("updated successfully")
        file = open(login_name, 'r+')
        file_data = file.read()
        details = file_data.split('\n')
        current = details[4]
        updated = new_mob_no.get()
        file_data = file_data.replace(current,str(updated))
        file.seek(0)
        file.truncate(0)
        file.write(file_data)
        file.close()

        update_notif.config(text="mobile number updated", fg="green")
    
# function for depositing cash into the atm
def deposit():
    global amount
    global deposit_notif
    global current
    amount = StringVar()
    file = open(login_name,"r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[5]

    #  deposit
    deposit_screen = Toplevel(master)
    deposit_screen.title("deposit")

    # labels
    Label(deposit_screen, text="deposit", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    current = Label(deposit_screen, text="Current Balance : "+details_balance, font=('Calibri',12))
    current.grid(row=1,sticky=W)

    Label(deposit_screen, text="Amount", font=('Calibri',12)).grid(row=2,sticky=W)
    deposit_notif = Label(deposit_screen, font=('calibri',12))
    deposit_notif.grid(row=4,sticky=N,pady=5)
    
    # entry
    Entry(deposit_screen, textvariable = amount).grid(row=2,column=1)

    # button
    Button(deposit_screen, text="Finish", font=('Calibri',12),command=finish_deposit).grid(row=3,sticky=W,pady=5)
    

def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(text="Amount is required",fg="red")
        return
    if float(amount.get()) <= 0:
        deposit_notif.config(text="enter valid amount",fg="red")   
        return
    
    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current = details[5]
    updated = current
    updated = float(updated) + float(amount.get())
    file_data = file_data.replace(current,str(updated))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    

    deposit_notif.config(text="balance updated", fg="green")
# function for withdrawing cash from the atm
def withdraw():
    global withdraw_amount
    global withdraw_notif
    global current
    withdraw_amount = StringVar()
    file = open(login_name,"r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[5]

    #  withdraw
    withdraw_screen = Toplevel(master)
    withdraw_screen.title("deposit")

    # labels
    Label(withdraw_screen, text="withdraw", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    current = Label(withdraw_screen, text="Current Balance : "+details_balance, font=('Calibri',12))
    current.grid(row=1,sticky=W)

    Label(withdraw_screen, text="Amount", font=('Calibri',12)).grid(row=2,sticky=W)
    withdraw_notif = Label(withdraw_screen, font=('calibri',12))
    withdraw_notif.grid(row=4,sticky=N,pady=5)
    
    # entry
    Entry(withdraw_screen, textvariable = withdraw_amount).grid(row=2,column=1)

    # button
    Button(withdraw_screen, text="Finish", font=('Calibri',12),command=finish_withdraw).grid(row=3,sticky=W,pady=5)


def finish_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(text="amount is required", fg="red")
        return 
    if float(withdraw_amount.get()) <= 0:
        withdraw_notif.config(text="enter valid amount", fg="red")
        return
    
    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current = details[5]
    updated = current

    if float(withdraw_amount.get()) > float(current):
        withdraw_notif.config(text="Insufficient fund", fg="red")
        return
    
    updated = float(updated) - float(withdraw_amount.get())
    file_data = file_data.replace(current, str(updated))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    withdraw_notif.config(text="Balance Updated", fg="green")

# function for displaying personal details on atm window
def personal_details():
    # variables
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[3]
    details_balance = user_details[4]

    # personal details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title("Personal Details")

    # labels
    Label(personal_details_screen, text="Personal Details", font=('Calibri,12')).grid(row=0, sticky=N, pady=10)
    Label(personal_details_screen, text="Name : "+details_name, font=('Calibri,12')).grid(row=1, sticky=W)
    Label(personal_details_screen, text="Age : "+details_age, font=('Calibri,12')).grid(row=2, sticky=W)
    Label(personal_details_screen, text="Gender : "+details_gender, font=('Calibri,12')).grid(row=3, sticky=W)
    Label(personal_details_screen, text="Balance : "+details_balance, font=('Calibri,12')).grid(row=4, sticky=W)

# function for logging into the atm
def login():
    # variables
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen

    temp_login_name = StringVar()
    temp_login_password = StringVar()
    # login screen
    login_screen = Toplevel(master)
    login_screen.title("Login")
    # label for login function
    Label(login_screen, text="login to your account", font=('Calibri,12')).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="Username", font=('Calibri,12')).grid(row=1,sticky=W)
    Label(login_screen, text="Password", font=('Calibri,12')).grid(row=2,sticky=W)
    login_notif = Label(login_screen, font=('Calibri,12'))
    login_notif.grid(row=4,sticky=N)

    # entry for login function
    Entry(login_screen,textvariable=temp_login_name).grid(row=1,column=1,padx=5)
    Entry(login_screen,textvariable=temp_login_password, show="*").grid(row=2,column=1,padx=5)

    # button for login function
    Button(login_screen, text=("Login"), command=login_session, width=15, font=('Calibri,12')).grid(row=3,sticky=W,pady=5,padx=5)

# image import
img = Image.open('atm.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

# labels
Label(master, text="WELCOME TO ATM", font=('Calibri',14)).grid(row=0,sticky=N,pady=10)
Label(master, text="the most secure banking system", font=('calibri',12)).grid(row=1,sticky=N)
Label(master, image=img).grid(row=2,sticky=N,pady=15)

# buttons
Button(master, text="register", font=('Calibri',12),width=20,command=register).grid(row=3,sticky=N)
Button(master, text="login", font=('Calibri',12),width=20,command=login).grid(row=4,sticky=N,pady=10)

master.mainloop()
