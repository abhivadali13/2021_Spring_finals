# project setup

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import combinations, permutations
from collections import Counter
import random
import time
from numpy.random import multinomial


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

    >>> combos, discarded = combinations_creator('w')
    >>> len(combos) == 1001
    True

    >>> combos, discarded = combinations_creator('w')
    >>> len(discarded) == 4
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


def odds_assigner(ping_pong_combinations, discarded_combination, odds_dict):
    """
    This function assigns a certain number of combinations of ping pong balls to each team based on their odds.
    We temporarily remove the unassigned ping pong ball from the list of ping pong ball combinations and
    re-assign it back after. Then, we generate 1000 random numbers from 0 through 1000. Finally, we assign each
    team their odds from this number
    :param ping_pong_combinations: an array containing all the combinations of 14 choose 4 ping pong balls
    :param discarded_combination: the one combination that is not assigned to a team
    :param odds_dict: A dictionary that maps each their to their respective odds
    :return: a resulting dictionary that maps each team to their combinations
    """
    ping_pong_combinations.remove(discarded_combination)
    random_indices = random.sample(range(len(ping_pong_combinations)), 1000)
    random_indices_length = len(random_indices)
    combinations_dictionary = {}
    for i in odds_dict.keys():
        sample = int(odds_dict[i] * random_indices_length)
        draw = random.sample(random_indices, sample)
        for j in draw:
            if draw[0] == j:
                combinations_dictionary[i] = [ping_pong_combinations[j]]
            else:
                combinations_dictionary[i].append(ping_pong_combinations[j])
            random_indices.remove(j)
    ping_pong_combinations.append(discarded_combination)
    return combinations_dictionary


def ball_combination_picker():
    """
    This function simulates the selection of combinations of balls as done in the NBA Draft Lottery.
    First, a list of numbers from 1-15 is created. Then, the balls are mixed for 1/100000 of the time they
    are mixed in the actual NBA Draft Lottery. during this time, the list is shuffled and a random number is
    chosen from the list. This represents the first ball drawn. This process is repeated until 4 balls are drawn.
    :return: a list representing the 4 number combination that was drawn
    """
    ping_pong_balls = list(range(1, 15))
    number_of_balls_picked = 0
    ball_combination = []

    while number_of_balls_picked < 4:
        number_of_balls_picked += 1
        start = time.time()
        time.time()
        elapsed = 0

        if number_of_balls_picked == 1:
            mixing_seconds = 0.0002
        else:
            mixing_seconds = 0.0001

        while elapsed < mixing_seconds:
            random.shuffle(ping_pong_balls)
            elapsed = time.time() - start
            print("Shuffling ping pong balls; ", elapsed, "seconds elapsed...")
            time.sleep(.0001)
        chosen_ball = random.choice(ping_pong_balls)
        print("The chosen ball is: ", chosen_ball)
        ball_combination.append(chosen_ball)
        ping_pong_balls.remove(chosen_ball)

    return ball_combination


def team_selector(four_ball_combination, displaced_combination, teams_combinations):
    """
    Once the combination of balls is drawn, we must check which team has actually been assigned this combination.
    In order to do this, we look at all the permuatations of the ball combination and compare it to the combination
    assigned to each team and the unassigned combination to see which one the combination belongs to.
    :param four_ball_combination: an array representing the four number combination that was chosen
    :param displaced_combination: an array representing the combination that has not been assigned to a team
    :param teams_combinations: a dictionary that maps each team to a set of combinations they've been assigned to
    :return: the team that has been assigned the combination

    >>> team = team_selector([1,2,3,4], [11,12,13,14], {'Houston Rockets': [(1,2,3,4)]})
    >>> team == 'Houston Rockets'
    True

    >>> team = team_selector([1,2,3,4], [11,12,13,14], {'Minnesota Timberwolves': [(1,2,4,3)]})
    >>> team == 'Minnesota Timberwolves'
    True

    >>> team = team_selector([1,2,5,4], [11,12,13,14], {'Minnesota Timberwolves': [(1,2,4,3)]})
    >>> team != 'Minnesota Timberwolves'
    True
    """
    ball_combinations = list(permutations(four_ball_combination, 4))
    unassigned_four_ball_combinations = list(permutations(displaced_combination, 4))
    for i in ball_combinations:
        if i in unassigned_four_ball_combinations:
            return ValueError

        for j in teams_combinations:
            if i in teams_combinations[j]:
                return j


