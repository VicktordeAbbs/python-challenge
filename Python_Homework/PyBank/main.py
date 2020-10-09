import os
import csv

#file path
py_bank = os.path.join ("..","Resources", "budget_data.csv")
 

#open and read file
with open (py_bank) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    #read the header row
    csv_header = next(csv_reader) #Once this line comes in the header line is no longer seen as part of the data

    # Initializiing variables and containers
    total_profit_loss = 0
    num_of_rows  = 0
    profit_loss__ = []
    dates = []
    p_l_changes = []


    for row in csv_reader:
        total_profit_loss += float(row[1])
        num_of_rows +=1
        
        date = row [0]
        profit_loss = row [1]

        dates.append(date)
        profit_loss__.append(profit_loss)
         
        
    #print(dates)
    
    
    aa_list = profit_loss__
    #print(f'AA_LIST:{aa_list}')
    
    _index = (len(dates))
    #print(f'INDEX=:{_index}')
    gain_loss = "${:,.2f}".format(total_profit_loss)
    print(f'Total Month :{_index}')
    print(f'Total :{gain_loss}')

    
    p_l_change = 0
    for i in range(_index +1):
        monthly_p_l = aa_list [i+1]
        previous_monthly_p_l = aa_list [i]
        i += 1
        p_l_change = float(monthly_p_l) - float(previous_monthly_p_l)
        p_l_changes.append(p_l_change)
        
        #print(int(p_l_change))
        #total = sum(p_l_change)
        #print(total)
        if i == int(_index-1):
            break
        
    #print(p_l_changes)
    #print(int(len(p_l_changes)))
    total_p_l_changes = sum(p_l_changes)
    #print(total_p_l_changes)
    #average_p_l_changes = round(total_p_l_changes/(len(p_l_changes)), 2)
    average_p_l_changes = "$ {:,.2f}".format(total_p_l_changes/(len(p_l_changes)))

    print(f'Average change :{average_p_l_changes}')
    Max = "$ {:,.2f}".format(max(p_l_changes))

    Min = "$ {:,.2f}".format(min(p_l_changes))
    max_index = p_l_changes.index(max(p_l_changes))
    min_index = p_l_changes.index(min(p_l_changes))
    
    max_date = (dates[max_index + 1])
    min_date = (dates[min_index + 1])

    print(f"The greatest increase in profit: { max_date} ({Max})")
    print(f"The greatest decrease in profit: {min_date} ({Min})")
    
