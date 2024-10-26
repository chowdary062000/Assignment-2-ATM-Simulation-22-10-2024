def get_amount(self, title):
    # Simple input dialog for amount
    try:
        amount = tk.simpledialog.askinteger(title, "Enter the amount:")
        if amount is None:
            return 0
        elif amount <= 0:
            messagebox.showwarning("Invalid Input", "Please enter a positive amount.")
            return 0
        else:
            return amount
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")
        return 0
