import pandas as pd
import numpy as np

def main():
    game_sales = pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")

    # Which genre has the best video game sales records?
    genre = game_sales.groupby(["Genre"]).agg("sum")
    print("Global sales in millions by genre:")
    print(genre["Global_Sales"])

    # Which regional market buys the most video games?
    market = game_sales.agg("sum")
    print ("Regional Sales in millions (rounded down):")
    print ("NA Sales: ", int(market["NA_Sales"]), "\nEU Sales: ", int(market["EU_Sales"]))
    print ("JP Sales: ", int(market["JP_Sales"]), "\nOther Sales: ", int(market["Other_Sales"]))

    # Which platform has the best sales record?
    platform = game_sales.groupby(["Platform"]).agg("sum")
    print ("Global sales in millions by platform:")
    print (platform["Global_Sales"])

if __name__ == "__main__":
    main()