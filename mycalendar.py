__author__ = 'Irrevocable Cascade'


"""
This is an attempt to recreate the standard calendar class from Python as a learning exercise.
"""


"""
List of all available weekdays and months in dictionaries.
"""

WEEKDAYS = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday',
            6: 'Saturday'}

MONTHS = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
          7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

error = ValueError

class IllegalYearError(ValueError):
    def __init__(self, year):
        self.year = year
    def __str__(self):
        return "Bad year number %r; must be non-negative integer" % self.year

class IllegalMonthError(ValueError):
    def __init__(self, month):
        self.month = month
    def __str__(self):
        return "Bad month number %r; must be 1-12" % self.month


class MyCalendar(object):
    def __init__(self, year):

        if not 0 <= year:
            raise IllegalYearError(year)

        self.year = year
        self.makecalendar()
        self.calendardict = self.makecalendar()

    # Returns True if the year of the calendar is a leap year
    def isleapyear(self):
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        else:
            return False

    # What day of the week is a given day?
    def dayofweek(self, day, month):
        y = self.year
        if month == 1 or month == 2:
            month += 12
            y -= 1
        day_code = ((day + ((month + 1) * 26 // 10) + y + (y // 4) + 6 * (y // 100) + (
            y // 400)) % 7) + 6
        return WEEKDAYS[day_code % 7]

    def daysinmonths(self, month):
        if month == 2:
            if self.isleapyear():
                return 29
            else:
                return 28
        elif month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        else:
            return 30

    def makecalendar(self):
        # Create the data structure to represent the calendar. Returns the data structure.
        current_month = 1

        dictionary_of_months = {}

        while current_month <= 12:

            number_of_days = self.daysinmonths(current_month)
            dictionary_of_days = {}  # TODO MAKE THIS GENERATOR!

            for day in range(1, number_of_days + 1):
                dictionary_of_days[day] = self.dayofweek(day, current_month)

            dictionary_of_months[current_month] = dictionary_of_days

            current_month += 1

        return dictionary_of_months


class TextCalendar(MyCalendar):
    # Format top row of the calendar
    def formatmonthrow(self, month):
        return (MONTHS[month] + ' ' + str(self.year)).center(20) + '\n'

    # Format weekday row
    def formatweekdayrow(self):
        s = ''
        for weekday in WEEKDAYS:
            s += str(WEEKDAYS[weekday])[:2] + ' '
        s += '\n'
        return s

    # Figure out how many blank days we have based on the first weekday value of the month
    def formatfirstrow(self, first_day):

        # Swap key and values in WEEKDAYS, because we want to look up the numerical value of a weekday
        wdr = {v: k for k, v in WEEKDAYS.items()}

        return ' ' * 3 * wdr[first_day]

    def formatweekrows(self, weeks):

        week_string = ''
        count = 1
        s = ''

        for code, day in weeks.items():
            if day != 'Sunday':
                week_string += str(code).zfill(2) + ' '
                count += 1
            else:
                break

        # Remove the days we already added to the string
        for day in range(1, count):
            weeks.pop(day, None)

        s += week_string.rstrip()

        if len(s) != 0:
            s += '\n'

        week_string = ''

        for code, day in weeks.items():
            if day == 'Saturday':
                week_string += str(code).zfill(2) + '\n'
            else:
                week_string += str(code).zfill(2) + ' '

        s += week_string.rstrip()

        return s

    def printmonth(self, month):

        if not 0 < month <= 12:
            raise IllegalMonthError(month)

        month_string = self.formatmonthrow(month)
        month_string += self.formatweekdayrow()
        month_string += self.formatfirstrow(self.calendardict[month][1])
        month_string += self.formatweekrows(self.calendardict[month])

        return month_string

    def printyear(self):
        year_string = ' '

        for month in self.calendardict:
            year_string += self.printmonth(month) + '\n\n'

        return year_string


class HTMLCalendar(MyCalendar):
    def formatmonthrow(self, month, withyear):

        if withyear:
            return '<tr><th colspan="7" class="month_header">' + MONTHS[month] + ' ' + str(self.year) + '</th></tr>'

        return '<tr><th colspan="7" class="month_header">' + MONTHS[month] + '</th></tr>'

    def formatweekrow(self):

        s = '<tr>'
        for weekday in WEEKDAYS:
            s += '<th id="{0}" class="week_day">{0}</th>'.format(str(WEEKDAYS[weekday])[:2])

        s += '</tr>'
        return s

    def formatfirstrow(self, first_day):

        #Figure out how many blank cells we need.
        s = ''
        wdr = {v: k for k, v in WEEKDAYS.items()}
        bc = wdr[first_day]

        if bc != 0:
            s = '<tr>'

            for i in range(bc):
                s += '<td class="noday">&nbsp;</td>'

        return s

    def formatweekrows(self, weeks):

        week_string = ' '
        count = 1
        s = ''

        for code, day in weeks.items():
            if day != 'Sunday':
                week_string += '<th id="{0}" class="week_day">{1}</th>'.format(str(day[:2]), str(code).zfill(2))
                count += 1
            else:
                break

        # Remove the days we already added to the string
        for day in range(1, count):
            weeks.pop(day, None)

        s += week_string.rstrip() + '</tr>'

        if len(s) != 0:
            s += '\n'

        week_string = '<tr>'

        for code, day in weeks.items():
            if day == 'Saturday' and code < 31:
                week_string += '<th id="{0}" class="week_day">{1}</th>'.format(str(day[:2]),
                                                                               str(code).zfill(
                                                                                   2)) + '</tr>' + '\n' + '<tr>'
            else:
                week_string += '<th id="{0}" class="week_day">{1}</th>'.format(str(day[:2]), str(code).zfill(2))

        s += week_string.rstrip() + '</tr>'

        return s


    def printmonth(self, month, withyear):

        if not 0 < month <= 12:
            raise IllegalMonthError(month)

        code = '<table border="0" cellpadding="0" cellspacing="0" id="{0}" class="month">'.format(MONTHS[month][:3])
        code += '\n'
        code += self.formatmonthrow(month, withyear)
        code += '\n'
        code += self.formatweekrow()
        code += '\n'
        code += self.formatfirstrow(self.calendardict[month][1])
        code += self.formatweekrows(self.calendardict[month])

        tr_count = code.count("<tr>")

        if tr_count < 8:  # Fill the month table with extra rows, so all months have the same amount.
            code += '<tr>'
            code += 7 * '<td class="noday">&nbsp</td>'
            code += '</tr>'

        code += '\n</table>'
        return code

    def printyear(self, columns, withyear):

        # Put each month in a <td>. The amount of columns determines when we end the row.

        code = '<table border="0" cellpadding="0" cellspacing="0" id="{0}" class="year">'.format(self.year)
        code += '<tr>'
        c = 0
        # First a loop for the whole year:
        for month in self.calendardict:
            if c == columns:
                code += '</tr>\n<tr>'
                c = 0
            c += 1
            code += '\n<td>' + self.printmonth(month, withyear) + '</td>'
        code += '\n</table>'
        return code
