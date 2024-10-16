import os
import csv

file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

 

total_months = 0
total_net = 0
average_net = []
changes = []
months =[]
previous_net = None 
greatest_increase = ['-inf']
greatest_decrease = ['-inf']
greatest_increase_date = ""
greatest_decrease_date = ""



with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    print(reader)

    reader_header = next(reader)
  

    for Data in reader:
        total_months += 1
        total_net += int(Data[1])
        
        if previous_net is not None:
            change = int(Data[1]) - previous_net
            changes.append(change) 
            months.append(Data[0])

        previous_net = int(Data[1]) 
        
    if changes:
        average_net = sum(changes) / len(changes)

        greatest_increase = max(changes)
        greatest_decrease = min(changes)

        greatest_increase_date = months[changes.index(greatest_increase)]
        greatest_decrease_date = months[changes.index(greatest_decrease)]


output_analysis = f"Financial Analysis \n"
output_analysis += f"------------------------------------\n"
output_analysis += f"Total Months: {total_months} \n"
output_analysis += f"Total Net: ${total_net} \n"
output_analysis += f"Average Net: ${average_net: .2f} \n"
output_analysis += f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
output_analysis += f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"



with open(file_to_output,"w") as txt_file:
    
    
    txt_file.write(output_analysis)

    print("Total Votes written to file successfully")

    
    print(output_analysis)


    
       

  

 

