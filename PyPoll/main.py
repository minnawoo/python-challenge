import unicodecsv
from operator import itemgetter

# Open csv file and read data into a list of dictionaries
with open('election_data.csv', 'rb') as f:
     reader = unicodecsv.DictReader(f)
     election_data = list(reader)

# Print header
print("Election Results")
print("-------------------------")

# Print the total number of votes cast
num_votes = len(election_data)
print(f"Total Votes: {num_votes}")
print("-------------------------")

# Sort the table by candidate
sorted_election_data = sorted(election_data, key=itemgetter('Candidate'))

######################################################################################
# Count number of votes, calculate percentage of election won, and add to message list
######################################################################################  

# Prepare variables for for-loop through all votes
name = sorted_election_data[0]['Candidate']
num_candidates = 0
vote_count = 0
winner_name = ""
winner_percentage = 0
message = []

# Enter for-loop (knowing that we've sorted the list of votes by candidate)
for i in range(0, num_votes):
    row = sorted_election_data[i]
    if row['Candidate'] == name:
        vote_count += 1
    else:
        # Calculate percentage of votes out of total (before updating variables)
        percentage = round(vote_count/num_votes*100, 3)
        
        # Check if it beats the largest percentage we have in store
        if percentage > winner_percentage:
            winner_name = name
            winner_percentage = percentage
        
        # Add our previous candidate's name, votes, and percentage to the message list
        print(f"{name}: {percentage}% ({vote_count})")
        message.append(name + ": " + str(percentage) + "% " + "(" + str(vote_count) + ")")
        
        # Update variables for our current candidate
        num_candidates += 1
        name = row['Candidate']
        vote_count = 1 # since we did not add a vote to the count yet

##########################################################################       
# Add our last candidate's name, votes, and percentage to the message list
#  (Since we've exited the for-loop before doing that)
##########################################################################

# Calculate percentage of votes out of total
percentage = round(vote_count/num_votes*100, 3)

# Check if it's the winner
if percentage > winner_percentage:
    winner_name = name
    winner_percentage = percentage

# Add our last candidate's name, votes, and percentage to the message list
message.append(name + ": " + str(percentage) + "% " + "(" + str(vote_count) + ")")

# Print out the winner name, percentage won by, and total votes received
print(f"{name}: {percentage:.3f}% ({vote_count})")
print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")

# Print message list to Output.txt
with open("Output.txt", "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {num_votes}\n")
    text_file.write("-------------------------\n")
    for line in message:
        text_file.write(f"{line}\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winner_name}\n")
    text_file.write("-------------------------\n")