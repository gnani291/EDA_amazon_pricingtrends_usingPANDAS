import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("amazon.csv")

#Clean numeric columns
for col in ['discounted_price', 'actual_price', 'discount_percentage', 'rating', 'rating_count']:
    df[col] = (df[col].astype(str)
                         .str.replace('₹','', regex=True)
                         .str.replace(',','', regex=True)
                         .str.replace('%','', regex=True)
                         .str.strip())
    df[col] = pd.to_numeric(df[col], errors='coerce')

#Create new features
df['price_diff'] = df['actual_price'] - df['discounted_price']
df['discount_ratio'] = df['price_diff'] / df['actual_price']

#Correlation analysis
corr = df[['actual_price','discounted_price','discount_percentage','rating','rating_count','price_diff','discount_ratio']].corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap (Price, Discount, Rating)")
plt.show()

#Distribution of discounts
plt.figure(figsize=(8,5))
sns.histplot(df['discount_percentage'], bins=20, kde=True, color="teal")
plt.title("Distribution of Discount %")
plt.xlabel("Discount Percentage")
plt.ylabel("Count")
plt.show()

# ---- Pivot: Category vs Average Discount ----
pivot = pd.pivot_table(df, index='category', values='discount_percentage', aggfunc='mean')
print(pivot.head())

plt.figure(figsize=(10,5))
pivot.sort_values('discount_percentage', ascending=False).head(10).plot(kind='bar', legend=False, color="purple")
plt.title("Top Categories by Average Discount %")
plt.ylabel("Average Discount %")
plt.show()




