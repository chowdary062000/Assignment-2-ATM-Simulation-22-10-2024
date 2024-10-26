ATM_PIN
import tkinter as tk
from tkinter import messagebox

# Define the correct ATM PIN and other constants
correct_ATM_PIN = "1234"
DEPOSIT_LIMIT = 50000
WITHDRAWAL_LIMIT = 20000
account_balance = 1000
transaction_history = []

# Function to validate the ATM PIN
def validate_pin():
    entered_pin = pin_entry.get()
    if entered_pin == correct_ATM_PIN:
        messagebox.showinfo("Success", "PIN verified successfully.")
        show_account_menu()
    else:
        messagebox.showerror("Error", "Incorrect PIN. Please try again.")

# Function to show account options
def show_account_menu():
    # Destroy previous PIN entry screen
    pin_frame.destroy()

    # Create a new frame for account options
    global account_frame
    account_frame = tk.Frame(root)
    account_frame.pack(pady=20)

    tk.Label(account_frame, text="=== Account Menu ===").pack()

    options = [
        "Fast Withdrawal Options", "Withdrawal Options", "Deposit Options",
        "Change ATM PIN", "Mini Statement (Last 5 Transactions)",
        "Show Withdrawal Limits", "Check Account Balance", "Transfer Funds",
        "Bill Payment", "Exit"
    ]

    for i, option in enumerate(options, start=1):
        tk.Button(account_frame, text=option, command=lambda i=i: handle_menu_choice(i)).pack(fill='x')

# Function to handle menu choices
def handle_menu_choice(choice):
    if choice == 1:
        fast_withdrawal_options()
    elif choice == 2:
        withdrawal_options()
    elif choice == 3:
        deposit_options()
    elif choice == 4:
        change_atm_pin()
    elif choice == 5:
        mini_statement()
    elif choice == 6:
        show_withdrawal_limits()
    elif choice == 7:
        check_account_balance()
    elif choice == 8:
        transfer_funds()
    elif choice == 9:
        bill_payment()
    elif choice == 10:
        confirm_exit()

# Example function to handle withdrawal
def withdrawal_options():
    def process_withdrawal():
        amount = int(withdraw_entry.get())
        global account_balance
        if amount > WITHDRAWAL_LIMIT:
            messagebox.showerror("Error", f"Withdrawal limit exceeded. Max: {WITHDRAWAL_LIMIT}.")
        elif amount > account_balance:
            messagebox.showerror("Error", f"Insufficient funds. Balance: {account_balance}.")
        else:
            account_balance -= amount
            transaction_history.append(f"Withdrew ${amount}")
            messagebox.showinfo("Success", f"Successfully withdrew ${amount}. New balance: ${account_balance}.")

    withdrawal_frame = tk.Frame(root)
    withdrawal_frame.pack(pady=20)

    tk.Label(withdrawal_frame, text="Enter amount to withdraw (max $20,000):").pack()
    withdraw_entry = tk.Entry(withdrawal_frame)
    withdraw_entry.pack()

    tk.Button(withdrawal_frame, text="Withdraw", command=process_withdrawal).pack()

# Function to handle deposits (example)
def deposit_options():
    def process_deposit():
        amount = int(deposit_entry.get())
        global account_balance
        if amount > DEPOSIT_LIMIT:
            messagebox.showerror("Error", f"Deposit limit exceeded. Max: ${DEPOSIT_LIMIT}.")
        else:
            account_balance += amount
            transaction_history.append(f"Deposited ${amount}")
            messagebox.showinfo("Success", f"Successfully deposited ${amount}. New balance: ${account_balance}.")

    deposit_frame = tk.Frame(root)
    deposit_frame.pack(pady=20)

    tk.Label(deposit_frame, text="Enter amount to deposit (max $50,000):").pack()
    deposit_entry = tk.Entry(deposit_frame)
    deposit_entry.pack()

    tk.Button(deposit_frame, text="Deposit", command=process_deposit).pack()

# Function to confirm exit
def confirm_exit():
    if messagebox.askyesno("Exit", "Do you really want to exit?"):
        root.quit()

# Main ATM GUI setup
root = tk.Tk()
root.title("ATM Interface")
root.geometry("400x400")

# PIN Entry frame
pin_frame = tk.Frame(root)
pin_frame.pack(pady=20)

tk.Label(pin_frame, text="Enter your ATM PIN:").pack()

pin_entry = tk.Entry(pin_frame, show="*")
pin_entry.pack()

tk.Button(pin_frame, text="Submit", command=validate_pin).pack()

# Run the application
root.mainloop()
