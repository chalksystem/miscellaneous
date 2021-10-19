

class calendar:

    def __init__(self, year, control=2020, dayTracker=None):


        self.year = year 
        self.control = control
        self.dayTracker = dayTracker = self.control

        if year >= control:
            for i in range(control, year):
                if i%4 == 0:
                    dayTracker += 366
                else:
                    dayTracker += 365

        else:
            while year < control:
                control -= 28
                # self.control = control
                # return    
            for i in range(control, year):
                    if i%4 == 0:
                        dayTracker += 366
                    else:
                        dayTracker += 365

        self.dayTracker = dayTracker
        self.control = control


    def getDays(self ,monthIndex = {}, days = []):


        self.monthIndex = monthIndex
        self.days = days
        monthIndexList = []
        months = ['January','February','March','April','May','June','July','August','September','October','November','December']

        for i in range(1,len(months)+1):
            monthIndex[i] = months[i-1]
        self.monthIndex = monthIndex

        for i in monthIndex: 
            while i < 8:
                if i <= 2:
                    if i == 1:
                        monthIndexList.append(31)
                    else:
                        if self.year % 4 == 0:
                            monthIndexList.append(29)
                        else:
                            monthIndexList.append(28)
                elif i%2 == 0:
                    monthIndexList.append(30)
                else:
                    monthIndexList.append(31)
                break
            while i >= 8:
                if i%2 == 0:
                    monthIndexList.append(31)
                else:
                    monthIndexList.append(30)
                break

        self.days = monthIndexList

    def getCalendar(self, dayOneIndex = {}, startDay=None):

        self.dayOneIndex = dayOneIndex
        self.startDay = startDay = self.dayTracker

        weekDays = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']


        month = 1
        dayList = self.days[:]
        print('\n')
        for k in self.days:
            print(format(0,'%dd'% (14 - (len(self.monthIndex[month])- 2))),end=f'\b{self.monthIndex[month]} \n\n')


            for x in weekDays:
                print(format(0,'2d'),end=f'\b{x[0]} ')
            print('\n')
            dayOneTracker = 0
            day = k

            num = 1
            lineNum = 1
            spaceNum = 0
            for i in range(1-(startDay-1),day+1):
                if num > 7:
                    if i > 1:
                        print('\n')

                        lineNum += 1
                        num = 1
                    else:
                        num = 1
                if i < 1:
                    if -i <= -1:
                        i = 0
                        num += 1
                        print("%s" % f"{format(i,'2d')}",end=' ')
                    else:
                        num += 1
                        
                else:
                    if len(dayList) == 13 - month:
                        dayOneIndex[self.monthIndex[month]] = num
                        month += 1
                    if spaceNum == 0:
                        for j in range(1,num):
                            j = 0
                            print("%s" % f"{format(j,'3d')}\b",end=' ')
                        spaceNum += 1
                    num += 1
                    print("%s" % f"{format(i,'2d')}",end=' ')
            print('\n\n')
            startDay += k
            dayList.pop(0)
        self.dayOneIndex = dayOneIndex


# thisYear = calendar(2021)
# thisYear.getDays()
# thisYear.getCalendar()