from portfolio import Portfolio

portfolio = Portfolio()
portfolio.load_portfolio()
links = portfolio.query_links("Python")
print(links)
