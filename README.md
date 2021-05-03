# NBA Draft Lottery: A Monte Carlo Simulation

Project Background:

The NBA Draft Lottery determines the order that the 14 worst teams will select upcoming talent in the NBA Draft. 

- Every team is assigned a certain set of odds to pick #1 overall in the draft, with worse-performing teams having the highest chance. 
- The worst three teams will have equal odds at selecting #1.
- After the first four picks have been set, the remaining teams will pick in inverse order, based on standings. 

A typical lottery ball machine is used to carry out the NBA Draft Lottery. 

- Fourteen Ping Pong Balls (Numbered 1 to 14) are placed in a lottery machine.
- Each 4 digit combination of the 14 balls is assigned to a certain team. There are a total of 1,001 possible combinations, of which 1 is discarded. 
  - The teams with the lowest records are assigned the most number of combinations based on their odds. 
- Drawings are conducted to select the first four picks. The remaining picks are determined in inverse order of the teams’ records. 

In the Drawing Process, for each combination drawn, the lottery machine is mixed for 20 seconds before drawing the first ball and 10 seconds before every subsequent ball. 

- The team that has been assigned the combination that is drawn will receive the pick (1-4) in question
- If the same team was drawn twice, the result is discarded. If the unassigned sequence is drawn, the result is also discarded.

