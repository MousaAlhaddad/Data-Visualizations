# Data Visualizations
To list some examples of using Python Matplotlib and Seaborn libraries in producing informative data visualizations

## Scripts 
### [Game.py](Scripts/Game.py)
It produces an adapted bar chart that involves two categorical variables (matches and teams) and one quantitative variable (goals). 
### [Temperatures.py](Scripts/Temperatures.py)
It is based on a real [data set](Data/Temperatures.csv) that was was extracted for a project in the [Udacity's Data Analyst Nanodegree Program](https://www.udacity.com/course/data-analyst-nanodegree--nd002) and contains the yearly Riyadh and global temperatures between 1848 and 2013. The results are two time-series chars. Each uses one categorical variable (Riyadh vs the globe) and two quantitative variables (years and temperatures). On the second chart, however, the 10-year moving averages were used to smooth out the data. 
### [Insulin.py](Scripts/Insulin.py)
It is demonstrates the primary visualizations for univariate and bivariate data analysis producing five different charts: a bar chart, a histogram, a scatter plot, a clustered bar chart and a box plot. The dataset is not real. It was generated to consist of the data of 700 diabetic patients. 350 patients are from the Middle East countries while the rest are from East Asia. For each patient, the type of diabetes (type 1 or type 2), the age at diagnosis, the weight and the insulin dose were recorded. 
- The bar chart shows that type 2 diabetes is more common than type 1 diabetes.
- The histogram shows that the age distribution is bimodal due the age differences of the two types of diabetes. 
- The scatter plot shows the direct linear relationship between patients' weights and their insulin doses.
- The clustered bar chart shows the differences in the percentages of type 1 and type 2 diabetes between the Middle East and East Asia. 

## Jupyter Notebooks	
There is a corresponding Jupyter Notebook for each of the above scripts with the same name. The notebooks are found [here](Jupyter%20Notebooks). They were added to make the visualizations apparent on the GitHub website. 

## Dependencies
* [NumPy](https://www.numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)

## Contributing to the Repository
All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
