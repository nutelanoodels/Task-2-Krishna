import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("Cleaned_dataset.xlsx")
print(data.head())
print(data.shape)
print(data.describe())

print(data["Product"].value_counts())#as per the output the most sold item is "printer"
product_sales = data.groupby("Product")["TotalPrice"].sum()
print("total product sales : ", product_sales)#as per this the most sales are given by "chair"
print("payment methods used : ",data["PaymentMethod"].value_counts())#as per this the most used payment method is. "online"

data["Date"] = pd.to_datetime(data["Date"])
data["Month"] = data["Date"].dt.month

monthly_sales = data.groupby("Month")["TotalPrice"].sum()
print("monthly sales : " , monthly_sales)#this gives the monthly sales the maximum sales are in 6th month

#correlation analysis
print(data.corr(numeric_only = True))#this gives how strongly are fields related to eachother

#performing statistical analysis using interquartile range
q1 = data["TotalPrice"].quantile(0.25)
q3 = data["TotalPrice"].quantile(0.75)
iqr = q3-q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
outliars = data[(data["TotalPrice"] < lower) | (data["TotalPrice"] > upper)]
print(outliars)

#visualization
product_sales.sort_values().plot(kind='barh')

plt.xlabel("Revenue")
plt.ylabel("Product")
plt.title("Revenue by Product")
plt.grid(axis="x", linestyle=":", alpha=0.5)
plt.tight_layout()

plt.savefig("revenue_by_product.png", dpi=300)

plt.show()#this suggest that the most soled product is chair > printer > laptop > tablet > monitor > desk > phone
# it can be said that among all the catagories chair and printer generates the most revenue and phone generates the least