def lottery_results(dictionary_combinations, combination_unassigned, input_user):
    """
    This function calls on the ball_combination_picker() and team_selector() methods to run a full simulation of
    one NBA Draft Lottery. For the regular simulation, based on the first four teams that are assigned picks,
    the simulator goes in order based on a list of the teams in order of odds that are remaining and assigns
    them the picks 5-12. There are modifications for the other simulations involved, such as changing the number
    of teams that are picked using ping pong balls.
    :param dictionary_combinations: dictionary that maps each team to their assigned ball combinations
    :param combination_unassigned: an array representing the unassigned ball combination
    :param input_user: a user inputted string expressing what type of simulation this is
    :return: a dictionary that maps each team to the pick that they've been given in the lottery
    """
    team_aggregate_stats = {}
    team_order = 1
    lottery_order = list(dictionary_combinations.keys())
    pick_limit = 0

    if input_user == 'r' or input_user == 'R' or input_user == 'w' or input_user == 'W':
        pick_limit = 4
        pick_number = 5

    elif input_user == 'a' or input_user == 'A':
        pick_limit = 14

    while team_order <= pick_limit:
        ball_combination = ball_combination_picker()
        team = team_selector(ball_combination, combination_unassigned, dictionary_combinations)
        print()

        if team in lottery_order:
            print("The number #", team_order, " pick in the 2021 NBA Draft goes to: ", team)
            if team not in team_aggregate_stats:
                team_aggregate_stats[team] = [team_order]
            else:
                team_aggregate_stats[team].append(team_order)
            print()
            lottery_order.remove(team)
            team_order += 1

    if input_user != 'a' and input_user != 'A':
        if input_user == 'r' or input_user == 'R':
            total_pick_limit = 14

        elif input_user == 'w' or input_user == 'W':
            total_pick_limit = 15

        print()
        print("Picks 5 -", total_pick_limit, "are in this order: ")
        for j in lottery_order:
            if pick_number != total_pick_limit:
                print(j + ", ")
            else:
                print(j)

            if j not in team_aggregate_stats:
                team_aggregate_stats[j] = [pick_number]
            else:
                team_aggregate_stats[j].append(pick_number)
            pick_number += 1

    print('___________________')
    return team_aggregate_stats


def team_stats_calculator(team_stats):
    """
    This function uses the Counter function to count the number of times each team got each pick all the iterations
    of the simulation are complete.
    :param team_stats: A dictionary that maps each team to every pick that they received during the simulation
    :return: a Counter object that maps each team to the counts of each pick that they received during the simulation

    >>> cleaned_team_stats = team_stats_calculator({'Houston Rockets': [1, 2, 4, 6, 7]})
    >>> cleaned_team_stats
    {'Houston Rockets': Counter({1: 1, 2: 1, 4: 1, 6: 1, 7: 1})}

    >>> cleaned_team_stats = team_stats_calculator({'Houston Rockets': [1, 2, 4, 6, 7], 'Minnesota Timberwolves': [1, 3, 3, 3, 3]})
    >>> len(cleaned_team_stats['Minnesota Timberwolves']) == 2
    True

    >>> cleaned_team_stats = team_stats_calculator({'Houston Rockets': [1, 2, 4, 6, 7], 'Minnesota Timberwolves': [1, 3, 3, 3, 3]})
    >>> len(cleaned_team_stats) == 4
    False
    """
    formatted_team_stats = {}
    for i in team_stats:
        formatted_team_stats[i] = Counter(team_stats[i])
    return formatted_team_stats


