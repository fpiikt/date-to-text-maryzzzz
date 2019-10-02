"""
  Автор: Зеленская Мария, группа № P3355
"""


from match_dictionaries import MatchDictionaries



class DateConverter:
    """
       Class containing methods for representing date and time string as text
    """

    def __init__(self, date_sting):
        self.date = date_sting.split(' ')[0]
        self.time = date_sting.split(' ')[1]

        self.result = ''


    def convert_date_string(self):
        """
            Represents date and time string as text.
            Returns (str): Date as text or error
        """

        error = self.convert_date()
        if error:
            return error

        error = self.convert_time()
        if error:
            return error

        return self.result


    def convert_date(self):
        """
            Represents date string as text.
        """

        splitted_string = self.date.split('.')
        day = int(splitted_string[0])
        month = int(splitted_string[1])
        year = splitted_string[2]

        if day < 1 or day > 31:
            return 'Некоррктный день'

        if month < 1 or month > 12:
            return 'Некоррктный месяц'

        if int(year) < 1:
            return 'Некоррктный год'

        self.convert_day(day)
        self.convert_month(month)
        self.convert_year(year)

        return ''


    def convert_day(self, day):
        """
            Represents day string as text.
            Args:
            day (int): number of day to represent as text
        """

        self.result += MatchDictionaries.days[day] + ' '


    def convert_month(self, month):
        """
            Represents month string as text.
            Args:
            month (int): number of month to represent as text
        """

        self.result += MatchDictionaries.months[month] + ' '


    def convert_year(self, year):
        """
            Represents year string as text.
            Args:
            year (int): number of year to represent as text
        """

        list_year = [int(x) for x in list(year)]

        if list_year[0] != 0:
            if list_year[1] == 0 and list_year[2] == 0 and list_year[3] == 0:
                self.result += MatchDictionaries.year_thousands_number_rounded[list_year[0]] + \
                               MatchDictionaries.thousands['rounded'] + ' года '
                return
            else:
                self.result += MatchDictionaries.year_thousands_number[list_year[0]] + ' '
                if list_year[0] == 1:
                     self.result += MatchDictionaries.thousands['singular'] + ' '
                elif list_year[0] in [2, 3, 4]:
                    self.result += MatchDictionaries.thousands['plural_alt'] + ' '
                else:
                    self.result += MatchDictionaries.thousands['plural'] + ' '

        if list_year[1] != 0:
            if list_year[2] == 0 and list_year[3] == 0:
                self.result += MatchDictionaries.hundreds_rounded[list_year[1]] + ' года '
                return
            else:
                self.result += MatchDictionaries.hundreds[list_year[1]] + ' '

        if list_year[2] != 0:
            if list_year[3] == 0:
                self.result += MatchDictionaries.tens_rounded[list_year[2]] + ' года '
                return
            else:
                if list_year[2] == 1:
                    ten = str(list_year[2]) + str(list_year[3])
                    self.result += MatchDictionaries.first_ten_year[int(ten)] + ' года '
                    return
                else:
                    self.result += MatchDictionaries.tens[list_year[2]] + ' '

        if list_year[3] != 0:
            self.result += MatchDictionaries.year_last_number[list_year[3]] + ' года '

        return


    def convert_time(self):
        """
           Represents date string as text.
       """

        splitted_string = self.time.split(':')
        hours = int(splitted_string[0])
        minutes = int(splitted_string[1])
        seconds = int(splitted_string[2])

        if hours < 0 or hours > 23:
            return 'Некоррктный час'

        if minutes < 0 or minutes > 59:
            return 'Некоррктная минута'

        if seconds < 0 or seconds > 59:
            return 'Некоррктная секунда'

        self.convert_hours(hours)
        self.convert_minutes(minutes)
        self.convert_seconds(seconds)


    def convert_hours(self, hours):
        """
            Represents hours string as text.
            Args:
            hours (int): number of hours to represent as text
        """

        if hours < 10:
            self.result += MatchDictionaries.decimials[hours]['hours'] + ' '

        elif hours < 20:
            self.result += MatchDictionaries.first_ten[hours] + ' '

        else:
            list_hour = list(str(hours))
            self.result += MatchDictionaries.tens[int(list_hour[0])] + ' '
            self.result += MatchDictionaries.decimials[int(list_hour[1])]['hours'] + ' '

        if hours in [10, 11, 12]:
            self.result += MatchDictionaries.hours['plural'] + ' '

        elif hours % 10 == 1:
            self.result += MatchDictionaries.hours['singular'] + ' '

        elif hours % 10 > 0 and hours % 10 < 5:
            self.result += MatchDictionaries.hours['plural_alt'] + ' '

        else:
            self.result += MatchDictionaries.hours['plural'] + ' '


    def convert_minutes(self, minutes):
        """
            Represents minutes string as text.
            Args:
            minutes (int): number of minutes to represent as text
        """

        if minutes < 10:
            self.result += MatchDictionaries.decimials[minutes]['else'] + ' '

        elif minutes < 20:
            self.result += MatchDictionaries.first_ten[minutes] + ' '

        elif minutes % 10 == 0:
            self.result += MatchDictionaries.tens[minutes // 10] + ' '

        else:
            list_minute = list(str(minutes))
            self.result += MatchDictionaries.tens[int(list_minute[0])] + ' '
            self.result += MatchDictionaries.decimials[int(list_minute[1])]['else'] + ' '

        if minutes in [10, 11, 12]:
            self.result += MatchDictionaries.minutes['plural'] + ' '

        elif minutes % 10 == 1:
            self.result += MatchDictionaries.minutes['singular'] + ' '

        elif minutes % 10 > 0 and minutes % 10 < 5:
            self.result += MatchDictionaries.minutes['plural_alt'] + ' '

        else:
            self.result += MatchDictionaries.minutes['plural'] + ' '


    def convert_seconds(self, seconds):
        """
            Represents seconds string as text.
            Args:
            seconds (int): number of seconds to represent as text
        """

        if seconds < 10:
            self.result += MatchDictionaries.decimials[seconds]['else'] + ' '

        elif seconds < 20:
            self.result += MatchDictionaries.first_ten[seconds] + ' '

        elif seconds % 10 == 0:
            self.result += MatchDictionaries.tens[seconds // 10] + ' '

        else:
            list_second = list(str(seconds))
            self.result += MatchDictionaries.tens[int(list_second[0])] + ' '
            self.result += MatchDictionaries.decimials[int(list_second[1])]['else'] + ' '

        if seconds in [10, 11, 12]:
            self.result += MatchDictionaries.seconds['plural']

        elif seconds % 10 == 1:
            self.result += MatchDictionaries.seconds['singular']

        elif seconds % 10 > 0 and seconds % 10 < 5:
            self.result += MatchDictionaries.seconds['plural_alt']

        else:
            self.result += MatchDictionaries.seconds['plural']



if __name__ == '__main__':
    assert DateConverter('21.09.1000 00:00:00').convert_date_string() == 'Двадцать первое сентября тысячного года ноль часов ноль минут ноль секунд'
    assert DateConverter('01.12.1997 21:45:23').convert_date_string() == 'Первое декабря одна тысяча девятьсот девяносто седьмого года двадцать один час сорок пять минут двадцать три секунды'
    assert DateConverter('10.04.0950 12:12:12').convert_date_string() == 'Десятое апреля девятьсот пятидесятого года двенадцать часов двенадцать минут двенадцать секунд'
    assert DateConverter('12.12.5244 08:10:45').convert_date_string() == 'Двенадцатое декабря пять тысяч двести сорок четвертого года восемь часов десять минут сорок пять секунд'
    assert DateConverter('09.13.1253 22:12:43').convert_date_string() == 'Некоррктный месяц'
    assert DateConverter('32.02.2154 14:59:59').convert_date_string() == 'Некоррктный день'
    assert DateConverter('02.11.1254 24:45:12').convert_date_string() == 'Некоррктный час'
