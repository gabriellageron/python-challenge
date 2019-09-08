import os
import csv

total_months = 0
total_revenue = 0
avg_rev_chg = 0
great_rev_inc_date = "Date1"
great_rev_inc_amount = 0
great_rev_dec_date = "Date2"
great_dec_amount = 0
tot_rev_chg = 0


fileList = ["budget_data.csv"]
for file in fileList:
    csvpath = os.path.join('Resources', 'budget_data.csv')
    with open(csvpath, newline='') as csvfile:
        csvfile.readline()
        csvreader = csv.reader(csvfile, delimiter=',')
        total_months = 0
        total_revenue = 0
        prevRevenue = 0
        great_rev_inc_amount = 0
        great_dec_amount = 0
        for row in csvreader:
            total_revenue = total_revenue + int(row[1])
            #find total months
            total_months = total_months +1
            #create greates increase/decrease variables
            revIncrease = int(row[1]) - prevRevenue
            tot_rev_chg = tot_rev_chg + revIncrease
            prevRevenue =  int(row[1])
            if(revIncrease > great_rev_inc_amount):
                great_rev_inc_amount = revIncrease
                great_rev_inc_date = row[0]
            
            if(revIncrease < great_dec_amount):
                great_dec_amount = revIncrease
                great_rev_dec_date = row[0]


    avg_rev_chg = round(tot_rev_chg/total_months,2)

   #create and open output file to write resuts to
    outputpath = os.path.join("Output",file.split(".")[0] + "_Results.txt")

    lines = []
    
    resultsfile = open(outputpath, "w")
    
    #create the output
    lines.append("Financial Analysis")
    lines.append("----------------------------")
    lines.append("Total Months: "+str(total_months))
    lines.append("Total Revenue: $" + str(total_revenue))
    lines.append("Average Revenue Change: $"+str(avg_rev_chg))
    lines.append("Greatest Increase in Revenue: "+great_rev_inc_date + " ($" + str(great_rev_inc_amount) +")")
    lines.append("Greatest Decrease in Revenue: "+great_rev_dec_date + " ($" + str(great_dec_amount) +")")

     ##Write the output to file and console
    for line in lines:
        print(line)
        print(line,file=resultsfile)
        
    #new line
    print()
    
    #close the file
    resultsfile.close()