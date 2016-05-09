from datetime import date, timedelta
def alldays(year):
	 i=raw_input("Enter a number between 1 for friday to 6 to thursday:")
	 d= date(year, 01, int(i))
	 while d.year == year:
    		  yield d
     		  d += timedelta(7)

for d in alldays(2016):
   print d
   






