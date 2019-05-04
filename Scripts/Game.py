# Load the needed packages 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sb

"""
Create a new DataFrame with 38 matches and random goals for each team in each match 
"""
Dict =  {}
Dict['Match'] = ['Match {}'.format(x) for x in range(1,39)]*2
Dict['Team'] = ['Player Team']*38 + ['Opposing Team']*38
# Get a random number of gaols between 0 and 5 for 38 matches * 2 teams (38*2=76) 
# Having p=[0.05,0.25,0.4,0.15,0.1,0.05] changes the probabilities of each number of goals 
# Examples: the probability of scoring 2 goals is 0.30 and the probability of scoring 5 goals is 0.025
Dict['Goals'] = list(np.random.choice([0,1,2,3,4,5],76,p=[0.125,0.25,0.3,0.25,0.05,0.025]))
df = pd.DataFrame(Dict)
# Change the size of the figure
plt.figure(figsize=(20,10))

# Plot the player team goals in each match with a blue color
# Note that the width is negative 
plt.bar(range(38), df[df.Team=='Player Team'].Goals,color=sb.color_palette()[0],
        width=-0.3,align='edge',label='Player Team Goals');

# Plot the opposing team goals in each match with a red color
# Note that the width is postive 
plt.bar(range(38), df[df.Team=='Opposing Team'].Goals,color=sb.color_palette()[3],
        width=0.3,align='edge',label='Opposing Team Goals');

# Show legends 
plt.legend()

# Show the matches in the x ticks with rotation 
plt.xticks(range(38),df[df.Team=='Player Team'].Match,rotation=90);
