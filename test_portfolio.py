from portfolio_agent import analyze_portfolio

results = analyze_portfolio()

print("\n=== PROJECT PORTFOLIO ===\n")

for item in results:

    print(f"Project : {item['project']}")
    print(f"Risk Score : {item['score']}")
    print(f"Status : {item['status']}")
    print()