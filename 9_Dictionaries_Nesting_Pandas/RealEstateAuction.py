# PostgreSQL admin pass: q1w2e3r4

# Real Estate Auction

import pyarrow
import pandas as pd

# All necessary variables
name = ""
bid = 0
num_of_bidders = 0
bidders =  []
bidders_for_lot = {}
all_bids = {}
highest_bid = 0
highest_bid_name = ""

# No error conversion to Int
def nect_int(user_input):
    """Converts input to Int with no error for Str"""
    if not user_input.isnumeric():
        return 0
    else:
        return int(user_input)

# Setting up Lots data structure
properties = [
    {
        "property": "Apartment",
        "description": {
            "location": "Palmers Green, London, 413 Green Lanes, 4JD",
            "bedrooms": 2,
            "area": 83,
            "starting_price": 600000
        }
    },
    {
        "property": "Townhouse",
        "description": {
            "location": "Laguna Park, Bang Tao, Thailand",
            "bedrooms": 3,
            "area": 170,
            "starting_price": 250000
        }
    },
    {
        "property": "Villa",
        "description": {
            "location": "Fethiye, Mugla, Turkey",
            "bedrooms": 5,
            "area": 250,
            "starting_price": 500000
        }
    }
]

df_lots = pd.DataFrame(properties)

# Setting up Bids data structure
print("Welcome to Real Estate Auction!")
num_of_bidders = nect_int(input("\nHow many bidders are there? "))

if num_of_bidders == 0:
    exit()

for i in range(num_of_bidders):
    name = input("Enter bidder name: ")
    bidders.append(name)
    bidders_for_lot[name] = 0

for index, row in df_lots.iterrows():
    all_bids[row['property']] = bidders_for_lot

df_bids = pd.DataFrame(all_bids)

# Program starts
for index, row in df_lots.iterrows():
    print("\nProperty Type:", row['property'])
    description = row['description']
    print("Location:", description['location'])
    print("Bedrooms:", description['bedrooms'])
    print("Area:", description['area'], "sq.m.")
    print("Starting Price:", "${:,}".format(description['starting_price']))
    print("-" * 30)

    highest_bid = 0

    for i in range(num_of_bidders):
        bid = nect_int(input(f"{bidders[i]}'s bid: $"))
        df_bids.loc[bidders[i], row['property']] = bid

# Final calculations
max_bids = df_bids.max().apply(lambda x: "${:,}".format(x))
winners_names = df_bids.idxmax()

df_max_bids = pd.DataFrame(max_bids, columns=['Max bid']).T
df_winners_names = pd.DataFrame(winners_names, columns=['Winner']).T

df_result = pd.concat([df_bids, df_max_bids, df_winners_names])

print(f"\nTable of lots, bidders, and winners:\n\n{df_result}")