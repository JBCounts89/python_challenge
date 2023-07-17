import pandas as pd

#Reading in the dataframe
data_df= pd.read_csv("PyBank/Resources/budget_data.csv")

#The total number of months included in the dataset
month_totals= len(data_df)

#The net total amount of "Profit/Losses" over the entire period
net_total_amounts= data_df["Profit/Losses"].sum()

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
delta= data_df["Profit/Losses"].diff()
mean_delta= delta.mean()

#The greatest increase in profits (date and amount) over the entire period
biggest_profit= delta.max()
biggest_profit_date= data_df.loc[delta.idxmax(), "Date"]

#The greatest decrease in profits (date and amount) over the entire period
biggest_profit_drop= delta.min()
biggest_profit_drop_date= data_df.loc[delta.idxmin(), "Date"]

#Conducting the analysis
outcomes= []
outcomes.append("Financial Analysis")
outcomes.append(f"Total Months: {month_totals}")
outcomes.append(f"Total: ${net_total_amounts} ")
outcomes.append(f"Average Change: ${mean_delta:.2f}")
outcomes.append(f"Greatest Increase in Profits: {biggest_profit_date} (${biggest_profit:0f})")
outcomes.append(f"Greatest Decrease in Profits:{biggest_profit_drop_date} (${biggest_profit_drop}) ")

#Exporting the results as a text file
with open("Analysis.txt", "w") as file:
    file.write('\n'.join(outcomes))