from Agent import Agent
import sys
import pandas as pd
fba_agent = Agent(name='FBA Agent')
df_path = sys.argv[2]
stock_data = pd.read_csv(df_path)
print("The exchange opens.")
log_file = fba_agent.trading(stock_data)
log_file.to_csv('log_data.csv')
print("The exchange closes.")