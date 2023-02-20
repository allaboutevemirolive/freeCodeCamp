def add_time(start_time, duration_time, starting_day=""):
    # Separate the start time into hours and minutes
    start_pieces = start_time.split()
    start_hour, start_minute = map(int, start_pieces[0].split(":"))
    end = start_pieces[1]

    # Calculate 24-hour clock format
    if end == "PM" :
        start_hour += 12
    
    # Separate the duration time into hours and minutes
    duration_hour, duration_minute = map(int, duration_time.split(":"))

    # Add hours and minutes
    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute

    # Handle minute overflow
    if new_minute >= 60 :
        hours_add = new_minute // 60
        new_minute -= hours_add * 60
        new_hour += hours_add

    # Handle hour overflow
    days_add = 0
    if new_hour >= 24 :
        days_add = new_hour // 24
        new_hour -= days_add * 24

    # Determine AM or PM and return to 12-hour clock format
    if new_hour < 12 :
        end = "AM"
    else :
        end = "PM"
        new_hour -= 12

    # Handle 12:00 edge case
    if new_hour == 0 :
        new_hour = 12

    # Handle next day or days later
    if days_add > 0 :
        if days_add == 1 :
            days_later = " (next day)"
        else :
            days_later = " (" + str(days_add) + " days later)"
    else :
        days_later = ""

    # Get day of the week if starting_day is provided
    if starting_day :
        week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        start_day = week_days.index(starting_day.lower().capitalize())
        new_day = (start_day + days_add) % 7
        day = ", " + week_days[new_day]
    else :
        day = ""

    # Format and return new time string
    new_time = f"{new_hour}:{new_minute:02d} {end}{day}{days_later}"
    return new_time
