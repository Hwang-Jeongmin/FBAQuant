import pandas as pd

class Agent:
    def __init__(self, name="FBA_agent", credit=1000, holdings=0):
        self.name = name
        self.credit = credit
        self.holdings = holdings
    def trading(self, stock_data):
        stock_price = round(stock_data['Adj Close'],2).tolist()
        date = stock_data['Date'].tolist()
        print(f"{self.name} entered")
        log_data = []
        for i in range(2, len(stock_price)):
            
            if self.credit >= stock_price[i]:
                
                if stock_price[i] > stock_price[i-1] and stock_price[i-1] > stock_price[i-2]:
                    buy_amount = self.credit // stock_price[i]
                    log = f"{self.name} buys {buy_amount} ${stock_price[i]} TSLA at {date[i]}."
                    log_data.append(log)
                    print(log)
                    self.credit -= buy_amount * stock_price[i]
                    self.holdings += buy_amount
                    
            if self.holdings > 0:
                                    
                if stock_price[i] < stock_price[i-1]:
                    self.credit += self.holdings * stock_price[i]
                    log = f"{self.name} sells {self.holdings} ${stock_price[i]} TSLA at {date[i]}."
                    log_data.append(log)
                    print(log)
                    self.holdings = 0
                    log_file = pd.DataFrame(log_data)
        return log_file