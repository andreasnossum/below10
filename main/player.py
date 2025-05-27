# Class that initialize a player with a given strategy

# Strategies:
# - "safe": plays only the highest card on hand, draws from deck if face-up >7 and > card on hand, else draw frmo face-up pile
# - "optimize": simpe/safe player, but always want to reduce number of card on hand if possible (two of a kind + ladder)
# - "riskX": safe/optimized player, but takes risks X% of times if no good options available
# - "balanced": ... signal hypothesis...
