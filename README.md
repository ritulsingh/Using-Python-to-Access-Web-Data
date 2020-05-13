# Using-Python-to-Access-Web-Data
This is repository all about the solution of "Using Python to Access Web Data " in coursera assignment.

# Week 2 Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

Data Files
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)

Actual data: http://py4e-data.dr-chuck.net/regex_sum_383952.txt (There are 84 values and the sum ends with 667)

These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.

Data Format

The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. Here is a sample of the output you might see:


The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none).

Handling The Data
The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

# Week 3 Exploring the HyperText Transport Protocol

You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.

http://data.pr4e.org/intro-short.txt
There are three ways that you might retrieve this web page and look at the response headers:

Preferred: Make sure to change the code to retrieve the above URL - the values are different for each URL.
Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
Use the telnet program as shown in lecture to retrieve the headers and content.
Enter the header values in each of the fields below and press "Submit".


Solution:

Last-Modified:
Sat, 13 May 2017 11:22:22 GMT
 
ETag:
"1d3-54f6609240717"
 
Content-Length:
467
 
Cache-Control:
max-age=0, no-cache, no-store, must-revalidate
 
Content-Type:
text/plain


# Week 4 Scraping Numbers from HTML using BeautifulSoup
In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)

Actual data: http://py4e-data.dr-chuck.net/comments_383954.html (Sum ends with 20)

You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

# Week 5 Extracting Data from XML

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)

Actual data: http://py4e-data.dr-chuck.net/comments_383956.xml (Sum ends with 42)

You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.                                                                                     
