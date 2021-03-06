from ics import Calendar, Event, alarm
from .text_processor import text_pipeline
from datetime import datetime
from datetime import timedelta


def times_per_day(instruction):
    directive = instruction[0]
    for index, elem in enumerate(directive):
        times = elem
        if times.isdigit():
            if (directive[index + 1] == "TIMES") | (directive[index + 1] == "DAILY"):
                return int(times)
        elif index == len(directive) - 1:
            return 1


def is_in_time(start, end, current):
    if start < end:
        return start.now().strftime("%H:%M:%S") <= current.now().strftime("%H:%M:%S") <= end.now().strftime("%H:%M:%S")
    else:
        return (current.now().strftime("%H:%M:%S") >= start.now().strftime("%H:%M:%S")) | (current.now().strftime("%H"
                                                                                                                  ":%M:%S") <= end.now().strftime("%H:%M:%S"))


def create_log_file(instruction):
    start = datetime.now().replace(hour=8, minute=0, second=0)
    end = datetime.now().replace(hour=22, minute=0, second=0)
    time_unit_one = 0
    file_name = open('event_log_file.txt', 'w')
    if len(instruction[0]) == 0:
        # file_name.write("Please take another photo. The camera is having a hard time grabbing your information\n")
        # file_name.write("1. Make sure there isn't a glare in the photo and there is natural lighting\n")
        # file_name.write("2. Make sure that the text on the bottle is clearly in frame\n")
        file_name.write("Another One")
        file_name.close()
    # So at this point if your event_log_file.txt contains only "Another One" they should take another picture.
    else:
        file_name.write("This is the event below:\n")
        file_name.write(
            ' '.join(instruction[2]) + ", " + ' '.join(instruction[3]))
        if instruction[1].__contains__("DAY") | instruction[1].__contains__("DAYS"):
            for elem in instruction[1]:
                if elem.isdigit():
                    time_unit_one = int(elem)
                    break
                else:
                    time_unit_one = 5
            curr_time = datetime.now() + timedelta(minutes=1)
            event = curr_time
            num_times = times_per_day(instruction)
            file_name.write("\nThe alarms are set for: \n")

            if not is_in_time(start, end, curr_time):
                temp_event = datetime.strptime(start, '%H:%M:%S')
            else:
                temp_event = curr_time

            for _ in range(time_unit_one):
                file_name.write(str(event) + "\n")
                for time in range(num_times - 1):
                    event += timedelta(hours=4)
                    file_name.write(str(event) + "\n")
                event = temp_event + timedelta(days=1)
                temp_event += timedelta(days=1)

        elif instruction[1].__contains__("HOURS") | instruction[1].__contains__("HOUR"):
            for elem in instruction[1]:
                if elem[0].isdigit():
                    print(elem[0])
                    time_unit_one = int(elem[0])
                    break
                else:
                    time_unit_one = 1
            curr_time = datetime.now() + timedelta(minutes=30)
            event = curr_time
            num_times = times_per_day(instruction)
            file_name.write("\nThe alarms are set for: \n")
            for _ in range(20):
                file_name.write(str(event) + "\n")
                event += timedelta(hours=time_unit_one)

        file_name.close()


# def create_ics_file(duration_directive_tuple):
#     c = Calendar()
#     e = Event()
#     a = alarm
#     directive = duration_directive_tuple[0]
#     duration = duration_directive_tuple[1]
#     frequency = {"ONCE": 1, "ONE": 1, "TWICE": 2, "THRICE": 3, "THREE": 3, "FOUR": 4}
#
#     # Add Error Handling stuff
#     medication = str(input("What would you like to call this medicine: "))
#     print(" ")
#     # Enter in this form '8AM' or '8PM' or '8:30AM' or '8:30PM'
#     time_to_start = str(input("When would you like to start this medication ?: "))
#     print(" ")
#     while True:
#         try:
#             quantity = int(input("How many pills are in the bottle: "))
#             print(" ")
#         except ValueError:
#             print("Please Enter a whole number!!!\n")
#             continue
#         else:
#             break
#
#     if "HOURS" in duration:
#         # Look for and extract the number range of hours
#         hourly_range = 1
#         hours = [hour for hour in duration if hour[0].isnumeric()]
#
#         # Gets rid of any extra numbers left from the preprocessing step
#         if len(hours) > 1:
#             hours = hours[-1]
#
#         # This is to check for an hourly range like 4-6 HOURS
#         if hours[0].__contains__("-"):
#             # default to one hour
#             print("Your are meant to take your medication every", hours[0], "hours")
#             while True:
#                 try:
#                     hourly_range = int(input("In how many hours should I remind you to take your medication?: "))
#                     print(" ")
#                 except ValueError:
#                     print("Please Enter a single number in the", hours[0], "hour", "range")
#                     print(" ")
#                     continue
#                 if (hourly_range > 6) | (hourly_range < 4):
#                     print("Please Enter a single number in the", hours[0], "hour", "range")
#                     print(" ")
#                     continue
#                 else:
#                     break
#
#             print("A reminder has been set for every", str(hourly_range), "hours")
#
#             # # Create the event
#             # e.name = " ".join(directive) + '(' + medication + ')'
#             # date_time = datetime.now()
#             # e.begin = date_time
#             # a.duration = hourly_range
#             # a.repeat = 20
#             # e.alarms = a
#             # c.events.add(e)
#             #
#             # c.events
#             # with open('prescription.ics', 'w') as my_file:
#             #     my_file.writelines(c)
#
#         else:
#             print("Your are meant to take your medication every", hourly_range, "hours")
#
#             # Create the event
#             # e.name = " ".join(directive) + '(' + medication + ')'
#             # date_time = datetime.now()
#             # e.begin = date_time
#             # a.duration = hourly_range
#             # a.repeat = 20
#             # e.alarms = a
#             # c.events.add(e)
#             #
#             # c.events
#
#             with open('prescription.ics', 'w') as my_file:
#                 my_file.writelines(c)

#
# if ("DAY" in duration) | ("EVERYDAY" in duration) | ("DAILY" in duration):
#
# # If the medication is to be taken daily
# if duration.__contains__("EVERYDAY"):
#     # duration[0] should be the number of pills taken each time since duration = "# EVERYDAY"
#     # Use days_to_schedule to figure out how many events to add
#     # 30 pills @ TWICE A DAY = 15 dosages/15 events
#     days_to_schedule = quantity / int(duration[0])
#     # What time would you like to start taking the medication
#     print("Enter time 8AM as 8:00 and 8PM as 20:00 Exactly")
#     time_to_take = input("What time would you like to start taking the medication: ")
#
#     e.name = directive + " of " + medication
#     e.begin = '2020-06-26 00:00:00'  # This will be the current day as well as the medication taking time
#
#     while days_to_schedule > 1:
#         c.events.add(e)
#         # Figure out a way to add days to e.begin !!!
#         days_to_schedule -= 1
# # If the medication is to be taken hourly
#
# c.events
# # [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
# # End the event based off of how many pills are in the bottles. QTY
# # Ask for the users input on this
# with open('prescription.ics', 'w') as my_file:
#     my_file.writelines(c)
# # and it's done !


def main():
    create_log_file(text_pipeline())
    # text_pipeline() returns a tuple of the directive and duration.


if __name__ == "__main__":
    main()