def team_data_plotter(team_aggregate_data):
    """
    This function creates two lists, one that contains each team's names, and one that contains their associated
    picks from the simulation...these are used to generate a plot that provides a visual understanding of the
    simulation
    :param team_aggregate_data: a dictionary that maps each team to the counts of the picks they received
                                during the simulation
    """
    new_key = "Kings"
    old_key = "Sacramento Kings"
    if old_key in team_aggregate_data:
        team_aggregate_data[new_key] = team_aggregate_data.pop(old_key)

    new_key = "Pistons"
    old_key = "Detroit Pistons"
    if old_key in team_aggregate_data:
        team_aggregate_data[new_key] = team_aggregate_data.pop(old_key)

    new_key = "Cavs"
    old_key = "Cleveland Cavaliers"
    if old_key in team_aggregate_data:
        team_aggregate_data[new_key] = team_aggregate_data.pop(old_key)

    new_key = "Rockets"
    old_key = "Houston Rockets"
    if old_key in team_aggregate_data:
        team_aggregate_data[new_key] = team_aggregate_data.pop(old_key)

    new_key = "Wolves"
    old_key = "Minnesota Timberwolves"
    if old_key in team_aggregate_data:
        team_aggregate_data[new_key] = team_aggregate_data.pop(old_key)

    new_key = "Magic"
    old_key = "Orlando Magic"
    if old_key in team_aggregate_data:
        team_aggregate_data[new_key] = team_aggregate_data.pop(old_key)

    new_key = "Thunder"
    old_key = "Oklahoma City Thunder"
    if old_key in team_aggregate_data:
        team_aggregate_data[new_key] = team_aggregate_data.pop(old_key)

    new_key = "Raptors"
    old_key = "Toronto Raptors"
    if old_key in team_aggregate_data:
        team_aggregate_data[new_key] = team_aggregate_data.pop(old_key)

    new_key = "Bulls"
    old_key = "Chicago Bulls"
    if old_key in team_aggregate_data:
        team_aggregate_data[new_key] = team_aggregate_data.pop(old_key)

    new_key = "Wizards"
    old_key = "Washington Wizards"
    if old_key in team_aggregate_data:
        team_aggregate_data[new_key] = team_aggregate_data.pop(old_key)

    new_key = "Pelicans"
    old_key = "New Orleans Pelicans"
    if old_key in team_aggregate_data:
        team_aggregate_data[new_key] = team_aggregate_data.pop(old_key)

    new_key = "Pacers"
    old_key = "Indiana Pacers"
    if old_key in team_aggregate_data:
        team_aggregate_data[new_key] = team_aggregate_data.pop(old_key)

    new_key = "Warriors"
    old_key = "Golden State Warriors"
    if old_key in team_aggregate_data:
        team_aggregate_data[new_key] = team_aggregate_data.pop(old_key)

    new_key = "Spurs"
    old_key = "San Antonio Spurs"
    if old_key in team_aggregate_data:
        team_aggregate_data[new_key] = team_aggregate_data.pop(old_key)

    team_list = []
    pick_list = []
    for i in team_aggregate_data:
        for j in team_aggregate_data[i].items():
            k = 0
            while k < int(j[1]):
                team_list.append(i)
                pick_list.append(j[0])
                k += 1

    fig_dims = (20, 10)
    fig, ax = plt.subplots(figsize=fig_dims)
    x = team_list
    y = pick_list
    print('___________________')
    print()
    print("The following plot summarizes our simulations of the NBA Draft Lottery: ")
    print()
    sns.stripplot(x=x, y=y, alpha=0.5, s=10, linewidth=1.0, jitter=True)
    plt.show()


