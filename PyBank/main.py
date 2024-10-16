import os
import csv

file_to_load = os.path.join("..", "Resources", "budget_data.csv")
file_to_output = os.path.join("..", "analysis", "budget_analysis.txt")

 

total_months = 0
total_net = 0
average_net = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]



with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    print(reader)

    reader_header = next(reader)
  

    for Data in reader:
        total_months += 1
        total_net += int(Data[1])
        
        
    print("Total Months: ", total_months) 
    print("Total Net: ", total_net)
    





    
       

  

 

