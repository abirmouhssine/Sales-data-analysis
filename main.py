import pandas as pd
data = pd.read_csv("sales.csv")
print("SALES DATA")
print(data)

data["Revenue"] = data["Quantity"] * data["Price"]
total_revenue = data["Revenue"].sum()
print("Total Revenue:", total_revenue)

product_revenue = data.groupby("Product")["Revenue"].sum()
best_product = product_revenue.idxmax()
print("Revenue by product:")
print(product_revenue)
print("Best selling product:", best_product)

print("Best selling product:", best_product)
total_quantity = data["Quantity"].sum()
print("\n======== SALES REPORT =========")
print("Total Revenue:", total_revenue)
print("Total Quantity Sold:", total_quantity)
print("Best product:", best_product)
print("\nRevenue by Product:")
print(product_revenue)
print("================================")

with open("sales_report.txt", "w")as file:
    file.write("SALES REPORT\n")
    file.write("------------------\n")
    file.write(f"Total Revenue: {total_revenue}\n")
    file.write(f"Total Quantity Sold: {total_quantity}\n")
    file.write(f"Best product: {best_product}\n")
    file.write("\nRevenue by product:\n")
    file.write(product_revenue.to_string())
    print("Report saved successfully!")

import matplotlib.pyplot as plt
plt.figure(figsize=(9, 5))
product_revenue.plot(kind="bar")
plt.title("Sales Revenue Analysis")
plt.xlabel("Products")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)
plt.grid(axis="y",linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()


