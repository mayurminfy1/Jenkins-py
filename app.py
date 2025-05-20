# app.py
import requests
import numpy as np
import pandas as pd

def main():
    print("Hello from Jenkins + Docker + Python!")
    response = requests.get("https://api.github.com")
    print("GitHub API Status Code:", response.status_code)

    # Pandas + NumPy demo
    data = {"Name": ["Mayur", "Pal"], "Score": [90, 95]}
    df = pd.DataFrame(data)
    print("\nSample DataFrame:")
    print(df)

if __name__ == "__main__":
    main()
