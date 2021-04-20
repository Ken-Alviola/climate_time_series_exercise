# Climate-Time-Series-Exercise-Manila

### Description 
- Project in analyzing climate data from 1845-2013 for the city of Manila,Philippines

### Goals
- The goals are to look for trends in the data and create a predicitive model

---------------------------------
### Data Dictionary
---
| Column | Definition | Data Type |
| ----- | ----- | ----- |
|AverageTemperatureUncertainty| 95% confidence level of average temp| float|
|month| month number| int|
|year| year| int|
|decade| specific span of 10 years| int|

---------------------------------------------------
| Target | Definition | Data Type |
| ----- | ----- | ----- |
|AverageTemperature| Average temperature taken on 1st of month| float|

--------------------------------------------------
### Hypotheses
**1. Is the mean temp significantly different between the last 84 years and the 84 years before that?**
- null_hypothesis = "The mean temps are the same between the last 84 years and the 84 years before that"
- alternative_hypothesis = "The mean temps are significantly different between the last 84 years and the 84 years before that"

--------------------------------------------------

### Project Plan
1. Acquire climate data from kaggle page https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data
2. Prepare data by removing unnecessary/redundant columns, dealing with nulls, and scaling variables for use with ML models
3. Explore data using time series exploration
5. Create ML models based on timeseries methods and choose best performing for test data

---------------------------------------------------
### Project Takeaways
- Noticable uptrend over the last 168 years
- Mean temps between rainy and dry seasons are significantly different
- Mean temps over each decade have little varirance

--------------------------------------------------
### How to re-create
- All necessary files are in this repository so the best method would be to git clone and run wrangle_manila()
- Exploration and data cleaning notebooks are available as well and can be experimented with.
- Run explore_manila notebook. 
- Adjust exploration and modeling to your liking
