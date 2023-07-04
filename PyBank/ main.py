#start process of reading csv file
import os
import csv



pybank_csv = os.path.join('Resources', 'budget_data.csv')
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)


    #create variables to store data values
    months_total = 0
    profit_loss_total = 0
    profit_loss_sum = 0
    greatest_profit_increase = 0
    greatest_profit_decrease = 999999999999999999999


    #loop through rows in csv file
    for row in csvreader:
        #calculate total number of months included in dataset
        months_total = months_total + 1


        #create variable for total profit loss and calculate total profit loss
        profit_loss = row[1]
        profit_loss_total = profit_loss_total + int(profit_loss)

        #calculate The changes in "Profit/Losses" over the entire period, and (then the average of those changes)
        if months_total > 1:
            change = int(profit_loss) - final_profit_loss

            profit_loss_sum = profit_loss_total + change
            profit_loss_average = profit_loss_total / (months_total - 1)

        #calculate greatest increase in profits (date and amount) over the entire period
        if change > greatest_profit_increase:
            greatest_profit_increase = change
            greatest_profit_increase_date = row[0]

         #calculate greatest decrease in losses (date and amount) over the entire period
        if change < greatest_profit_decrease:
            greatest_profit_decrease = change
            greatest_profit_decrease_date = row[0]

        #create financial analysis and print total months, total profit loss, average change, greatest increase in profits, greatest decrease in profits
            final_profit_loss = (row[1])
        months = (f"Total Months: {months_total}")
        total = (f"Total: ${profit_loss_total}")
        average = (f"Average Change: ${profit_loss_average}")
        increase = (f"Greatest Increase in Profits: {greatest_profit_increase_date} (${greatest_profit_increase})")
        decrease = (f"Greatest Decrease in Profits: {greatest_profit_decrease_date} (${greatest_profit_decrease})")

    print("Financial Analysis")
    print("------------------")
    print(months)
    print(total)
    print(average)
    print(increase)
    print(decrease)

        #export a text file with the results
    output_path = os.path.join("Analysis", "analysis.txt")

    with open(output_path, 'w') as txtfile:

        analysis.write("Financial Analysis")
        analysis.write("/n")
        analysis.write("------------------")
        analysis.write("/n")
        lines = [months, total, average_change, increase, decrease]

        for line in lines:
            analysis.write(line)
            analysis.write("/n")

         