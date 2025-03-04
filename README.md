# Python-Challenge: PyBank & PyPoll

This project contains two Python scripts: **PyBank** for financial analysis and **PyPoll** for election results analysis. Both scripts process CSV data to calculate key metrics and output results to the terminal and a text file.

---

## PyBank: Financial Analysis

**Goal**: Analyze financial data (`budget_data.csv`) to compute:
- Total Months
- Total Profit/Loss
- Average Monthly Change
- Greatest Increase and Decrease in Profits

**How it works**:
- Reads the CSV file and extracts the financial data.
- Calculates total profit/loss, the greatest increase and decrease, and average monthly changes.
- Results are printed to the terminal and saved in `Analysis/Analysis.txt`.

---

## PyPoll: Election Results

**Goal**: Analyze election data (`election_data.csv`) to compute:
- Total Votes
- Vote Percentage per Candidate
- Election Winner

**How it works**:
- Reads the election data CSV and counts votes per candidate.
- Displays the total number of votes and the percentage of votes each candidate received.
- Outputs the winner of the election.
- Results are printed to the terminal and saved in `Analysis/Pypoll_analysis.txt`.

---

## How to Run

1. Place the CSV files (`budget_data.csv` and `election_data.csv`) inside the `Resources/` folder.
2. Run the script with:  
   `python main.py`
3. Results will be printed to the terminal and saved in the `Analysis/` folder.

---

## File Structure
- **`main.py`**: Main script for both








