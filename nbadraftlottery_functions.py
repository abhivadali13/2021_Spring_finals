# project setup

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import combinations, permutations
from collections import Counter
import random
import warnings
import time

import scipy.stats as ss
from numpy.random import multinomial
from decimal import *


def combinations_creator(simulation_type):
    """
    We generate a list of combinations of 14 choose 4. Each item in this list represents a possible combination
    that can be drawn on lottery night. one combination is left unassigned to a team, this combination is
    11-12-13-14.
    :param simulation_type: a user inputted string expressing what type of simulation this is
    :return: a list of ball combinations and one tuple that is the excluded combination

    >>> combos, discarded = combinations_creator('r')
    >>> len(discarded) == 4
    True

    >>> combos, discarded = combinations_creator('r')
    >>> len(combos) == 1001
    True
    """
    if simulation_type == 'r' or simulation_type == 'w' or simulation_type == 'a':
        ball_combinations = combinations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 4)
        ball_combinations = list(ball_combinations)
        excluded_combination = (11, 12, 13, 14)
        return ball_combinations, excluded_combination


def odds_creator(simulation_type, iteration_counter, playoff_team, wild_card_odds):
    """
    Each team is given their respective odds of obtaining the #1 pick
    based on their position in standings/type of simulation. If it is a regular simulation, the
    regular odds are given, if it is a wild-card simulation, there is
    another team added with a random normal variable that determines their odds, and for a multinomial simulation,
    the odds are represented as an array for each pick for each team.
    :param simulation_type: a user inputted string expressing what type of simulation this is
    :param iteration_counter: represents which iteration of the simulation the program is on
    :param playoff_team: represents the wild-card playoff team
    :param wild_card_odds: represents the odds of the wild-card playoff team
    :return: a dictionary with key/value pairs being each team and their odds, and a playoff team and their odds

    >>> odds, playoff_selected_team, playoff_odds = odds_creator('r', 1, None, None)
    >>> len(odds) == 14
    True

    >>> odds, playoff_selected_team, playoff_odds = odds_creator('m', 1, None, None)
    >>> len(odds['Houston Rockets']) == 14
    True

    >>> odds, playoff_selected_team, playoff_odds = odds_creator('a', 100, None, None)
    >>> len(odds) == 14
    True
    """
    if simulation_type == 'r' or simulation_type == 'w' or simulation_type == 'a':
        rockets_odds = 0.14
        timberwolves_odds = 0.14
        pistons_odds = 0.14
        magic_odds = 0.125
        thunder_odds = 0.105
        cavaliers_odds = 0.09
        kings_odds = 0.075
        raptors_odds = 0.06
        bulls_odds = 0.045
        wizards_odds = 0.03
        pelicans_odds = 0.02
        pacers_odds = 0.015
        warriors_odds = 0.01
        spurs_odds = 0.005

        if simulation_type == 'w':
            if iteration_counter == 1:
                mu, sigma = 0.07, 0.035
                wild_card_odds = np.round(np.random.normal(mu, sigma, 1),
                                          3)  # using a normal dist. to determine odds of wild card team
                while wild_card_odds <= 0 or wild_card_odds >= 0.14:  # we should not have a wild card team with non-positive odds or odds greater than the top possible odds
                    wild_card_odds = np.round(np.random.normal(mu, sigma, 1), 3)
            randomizer = random.randint(1, 5)
            if randomizer == 1:
                rockets_odds -= wild_card_odds
            elif randomizer == 2:
                timberwolves_odds -= wild_card_odds
            elif randomizer == 3:
                pistons_odds -= wild_card_odds
            elif randomizer == 4:
                magic_odds -= wild_card_odds
            else:
                thunder_odds -= wild_card_odds

    elif simulation_type == 'm':
        rockets_odds = [0.14, 0.134, 0.127, 0.12, 0.479, 0, 0, 0, 0, 0, 0, 0, 0,
                        0]  # from left to right, these odds represent each team's chances of obtaining picks 1-14
        timberwolves_odds = [0.14, 0.134, 0.127, 0.120, 0.278, 0.20, 0, 0, 0, 0, 0, 0, 0, 0]
        pistons_odds = [0.14, 0.134, 0.127, 0.120, 0.148, 0.260, 0.07, 0, 0, 0, 0, 0, 0, 0]
        magic_odds = [0.125, 0.122, 0.119, 0.115, 0.072, 0.257, 0.167, 0.022, 0, 0, 0, 0, 0, 0]
        thunder_odds = [0.105, 0.105, 0.106, 0.105, 0.022, 0.196, 0.267, 0.087, 0.006, 0, 0, 0, 0, 0]
        cavaliers_odds = [0.09, 0.092, 0.094, 0.096, 0, 0.086, 0.297, 0.206, 0.037, 0.002, 0, 0, 0, 0]
        kings_odds = [0.075, 0.078, 0.081, 0.085, 0, 0, 0.197, 0.341, 0.129, 0.013, 0, 0, 0, 0]
        raptors_odds = [0.06, 0.063, 0.067, 0.072, 0, 0, 0, 0.345, 0.321, 0.067, 0.004, 0, 0, 0]
        bulls_odds = [0.045, 0.048, 0.052, 0.057, 0, 0, 0, 0, 0.507, 0.259, 0.03, 0.001, 0, 0]
        wizards_odds = [0.03, 0.033, 0.036, 0.04, 0, 0, 0, 0, 0, 0.659, 0.190, 0.012, 0, 0]
        pelicans_odds = [0.02, 0.022, 0.024, 0.028, 0, 0, 0, 0, 0, 0, 0.776, 0.126, 0.004, 0]
        pacers_odds = [0.015, 0.017, 0.019, 0.021, 0, 0, 0, 0, 0, 0, 0, 0.861, 0.067, 0.001]
        warriors_odds = [0.01, 0.011, 0.012, 0.014, 0, 0, 0, 0, 0, 0, 0, 0, 0.929, 0.023]
        spurs_odds = [0.005, 0.006, 0.006, 0.007, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.976]

    odds_dictionary = {'Houston Rockets': rockets_odds, 'Minnesota Timberwolves': timberwolves_odds,
                       'Detroit Pistons': pistons_odds,
                       'Orlando Magic': magic_odds, 'Oklahoma City Thunder': thunder_odds,
                       'Cleveland Cavaliers': cavaliers_odds,
                       'Sacramento Kings': kings_odds, 'Toronto Raptors': raptors_odds, 'Chicago Bulls': bulls_odds,
                       'Washington Wizards': wizards_odds,
                       'New Orleans Pelicans': pelicans_odds, 'Indiana Pacers': pacers_odds,
                       'Golden State Warriors': warriors_odds, 'San Antonio Spurs': spurs_odds}

    if simulation_type == 'w':
        if iteration_counter == 1:
            playoff_teams = ['Charlotte Hornets', 'Boston Celtics', 'Miami Heat', 'Atlanta Hawks', 'New York Knicks',
                             'Milwaukee Bucks', 'Brooklyn Nets', 'Philadelphia 76ers',
                             'Utah Jazz', 'Pheonix Suns', 'Los Angeles Clippers', 'Denver Nuggets', 'Dallas Mavericks',
                             'Portland Trail Blazers', 'Los Angeles Lakers',
                             'Memphis Grizzlies']
            playoff_team_selector = random.randint(0, len(playoff_teams) - 1)
            playoff_team = playoff_teams[playoff_team_selector]
            print('The Wild Card Playoff Team selected to participate in the NBA Draft Lottery is the:', playoff_team)
            print('The', playoff_team, 'will enter the NBA Draft Lottery with:', str(wild_card_odds),
                  'odds of obtaining the #1 pick')

        odds_dictionary[playoff_team] = wild_card_odds

    return odds_dictionary, playoff_team, wild_card_odds
