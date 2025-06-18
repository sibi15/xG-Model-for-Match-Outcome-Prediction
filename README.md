# xG Model for Match Prediction
This project is a basic football match simulation tool built in Python that forecasts the outcome of a game based on shot-level expected goals (xG). Users input xG values for each shot taken by both the home and away teams. The model simulates 10,000 matches using a probabilistic approach to goal scoring and outputs the percentages of each possible result: home win, away win, or draw.

Tools & Concepts:
- Expected Goals (xG): Each shot is evaluated using its probability of becoming a goal.
- Monte Carlo Simulation: Repeats the match 10,000 times to capture realistic variation.
- Random Module: Determines goal outcomes based on shot xG.

Features:
- User-defined shot data (number of shots + xG per shot)
- Shot-by-shot probability-based scoring
- Calculates winner of each match
- Aggregates outcomes to show statistical probability for each result
- Simple and interactive CLI-based tool
