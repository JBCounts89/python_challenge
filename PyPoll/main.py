import pandas as pd

#Reading in the dataframe
data_df= pd.read_csv("PyPoll/Resources/election_data.csv")

#The total number of votes cast
total_votes= len(data_df)

#A complete list of candidates who received votes
candidates= data_df["Candidate"].unique().tolist()

#The percentage of votes each candidate won
vote_percents= data_df["Candidate"].value_counts(normalize=True) * 100

#The total number of votes each candidate won
candidates_votes= data_df["Candidate"].value_counts()

#The winner of the election based on popular vote
election_winner= candidates_votes.idxmax()

#Conducting the analysis
outcomes= []
outcomes.append("Election Results")
outcomes.append(f"Total Votes: {total_votes}")
for candidate in candidates:
    outcomes.append(f"{candidate}: {vote_percents[candidate]:.3f}% ({candidates_votes[candidate]})")
outcomes.append(f"Winner: {election_winner}")

#Exporting the election results
election_result= "result.txt"
with open(election_result, "w") as file:
    for outcome in outcomes:
        print(outcome)
        file.write(outcome + "\n")
print(f"The results were exported to the file {election_result}")