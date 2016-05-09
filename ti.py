from datetime import date,timedelta
def alldays(year):
	 d= date(year, 01, 02)
	 while d.year == year:
	 	if d.strftime("%A") != "Friday":
		  
     		     d += timedelta(7)				
		     yield d
for d in alldays(2016):
   print d
   

