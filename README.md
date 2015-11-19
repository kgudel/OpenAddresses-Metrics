# OpenAddresses-Metrics

This respository contains a python file that runs from the command line.

It takes as input a regional OpenAddresses zip file, you have to point it at the folder \us\ in the folder and include a \ at the end of the path, and a .csv file which it will write data into.

It then writes 10 fields into that file:

1. State: The state abbreviation or file name
2. Total Rows: The number of rows in the file
3. Good: The number of good rows in the file
4. City: The number of good rows in the file with a city
5. Zip: The number of good rows in the file with a zip code
6. Both: The number of good rows in the file with both a city and zip code
7. Parsing: The number of rows in the file with a quotation mark as a proxy for parsing problems
8. 'PO': The number of rows in the file  with no digits in the number field as a proxy for parsing and data problems
9. '-9s': The number of rows in the file with a negative number in the number field
10. Missing Fields: The number of rows in the file with fewer than 9 fields

This file also has 4 optional outputs each of which require an output file if they are choosen to run.

1. -g: Outputs all good files
2. -c: Outputs all good files with a city
3. -z: Outputs all good files with a zip code
4. -b: Outputs all good files with a city and a zip code

Each of these outputs include 6 rows:

1. Lat
2. Lon
3. Number
4. Street
5. City
6. Zip
