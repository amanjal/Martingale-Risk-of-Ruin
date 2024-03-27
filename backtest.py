import random
import sys

def martingale(startAmount, startingBet, multiplier, bet_multiplier, max_profit=0):
    """
    Simulates the Martingale betting strategy.
    
    Args:
        startAmount (float): The initial amount of money.
        startingBet (float): The initial bet amount.
        multiplier (float): The multiplier for winning bets.
        bet_multiplier (float): The multiplier for increasing bets after losing.
        max_profit (float, optional): The maximum allowable profit. Defaults to 0.

    Returns:
        int: The number of games played until the specified conditions are met.
    """
    currAmount = startAmount
    bet = startingBet
    winningChance = ((100/multiplier) * 0.99)/100
    currAmount -= bet
    gamesPlayed = 0
    while currAmount >= 0 and bet*multiplier <= max_profit:
        gamesPlayed += 1
        if random.random() < winningChance:
            currAmount += bet * multiplier
            bet = startingBet
        else:
            bet *= bet_multiplier
            currAmount -= bet
    return gamesPlayed


def main(args):
    seeds = 10_000
    games = []
    starting_amount = float(args[1])
    starting_bet=float(args[2])
    multiplier=float(args[3])
    bet_multiplier=float(args[4])
    max_profit = float(args[5])
    for s in range(seeds):
        random.seed = s
        games.append(martingale(starting_amount, starting_bet, multiplier, bet_multiplier, max_profit))

    # Calculate and print the average number of games played across all simulations
    print(sum(games)/len(games))
    

if __name__ == "__main__":
    main(sys.argv)


            

