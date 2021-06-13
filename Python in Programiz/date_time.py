import datetime as dt
# To know the date in datetime module.
current_date=dt.date.today()
print(current_date)
# To know the time at current and we can assign it.
current_time=dt.datetime.now()
print(current_time)
time1=dt.time(9,56,30,45677) # (hour,min,sec,microsec)
print(time1)
# to know the date and time at a single line commmand.
datetime1=dt.datetime(2021,5,31,9,58,50,4323) #(year,month,date,hour,min,se,microsec)
print(datetime1)