def team_sim_data(team_info, sim_count, input_from_user):
    """
    This function takes our Counter dictionary and uses its values to obtain some summary statistics
    for each team from our simulation. These statistics include: mean pick, standard deviation of pick,
    highest pick and lowest pick. This function also tests our hypotheses laid out in the readme as well.
    :param team_info: a dictionary that maps each team to the counts of the number of times they obtained each pick
    :param sim_count: the number of times the simulation iterated
    :param input_from_user: a user inputted string expressing what type of simulation this is
    """
    print()
    print('The following statistics summarize our simulations of the NBA Draft Lottery: ')
    print()
    hypothesis_1_count = 0
    hypothesis_1_indices = []
    hypothesis_2_count = 0
    hypothesis_2_indices = []
    hypothesis_3_count = 0

    for i in team_info:
        picks = []
        for j in team_info[i].items():
            k = 0
            while k < int(j[1]):
                picks.append(j[0])
                k += 1

        print(i, "simulation statistics: ")
        print()
        print("Average Pick: " + str(np.mean(picks)))
        print("Standard Deviation of Picks: " + str(np.std(picks)))
        print("Lowest Pick: #" + str(np.max(picks)))
        print("Highest Pick: #" + str(np.min(picks)))
        print()

        if input_from_user == 'r':
            if (
                    i == 'Oklahoma City Thunder' or i == 'Cleveland Cavaliers' or i == 'Sacramento Kings' or i == 'Toronto Raptors'):
                for r, k in enumerate(picks):
                    if k <= 4 and r not in hypothesis_1_indices:
                        hypothesis_1_count += 1
                        hypothesis_1_indices.append(i)

        if input_from_user == 'a':
            if i == 'Houston Rockets' or i == 'Minnesota Timberwolves' or i == 'Detroit Pistons':
                for r, k in enumerate(picks):
                    if k >= 7 and r not in hypothesis_2_indices:
                        hypothesis_2_count += 1
                        hypothesis_2_indices.append(i)

        if input_from_user == 'o':
            if i == 'New York Knicks':
                for r in picks:
                    if r == 1:
                        hypothesis_3_count += 1

    if input_from_user == 'r' or input_from_user == 'a' or input_from_user == 'o':
        print('___________________')
        print()
        if input_from_user == 'r':
            if hypothesis_1_count / (sim_count - 1) >= 0.25:
                print("Hypothesis 1 is: True")
            else:
                print("Hypothesis 1 is: False")

        elif input_from_user == 'a':
            if hypothesis_2_count / (sim_count - 1) >= 0.40:
                print("Hypothesis 2 is: True")
            else:
                print("Hypothesis 2 is: False")

        elif input_from_user == 'o':
            if hypothesis_3_count / (sim_count - 1) >= 0.40:
                print("Hypothesis 3 is: True")
            else:
                print("Hypothesis 3 is: False")


def multinomial_simulator(odds, counter):
    """
    This function iterates through the odds list for each team in the lottery. It then creates a multinomial
    distribution and simulates the number of times each pick is awarded to each team out of a given number
    of simulations.
    :param odds: A list representing a team's chances of obtaining picks 1-14
    :param counter: An integer representing how many times the simulation should iterate
    """
    print()
    for i in odds:
        simulations = multinomial(counter, odds[i])
        for j in range(len(simulations)):
            print(i + ' Pick %d: %d ' % (j + 1, simulations[j]))
        print()


def bernoulli_random_trial():
    """
    This function simply uses the numpy package for a random bernoulli trial with 0.7 success rate and
    runs this one time. Then, it returns the results: either a 1 for success or a 0 for failure. This is used to determine
    whether or not the NBA's attempt to rig the 1985 Lottery in favor of the Knicks is successful or not.
    :return: a variable that represents a 0 for a failed attempt or a 1 for a successful attempt

    >>> result = bernoulli_random_trial()
    >>> result == 0 or result == 1
    array([ True])
    """
    x = 1
    success_rate = 0.7
    Y = np.random.binomial(1, success_rate, x)
    return Y


