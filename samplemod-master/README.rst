ClearTax Coding Assignment
============================

This assignment is used to implement following two functionalities:
a.	URL with the Top 5 highest throughput (highest number of times called) along with the frequency

b.	Max, Min and average response times for each distinct api

**Sample Output**

*Reference output format*:

1.	Top 5 highest throughput URLs:

Method	URL	Frequency
PUT	/book/{id}	7
GET	/book/{id}	5
POST	/person/add	4
GET	/book/{id}/return	4
GET	/person/all	3

2.	Time taken for each endpoint:

Method	URL	Min Time	Max Time	Average Time
PUT	/book/{id}	20	234	98.57
GET	/book/{id}	37	110	65.4
POST	/person/add	60	140	97.25
GET	/book/{id}/return	45	78	63
GET	/person/all	60	102	86.67
GET	/person/{id}/details	35	87	66.67





