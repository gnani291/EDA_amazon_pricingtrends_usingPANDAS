Title:
Exploratory Data Analysis of Amazon Product Pricing, Discounts, and Ratings

Description:
This code performs an end-to-end exploratory data analysis (EDA) on an Amazon product dataset using Pandas, Matplotlib, and Seaborn. It begins by loading the dataset from a CSV file and focuses on cleaning important numeric columns such as prices, discount percentages, ratings, and rating counts. Since these values often contain symbols like ₹, commas, and percentage signs, the code removes these characters and safely converts the data into numeric format, handling invalid entries gracefully.

Next, the code engineers new features to gain deeper insights. It calculates the price difference between actual and discounted prices and derives a discount ratio, which shows the relative discount compared to the original price. These features help in understanding how aggressive the discounts are across products.

The analysis then moves to understanding relationships between variables using a correlation matrix, visualized through a heatmap. This highlights how prices, discounts, and customer ratings are related to each other. To further explore discount behavior, the code plots a histogram of discount percentages, showing how discounts are distributed across products.

Finally, the code uses a pivot table to compute the average discount percentage for each product category. A bar chart visualizes the top categories offering the highest average discounts, making it easy to compare categories.

Overall, this script helps uncover pricing patterns, discount trends, and their relationship with ratings in an Amazon product dataset.