def nba_rigging_odds(bernoulli_result):
    """
    This function determines the odds of each team winning the lottery. If the bernoulli trial was a success, a
    normal random variable that results in odds that are larger than the original odds for the Knicks is used to
    replace their original odds, then a randomly selected team loses the difference between these odds,
    illustrating that the lottery was rigged. If the bernoulli trial was a failure, the Knicks' odds are brought
    down to 0.001 and a randomly selected team gets the rest of their odds added.
    :param bernoulli_result: a variable that represents a 0 for a failed attempt or a 1 for a successful attempt
    :return: a list of the odds for each team to win the lottery
    """
    pacers_odds = 0.1429
    clippers_odds = 0.1429
    supersonics_odds = 0.1429
    hawks_odds = 0.1429
    kings_odds = 0.1429
    warriors_odds = 0.1429

    if bernoulli_result == 1:
        print('The NBA was not caught attempting to rig the 1985 NBA Draft Lottery')
        mu, sigma = 0.25, 0.1
        knicks_odds = np.round(np.random.normal(mu, sigma, 1),
                               3)  # using a normal dist. to determine odds of rigged knicks pick
        while knicks_odds <= 0 or knicks_odds >= 0.2858 or knicks_odds <= 0.1429:  # knicks should not have non-positive odds or odds that will reduce other teams' odds to negative values
            knicks_odds = np.round(np.random.normal(mu, sigma, 1), 3)
        randomizer = random.randint(1, 6)
        if randomizer == 1:
            pacers_odds -= (knicks_odds - 0.1429)
        elif randomizer == 2:
            clippers_odds -= (knicks_odds - 0.1429)
        elif randomizer == 3:
            supersonics_odds -= (knicks_odds - 0.1429)
        elif randomizer == 4:
            hawks_odds -= (knicks_odds - 0.1429)
        elif randomizer == 5:
            kings_odds -= (knicks_odds - 0.1429)
        else:
            warriors_odds -= (knicks_odds - 0.1429)
        print('The New York Knicks rigged odds are now:', knicks_odds)
        print()

    else:
        print('The NBA was caught attempting to rig the 1985 NBA Draft Lottery')
        knicks_odds = 0.01
        randomizer = random.randint(1, 6)
        if randomizer == 1:
            pacers_odds += (0.1429 - knicks_odds)
        elif randomizer == 2:
            clippers_odds += (0.1429 - knicks_odds)
        elif randomizer == 3:
            supersonics_odds += (0.1429 - knicks_odds)
        elif randomizer == 4:
            hawks_odds += (0.1429 - knicks_odds)
        elif randomizer == 5:
            kings_odds += (0.1429 - knicks_odds)
        else:
            warriors_odds += (0.1429 - knicks_odds)
        print('The New York Knicks odds after punishment are now:', knicks_odds)
        print()

    return [knicks_odds, pacers_odds, clippers_odds, supersonics_odds, hawks_odds, kings_odds, warriors_odds]


def nba_1985_draft_lottery_simulator(team_odds):
    """
    Given the odds for each team, a multinomial distribution is used to determine the 1st pick, then the 2nd pick,
    and so on, all the way to the fifth pick. Then, the final two picks in the lottery are filled in manually.
    The resulting pick for each team is then added to a dictionary, in which the key is the team name and the value
    is the pick, and this dictionary is returned.
    :param team_odds: a list representing the odds for all the teams in the lottery of getting the number #1 pick
    :return: a dictionary that maps each team to their pick
    """
    team_list = ['New York Knicks', 'Indiana Pacers', 'Los Angeles Clippers', 'Seattle SuperSonics', 'Atlanta Hawks',
                 'Sacramento Kings', 'Golden State Warriors']
    pick_list = []
    pick_number = 1
    while pick_number <= 5:
        simulations = multinomial(1, team_odds)
        pick_list.append(team_list[np.argmax(simulations)])
        team_odds.pop(np.argmax(simulations))
        team_list.pop(np.argmax(simulations))
        pick_number += 1

    for i in team_list:
        if i not in pick_list:
            pick_list.append(i)

    pick_dictionary = {}
    for i, value in enumerate(pick_list):
        pick_dictionary[value] = [i + 1]
        print("The number #", i + 1, "pick in the 1985 NBA Draft goes to:", value)

    print()
    return pick_dictionary
