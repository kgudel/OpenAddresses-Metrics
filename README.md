# OpenAddresses-Metrics

This respository contains a python file that runs from the command line.

It takes as input a regional OpenAddresses zip file, you have to point it at the folder \us\ in the folder and include a \ at the end of the path, and a .csv file which it will write data into.

It then writes 10 fields into that file:

1. State: The state abbreviation or file name
2. Total Rows: The number of rows in the file
3. Good: The number of good rows in the file. Good rows are defined as those where the lat, lon, number, and street fields are not blank, there are no quotation marks, the number field has at least one digit, the number field is not 0 or a negative number, and the row is not field descriptors.
4. City: The number of good rows in the file with a city.
5. Zip: The number of good rows in the file with a zip code.
6. Both: The number of good rows in the file with both a city and zip code.
7. Parsing: The number of rows in the file with a quotation mark as a proxy for parsing problems.
8. 'PO': The number of rows in the file  with no digits in the number field as a proxy for parsing and data problems.
9. '-9s': The number of rows in the file with a negative number in the number field
10. Missing Fields: The number of rows in the file with fewer than 9 fields.

This file also has 1 optional output: Summary ('-s', '--summary'). If the summary flag is turned out the file takes another file as input, where the summary data will be written. It then returns:

1. The number of good rows in a statewide file
2. The number of good rows in other files
3. The number of good rows with zips in either statewide or other rows, choosing the one with the most good rows with zips
4. The number of good rows with cities in either statewide or other rows, choosing the one with the most good rows with cities
5. The number of good rows with zips and cities in either statewide or other rows, choosing the one with the most good rows with zips and cities
