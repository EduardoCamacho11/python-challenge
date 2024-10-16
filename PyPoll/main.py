import csv
import os

file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "elections_analysis.txt")

total_votes= 0 
candidate_votes = {}
candidate_list = []


with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:
        total_votes += 1
        candidate = row[2]

        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_votes[candidate] = 0 

        candidate_votes[candidate]+= 1

    
    
output_analysis = "Election Results \n"
output_analysis += "--------------------------\n"
output_analysis += f"Total Votes: {total_votes}\n"
output_analysis += "--------------------------\n"
for candidate, votes in candidate_votes.items():    
    percentage = (votes / total_votes)* 100
    output_analysis += f"{candidate}: {percentage: .3f}% ({votes})\n" 
output_analysis += "--------------------------\n"
winner = max(candidate_votes, key=candidate_votes.get)
output_analysis += f"Winner: {winner}"



with open(file_to_output,"w") as txt_file:
    
    
    txt_file.write(output_analysis)

    print("Total Votes written to file successfully")

    
    print(output_analysis)

    
    
   



