# NBA Draft Lottery: A Monte Carlo Simulation

## Project Video Presentation:

https://mediaspace.illinois.edu/media/t/1_xrx7fo7d

## Project Background:

The NBA Draft Lottery determines the order that the 14 worst teams will select upcoming talent in the NBA Draft. 

- Every team is assigned a certain set of odds to pick #1 overall in the draft, with worse-performing teams having the higher chances. 
- The worst three teams will have equal odds at selecting #1.

A typical lottery ball machine is used to carry out the NBA Draft Lottery. 

![image](https://user-images.githubusercontent.com/46533891/116900598-87018a00-abfe-11eb-9491-bbfd60310a51.png)

- Fourteen Ping Pong Balls (Numbered 1 to 14) are placed in a lottery machine.
- Each 4 digit combination of the 14 balls is assigned to a certain team. There are a total of 1,001 possible combinations, of which 1 is discarded. 
  - The teams with the lowest records are assigned the most number of combinations based on their odds. 
- Drawings are conducted to select the first four picks. The remaining picks are determined in inverse order of the teams’ records. 

In the Drawing Process, for each combination drawn, the lottery machine is mixed for 20 seconds before drawing the first ball and 10 seconds before every subsequent ball. 

- The team that has been assigned the combination that is drawn will receive the pick (1-4) in question.
- If the same team was drawn twice, the result is discarded. If the unassigned sequence is drawn, the result is also discarded.

![Screen Shot 2021-05-03 at 11 00 42 AM](https://user-images.githubusercontent.com/46533891/116900841-d47df700-abfe-11eb-8d4e-8b8e6a98cb38.png)

For more information on this process, feel free to visit: https://www.nba.com/nba-draft-lottery-explainer.

## Project Purpose:

In this project, I carry out the following steps:

- Replicate, and perform a Monte Carlo simulation of, the NBA Draft Lottery and calculate aggregate statistics of which teams are given which picks
  - Do this using the ping-pong ball method outlined above and using a multinomial distribution.

- Apply my own modifications to the NBA Draft Lottery.
  - Run a simulation of the NBA Draft Lottery where balls are drawn for all the picks, rather than just the top 4.
  - Include a randomly selected wild-card playoff team and invite them to participate in the lottery.

- Simulate the 1985 “frozen envelope” NBA Draft Lottery, and explore the popular conspiracy among the NBA media and NBA fans that this event was rigged by the NBA.
  - Some background on this event: https://www.si.com/longform/2015/1985/ewing/index.html

![image](https://user-images.githubusercontent.com/46533891/116901056-13ac4800-abff-11eb-9f8d-d5d9f4818d16.png)

## Some Hypotheses:

- In a simulation of the NBA Draft Lottery 1000 times, the teams that are 5th-8th in the lottery will obtain a top-4 pick at least 25% of the time.
- In a simulation of the modified NBA Draft Lottery 1000 times where ping pong balls are drawn for all the picks, at least 40% of the time, one of the three teams with the highest odds of getting the number #1 pick will drop down below pick #7. 
- In a simulation of the 1985 NBA Draft Lottery 1000 times (accounting for the “frozen envelope”), the New York Knicks obtain the first-pick in the draft over 40% of the time.

## Random Variables:

- The original NBA draft lottery can be translated to a Multinomial Distribution where every team is assigned a set of probabilities to land each of the 14 picks. 
  - N successive independent trials are performed for each team to see which of the outcomes is the most likely.
  - Based on this information, we can formulate the lottery order by observing which teams get which picks the most.

- The modified NBA draft lottery with the wild-card team can be modeled using a Beta Distribution.
  - Determine the odds with a prior that is set to the current median chance of getting the #1 pick (7% odds).
  - This distribution will be fine-tuned with some data from actual simulations.
  - The odds for the new playoff team will be determined from a random draw from this new distribution; the wild-card team can only get the #1 or #15 pick.
  - The odds for the rest of the teams are adjusted based on this result.

- The 1985 NBA Draft Lottery Conspiracy can be translated to the combination of a Bernoulli Random Trial + a Normal distribution.
  - First, a Bernoulli trial is performed (70% success/30% failure). This indicating whether or not the league gets caught trying to rig the lottery before it happens
    - If they do get caught (a failure result), the Knicks will be removed from the lottery and the odds will be redistributed to the other teams
  - If they do not get caught, their odds are modeled as a normal distribution with a mean of 0.25 (representing their increased odds of winning the lottery versus other teams due to the "frozen envelope") and a large standard deviation, illustrating that the result has high variability, since rigging the lottery is very risky (greatly increased odds, or greatly decreased odds of obtaining the number one pick).

