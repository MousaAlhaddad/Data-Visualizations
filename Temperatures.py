# Load the needed packages 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset as a DataFrame
Temperatures = pd.read_csv('Temperatures.csv',index_col='year')

# Plot Temperature Differences Using the Raw Data
plt.plot(Temperatures.avg_temp_local,label='Riyadh Temperatures')
plt.plot(Temperatures.avg_temp_global,label='Global Temperatures')
plt.legend(loc='center right')
plt.xlabel('Year')
plt.ylabel('Tempreture (ºC)')
plt.title('Temperature Differences Using the Raw Data')
plt.show()
Temperatures['moving_local'] = np.nan
Temperatures['moving_global'] = np.nan

# Calculat the 10-Years moving average
for x in range(1848,1848+len(Temperatures)-10):
    Temperatures.moving_local[x+10] = Temperatures['avg_temp_local'].loc[x:10+x].mean()
    Temperatures.moving_global[x+10] = Temperatures['avg_temp_global'].loc[x:10+x].mean()

# Plot Temperature Differences with 10-Years Moving Averages
# Note that the moving averages were used to smooth out the data.
plt.plot(Temperatures.moving_local,label='Riyadh Temperatures')
plt.plot(Temperatures.moving_global,label='Global Temperatures')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Temperature (ºC)')
plt.title('Temperature Differences with 10-Years Moving Averages')
plt.show()

# Print the conclusions
Text = ('1. It is apparent that Riyadh is a hot city with an average yearly temperature of {} degrees when'
      +' it is compared to the global temperature that averages {} degrees for the same period.'
      +'\n2. There is an increase in the global temperatures over the past 150 years.'
      + '\n3. The raising trend of the global temperature is also associated with an increasing trend'
      + ' of the temperatures in Riyadh.' 
      + '\n4. The temperatures both in Riyadh and globally has been increasing more evidently'
      + 'in the last 30 years.')
Text = Text.format(round(Temperatures.avg_temp_local.mean(),1),
                                      round(Temperatures.avg_temp_global.mean(),1))
print(Text)
