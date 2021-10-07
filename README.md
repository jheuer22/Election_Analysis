# Election Analysis

## Challenge Project Overview 
A Colorado Board of Elections asked for the following tasks to be completed during an election audit of a recent local congressional election: 

1. Calculate the total number of votes cast.
2. Get the complete list of the candidates who received votes.
3. Calculate the total number of votes cast for each county. 
4. Calculate the percentage of votes each county cast. 
5. Determine which county cast the most votes. 
6. Calculate the total number of votes each candidate received.
7. Calculate the percentage of votes each candidate won.
8. Determine the winner of the election based on popular vote. 

## Resources 
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Challenge Summary 
The analysis of the elections show that: 
 - There were 369,711 votes case in the election 
 - The candidates were: 
      - Charles Casper Stockham
      - Diana DeGette
      - Raymon Anthony Doane
  - County Vote totals: 
      -  Jefferson: 10.5% of overall votes with 38,855 votes
      -  Denver: 82.8% of overall votes with 306,055 votes
      -  Arapahoe: 6.7% of overall votes with 24,801 votes.
  - Largest County Turnout:
      -  Denver with 306,055 total votes
  - The candidate results were: 
      - Charles Casper Stockham received  23.0 % of the votes and 85,213 votes 
      - Diana DeGette received 73.8 % of the vote and 272,892 votes 
      - Raymon Anthony Doane received 3.1 %  of the vote and 11,606 votes
  - The winner of the election was: 
      - Diana DeGette, who received 73.8% of the vote with 272,892 votes. 
     

 ## Election Audit Summary  

The results of the election for the congressional district have been summarized above. The Colorado Board of Elections can modify this script for any future audits of elections by changing a few key portions of the scripts to reflect the needs of the new election. First, the csv file that is being imported for the analysis would need to be located in the "Resources" file and the name would need to be specified under the portion of the script titled "# Add a variable to load a file from a path." From that location, the csv file would be imported, and the same analysis of county totals and candidate totals would be run for the specific counties and candidates in the specified race.

If any additional information was requested outside of county totals and candidate totals, there would need to be an additional block of script added to write the new values of the variable into a list and a dictionary so that the items could be categorized. There would be script to iterate through the file and tally the votes by the variable, and the totals of the items could be stored. Another section of script would need to be added to print the totals into the txt file with outcomes of the script. I would suggest hiring another analyst in the case that any additional analytic information beyond county and candidate totals are needed as the script changes would be significant.  

 
