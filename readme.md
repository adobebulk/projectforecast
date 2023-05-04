## Project: Forecast
2020-03-29
C.T. Smith

# Overview
This project is to establish an easy-to-read daily forecast, meant to be digested while quickly performing morning tasks. The end state objective is a small printout (think: receipt) to view in the morning while showering, brushing teeth, making coffee, in order to quickly determine the proper clothing attire to wear. Note: this is distinctly different that a smartphone alert because a smartphone is typically not in use at the time of these quick morning activities. 

# Delivery
The current objective is to deliver the product as a printed statement or receipt, at a certain time every morning, of the local weather forecasts. Because the NOAA data is readily available via FTP or other web query (please reference https://www.weather.gov/tg/dataprod), the NOAA NWS data will be used and parsed, as desired, to provide the desired outcome.

Update 2021-06-05: The zone maps are located here: https://www.weather.gov/pimar/PubZone	

##Format
The initial stages of the project will include a simple text file printout:

```

WEATHER STATEMENT
2020-04-20 - 0500H CDT
PARSED BY SMITH WEATHER
FROM THE NATIONAL WEATHER SERVICE
. . . 


TODAY		.	.	.	MONDAY
HIGH		.	.	.	75F
LOW		    .	.	.	53F
PRECIP	    .	.	.	50%
WIND		.	.	.	5G15NNE

###
```
