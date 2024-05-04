# Latitude and Weather Analytics: A Tool for Destination Selection

# Project Overview

This project explores how weather varies with latitude and identifies ideal travel destinations based on user-specified weather conditions. Using Python and several APIs, the analysis includes fetching random cities, retrieving their weather data, and visualizing the relationships between latitude and various weather features. The project further extends to use weather data to find hotels in ideal locations.

## Installation and Usage

Ensure Python is installed on your system along with the following libraries:
- pandas
- matplotlib
- requests
- numpy
- hvplot
- scipy

To install the necessary Python packages, run:

```bash
pip install pandas matplotlib requests numpy hvplot scipy
```

# Introduction
This analysis aims to understand how different weather parameters correlate with latitude. By dividing the globe into northern and southern hemispheres, we also aim to see if these relationships differ based on being closer to or farther from the equator.

# Project Goals
- Analyze the relationship between latitude and various weather parameters like temperature, humidity, cloudiness, and wind speed.
- Identify areas with ideal weather conditions and locate hotels in these regions using the GeoApify API.

# Data Pre-processing and Gathering
Data was gathered using:

- **CityPy:** To randomly select cities based on latitude and longitude.
- **OpenWeather API:** To fetch weather data for these cities.
- **GeoApify API:** To find hotels in cities with ideal weather conditions.

Data cleaning involved removing duplicates, handling missing values, and splitting the dataset into northern and southern hemisphere data for separate analysis.

## Data Unbiasing Approach

Our data gathering strategy is designed to avoid bias by using random selection methods that ensure a diverse distribution of cities globally. This approach helps in achieving a balanced representation across different geographical areas, enhancing the validity of our analysis. The image below illustrates the geographic spread of cities included in our study.

![Breakout of Cities](https://imgur.com/XejWKvL.png)

# Sample Visualizations and Analysis

![Linear Regression: Latitude vs Temperature](https://imgur.com/q3kO9S2.png)


![Linear Regression: Latitude vs Wind Speed (m/s)](https://imgur.com/uuFdP8s.png)


![Scatter Plot: Latitude vs Cloudiness %](https://imgur.com/PSPshZS.png)


![Scatter Plot: Latitude vs Humidity %](https://imgur.com/9Mlak10.png)



# Hotel Finder Visualizations

![Hotel Finder](https://imgur.com/XjJeU60.png)

# Major Findings
- Temperature shows a strong correlation with latitude, with higher temperatures near the equator and lower as we move away. Pearson r was close to 1.
- Other features (humidity, cloudiness, wind speed) showed little to no correlation with latitude. Pearson r was close to 0.
- The split analysis for northern and southern hemispheres confirmed the temperature trends but did not reveal new patterns for other features.

# Limitations and Future Development
- Future iterations could automate the retrieval of more periodic data to observe seasonal changes.
- Expanding the analysis to include elevation data might provide deeper insights.

# Conclusion
This study reaffirms the common understanding of temperature variation with latitude and provides a useful tool for identifying potential travel destinations based on weather preferences. The integration of hotel data further extends its practical application for planning trips.

References
- [CityPy documentation](https://github.com/wingchen/citipy)
- [OpenWeather API documentation](https://openweathermap.org/current)
- [GeoApify API documentation](https://apidocs.geoapify.com/docs/places/#about)
- [Matplotlib documentation](https://matplotlib.org/stable/)
- [Pandas documentation](https://pandas.pydata.org/docs/)
- [HVPlot documentation](https://hvplot.holoviz.org/user_guide/index.html)

