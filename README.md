# data_manipulation
## Periodic Data Processing

The objective is to write a python program to periodically and automatically do the data manipulation every day. 
 
I have written 2 scripts which both take as input *d1.csv* and *d2.csv* and output a *data_final.csv* file. The script titled *data_processing.py* has to be run manually and the script titled *periodic_data_processing.py* makes use of a scheduler to run every day at 08:30.

Both scripts perform the following functions on the input:
1.	process all csvs and output one processed csv including headers
2.	delete the rows which do not contain a name
3.	ensure the price column contains only numbers
4.	split the name column into first and last columns.
6.	add a new column, which will be True if the price is greater than 100, and False otherwise.
 
•	The scripts are directly executable from the command line, so you don't need to open a IDE in order to clean the data

•	The processed csv for inputs *d1.csv* and *d2.csv* is titled *data_final.csv* and is already included in the repository
 
