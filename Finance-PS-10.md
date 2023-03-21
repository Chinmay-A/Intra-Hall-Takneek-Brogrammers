# Intra-Hall-Takneek-Brogrammers
Submissions for the Intra Hall Takneek PS 10

#Startegy
The idea is based on a 3 day mean reversion pattern.

#Model
I have assumed the Hedge Fund Model wherein a net value of 20M is traded daily. The profits which are in excess of the 20M USD are collected each day.
And on loss making days the portfolio is reinjected such that the net cash traded next day is also 20M USD. The alpha is neutralized over the UNIVERSE.

#Details
An "Alpha" is generated using the close price data available in Yahoo Finance. A 3 day mean reversion strategy is used and is implemented by calculating
the change price in three days and then scaling it (rank) such that the lowest value is assigned 0 and the highest value is assigned 1. Then the mean
over the universe is subtracted to neutralize the alpha.

#

The PnL generated is 401M over a span of 8 years.
The Sharpe Ratio is 1.65

-Chinmay Amrutkar
