# Time Series Analysis

## TIME SERIES DATA

* **Time series data** : Measurements of the same data taken over a period of
(usually regular) intervals of time. E.g. _Stock returns, temperature_

* **Cross sectional data** : A snapshot in time of a group of data. E.g. _Beer, Mammals, Iris_

#### Labs : [Taking a look at time series data](https://github.com/ga-students/DS_HK_1/wiki/Lesson-20-:-Time-Series-Analysis#time-series-analysis)

## DIFFERENCES IN TIME SERIES DATA

#### Assumptions of linear regression models
1. Linear relationship between dependent and independent
variables
1. Independence of the errors (serial correlation)
1. Homoscedasticity (constant variance of the errors)
	1. Over time
	1. Between the variab
1. Normality of the errors

Another important difference, unlike cross sectional models, the order of the data is VERY important.

#### Things to look for in time series data
* **Trends**, measurements tend to increase or decrease over time
* **Seasonality / Cyclicality**, An observable cycle in the data (days, years, weeks, secs, etc)

## DIAGNOSTIC TOOLS

**Normality of the errors**

#### Labs : [Residuals plot](https://github.com/ga-students/DS_HK_1/wiki/Lesson-20-:-Time-Series-Analysis#residuals-plot)

**Independence of the errors (serial correlation)**

Indicates that there is room for improvement in our model – there is some association in the data that we are not taking into account. Our tool for this is called an **Autocorrelation plot**

![](https://raw.githubusercontent.com/ga-students/DS_HK_1/eec7d9853a147b2ac0eaeeb7fc908aa2f47f8444/lessons/class/lesson20/assets/ac1.png)

![](https://raw.githubusercontent.com/ga-students/DS_HK_1/eec7d9853a147b2ac0eaeeb7fc908aa2f47f8444/lessons/class/lesson20/assets/ac2.png)

![](https://raw.githubusercontent.com/ga-students/DS_HK_1/eec7d9853a147b2ac0eaeeb7fc908aa2f47f8444/lessons/class/lesson20/assets/ac3.png)

![](https://raw.githubusercontent.com/ga-students/DS_HK_1/eec7d9853a147b2ac0eaeeb7fc908aa2f47f8444/lessons/class/lesson20/assets/ac4.png)

#### Labs : [Sunspots data ACF and PACF (correlograms)](https://github.com/ga-students/DS_HK_1/wiki/Lesson-20-:-Time-Series-Analysis#autocorrelation-and-partial-autocorrelation-in-the-correlogram)

## AUTOREGRESSIVE MODELS

Autoregressive models use the value at time -1 to predict the value at time 0

**Basic linear regression**

![ \gamma  =  \alpha  +  \beta _{x} +  \epsilon ](http://www.sciweavers.org/tex2img.php?eq=Y%20%3D%20%20%5Calpha%20%20%2B%20%20%5Cbeta%20_%7Bx%7D%20%2B%20%20%5Cepsilon%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

**Multivariate regression**

![Y = α + β_{1}x_{1} + β_{2}x_{2} + β_{3}x_{3} + ε](http://www.sciweavers.org/tex2img.php?eq=Y%20%3D%20%CE%B1%20%2B%20%CE%B2_%7B1%7Dx_%7B1%7D%20%2B%20%CE%B2_%7B2%7Dx_%7B2%7D%20%2B%20%CE%B2_%7B3%7Dx_%7B3%7D%20%2B%20%CE%B5&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

**Autoregressive regression AR(1)**

![ \gamma_{i}  =  \phi_{0} +  \phi_{1}\gamma_{i-1} + ε_{i}](http://www.sciweavers.org/tex2img.php?eq=%20%5Cgamma_%7Bi%7D%20%20%3D%20%20%5Cphi_%7B0%7D%20%2B%20%20%5Cphi_%7B1%7D%5Cgamma_%7Bi-1%7D%20%2B%20%CE%B5_%7Bi%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

* **Yi** : target variable
* **Φ0** : intercept (~ α, constant)
* **Φ1** : coefficient (~ β)
* **Yi-1** : lagged variable (~ x)
* **εi** : error

**Autoregressive regression AR(3)**

![ \gamma_{i}  =  \phi_{0} +  \phi_{1}\gamma_{i-1} + \phi_{2}\gamma_{i-2} + \phi_{3}\gamma_{i-3} + ε_{i}](http://www.sciweavers.org/tex2img.php?eq=%20%5Cgamma_%7Bi%7D%20%20%3D%20%20%5Cphi_%7B0%7D%20%2B%20%20%5Cphi_%7B1%7D%5Cgamma_%7Bi-1%7D%20%2B%20%5Cphi_%7B2%7D%5Cgamma_%7Bi-2%7D%20%2B%20%5Cphi_%7B3%7D%5Cgamma_%7Bi-3%7D%20%2B%20%CE%B5_%7Bi%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

### Further Reading
* **Stationarity**
* **Unit root processes**
* **MA** (Moving average) regressions
* **ARMA** (Autoregressive moving average) regressions
* **ARCH** (Autoregressive conditional heteroscedasticity)
* **EGARCH** (Exponential generalized ARCH)

#### Labs : [Other things to Play With](https://github.com/ga-students/DS_HK_1/wiki/Lesson-20-:-Time-Series-Analysis#other-things-to-play-with-arma-stationary-processes-unit-root-tests-macroeconomic-data)
