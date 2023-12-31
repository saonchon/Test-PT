import tkinter as tk
import csv

class ProfitAnalysis:
    def __init__(self):
        self.pts = 0

    def price_earning(self, p_e, p_e2):
        self.p_e = p_e
        self.p_e2 = p_e2
        if self.p_e < 18:
            self.pts += 1
        if self.p_e < self.p_e2:
            self.pts += 1

    def return_on_equity(self, roe, roe2):
        self.roe = roe
        self.roe2 = roe2
        if self.roe < 15:
            self.pts += 1
        if self.roe < self.roe2:
            self.pts += 1

    def return_on_asset(self, roa, roa2):
        self.roa = roa
        self.roa2 = roa2
        if self.roa < 5:
            self.pts += 1
        if self.roa < self.roa2:
            self.pts += 1

    def net_profit_margin(self, npm, npm2):
        self.npm = npm
        self.npm2 = npm2
        if self.npm < self.npm2:
            self.pts += 1

    def dividend_yield(self, div, div2):
        self.div = div
        self.div2 = div2
        if self.div < 8:
            self.pts += 1
        if self.div < self.div2:
            self.pts += 1

    def scenario(self, p_price, n_price):
            self.p_price = p_price
            self.n_price = n_price
            if self.n_price < self.p_price:
             x = ((self.p_price - self.n_price) / self.p_price) * 100  # Calculate stop loss
             if x <= 1:
                self.pts += 1
             elif x <= 5:
                self.pts += 2
             elif x <= 10:
                self.pts += 3
             elif x > 10:
                self.pts += 4


x = 0
def stop_loss(p_price, n_price):
    global x
    if p_price > n_price:
        x = ((p_price - n_price) / p_price) * 100
        if x > 10:
            return "The loss exceeds 1:1 zone"
    else:
        x = 0  
    return ""  

     
def analyze_pts(pts):
    if pts <= 4:
        return "Low level of selling suggestion"
    elif pts <= 8:
        return "Moderate level of selling suggestion"
    elif pts <= 13:
        return "High level of selling suggestion"

def save_to_csv():
    with open('companies_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow([
            'Company Purchasing Price', 'Company Up-to-date Price', 'Company P/E', 'Company ROE',
            'Company ROA', 'Company Net Profit Margin', 'Company Dividend Yield', 'Industry P/E',
            'Industry ROE', 'Industry ROA', 'Industry Net Profit Margin', 'Industry Dividend Yield',
            'Points', 'Selling Suggestion', 'Stop Loss Message'
        ])
        # Write data
        writer.writerows(companies_data)

# List to store data for multiple companies
companies_data = []

def on_analyze_button_click():
    global y
    y=0
    
    p_price = float(p_price_entry.get())
    n_price = float(n_price_entry.get())
    p_e = float(p_e_entry.get())
    roe = float(roe_entry.get())
    roa = float(roa_entry.get())
    npm = float(npm_entry.get())
    div = float(div_entry.get())
    p_e2 = float(p_e2_entry.get())
    roe2 = float(roe2_entry.get())
    roa2 = float(roa2_entry.get())
    npm2 = float(npm2_entry.get())
    div2 = float(div2_entry.get())

   
    profit_analysis = ProfitAnalysis()
    profit_analysis.price_earning(p_e, p_e2)
    profit_analysis.return_on_equity(roe, roe2)
    profit_analysis.return_on_asset(roa, roa2)
    profit_analysis.net_profit_margin(npm, npm2)
    profit_analysis.dividend_yield(div, div2)
    profit_analysis.scenario(p_price, n_price)

    # Display results in the result_label
    result_label.config(text=f"Points: {profit_analysis.pts}\n{analyze_pts(profit_analysis.pts)}")
    stop_loss_message = stop_loss(p_price, n_price)
    stop_loss_label.config(text=stop_loss_message)


    # Add data to the list of companies
    companies_data.append((
        p_price, n_price, p_e, roe, roa, npm, div,
        p_e2, roe2, roa2, npm2, div2, profit_analysis.pts, analyze_pts(profit_analysis.pts),stop_loss_message
    ))

# GUI setup
root = tk.Tk()
root.title("Stock Analysis")

# Create and place GUI components
tk.Label(root, text="Company Purchasing Price:").grid(row=0, column=0)
p_price_entry = tk.Entry(root)
p_price_entry.grid(row=0, column=1)

tk.Label(root, text="Company Up-to-date Price:").grid(row=1, column=0)
n_price_entry = tk.Entry(root)
n_price_entry.grid(row=1, column=1)

tk.Label(root, text="Company P/E:").grid(row=2, column=0)
p_e_entry = tk.Entry(root)
p_e_entry.grid(row=2, column=1)

tk.Label(root, text="Company ROE:").grid(row=3, column=0)
roe_entry = tk.Entry(root)
roe_entry.grid(row=3, column=1)

tk.Label(root, text="Company ROA:").grid(row=4, column=0)
roa_entry = tk.Entry(root)
roa_entry.grid(row=4, column=1)

tk.Label(root, text="Company Net Profit Margin:").grid(row=5, column=0)
npm_entry = tk.Entry(root)
npm_entry.grid(row=5, column=1)

tk.Label(root, text="Company Dividend Yield:").grid(row=6, column=0)
div_entry = tk.Entry(root)
div_entry.grid(row=6, column=1)

tk.Label(root, text="Industry P/E:").grid(row=7, column=0)
p_e2_entry = tk.Entry(root)
p_e2_entry.grid(row=7, column=1)

tk.Label(root, text="Industry ROE:").grid(row=8, column=0)
roe2_entry = tk.Entry(root)
roe2_entry.grid(row=8, column=1)

tk.Label(root, text="Industry ROA:").grid(row=9, column=0)
roa2_entry = tk.Entry(root)
roa2_entry.grid(row=9, column=1)

tk.Label(root, text="Industry Net Profit Margin:").grid(row=10, column=0)
npm2_entry = tk.Entry(root)
npm2_entry.grid(row=10, column=1)

tk.Label(root, text="Industry Dividend Yield:").grid(row=11, column=0)
div2_entry = tk.Entry(root)
div2_entry.grid(row=11, column=1)

# Button to trigger analysis
analyze_button = tk.Button(root, text="Analyze", command=on_analyze_button_click)
analyze_button.grid(row=12, column=0, columnspan=2)

# Label to display results
result_label = tk.Label(root, text="")
result_label.grid(row=13, column=0, columnspan=2)

#stop_loss_
stop_loss_label = tk.Label(root, text="")
stop_loss_label.grid(row=14, column=0, columnspan=2)

#savetocsv
save_button = tk.Button(root, text="Save to CSV", command=save_to_csv)
save_button.grid(row=15, column=0, columnspan=2)

# Start the GUI eSvent loop
root.mainloop()

# Display all companies' data after the loop exits
print("All Companies Data:")
for i, data in enumerate(companies_data, start=1):
    print(f"Company {i} Data: {data}")

