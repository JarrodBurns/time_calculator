
def add_time(start_time, duration_time, day_of_week=None):
    """
    Adds the duration time to the start time and returns the result.

    If the function is given an optional starting day of the week
    parameter, then the output will display the day of the week
    of the result.
    """
    start_time = start_time.lower()
    ampm_hour = int(start_time.split(":")[0])
    ampm_minute = int(start_time.split()[0].split(":")[1])
    am_or_pm = start_time.split()[1].lower()
    add_hour = int(duration_time.split(":")[0])
    add_minute = int(duration_time.split(":")[1])

    # preparing day_of_week if user provided
    if day_of_week is not None:
        day_of_week = day_of_week.lower()

    # Converting to 24 hour time
    if am_or_pm == "pm":
        ampm_hour += 12

    tfh_plus_hours = ampm_hour + add_hour
    tfh_plus_minutes = ampm_minute + add_minute
    tfh_plus_days = 0

    # Elapsing total minutes
    while tfh_plus_minutes >= 60:
        tfh_plus_minutes -= 60
        tfh_plus_hours += 1

    # Elapsing total hours
    while tfh_plus_hours >= 24:
        tfh_plus_hours -= 24
        tfh_plus_days += 1

    def days_later(tfh_plus_days, day_of_week):
        """
        Counts the number of days elapsed.
        """
        if tfh_plus_days < 1 and day_of_week is not None:
            return f", {day_of_week.title()}"
        if tfh_plus_days < 1 and day_of_week is None:
            return ""
        if tfh_plus_days == 1:
            return ", (next day)"
        return f", ({tfh_plus_days} days later)"

    def convert_to_ampm(tfh_plus_hours, tfh_plus_minutes):
        """
        Converts time from 24 hour format in order to
        display 12 hour format to the user.
        """
        if tfh_plus_hours == 0:
            return f"{(tfh_plus_hours + 12):02}:{tfh_plus_minutes:02} AM"
        if tfh_plus_hours < 12:
            return f"{tfh_plus_hours:02}:{tfh_plus_minutes:02} AM"
        if tfh_plus_hours == 12:
            return f"{tfh_plus_hours:02}:{tfh_plus_minutes:02} PM"
        return f"{(tfh_plus_hours - 12):02}:{tfh_plus_minutes:02} PM"

    def day_addition(day_of_week, tfh_plus_days):
        """
        When a day of the week is defined:
        Returns day of the week + provided days.
        """
        my_dict = {
            "sunday": 0,
            "monday": 1,
            "tuesday": 2,
            "wednesday": 3,
            "thursday": 4,
            "friday": 5,
            "saturday": 6
        }

        if day_of_week is not None and tfh_plus_days >= 1:

            x = my_dict[day_of_week] + tfh_plus_days

            while x > 6:
                x -= 7

            return f", {list(my_dict)[x].title()}"
        return ""

    return f"{convert_to_ampm(tfh_plus_hours, tfh_plus_minutes)}{day_addition(day_of_week, tfh_plus_days)}{days_later(tfh_plus_days, day_of_week)}"
