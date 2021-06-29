class Time:
    def __init__(self,h,m,s):
        self.__hour=h
        self.__minute=m
        self.__second=s
    def display(self):
        print("Hours : ",self.__hour)
        print("Minute : ",self.__minute)
        print("Seconds : ",self.__second)
    def __add__(self,other):
        hr=self.__hour + other.__hour
        mn=self.__minute + other.__minute
        sec=self.__second + other.__second
        time=(hr*60*60)+(mn*60)+sec
        total_hr=time//3600
        time%=3600
        total_min=time//60
        total_sec=time%60
        print()
        print("Total Time")
        print("HOURS : ",total_hr)
        print("MINUTES : ",total_min)
        print("SECONDS : ",total_sec)

t1=Time(5,46,52)
t2=Time(6,36,21)
t1.display()
t2.display()
t1+t2
