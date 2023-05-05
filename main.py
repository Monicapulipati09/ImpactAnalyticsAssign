
# In a university, your attendance determines whether you will be
# allowed to attend your graduation ceremony.
# You are not allowed to miss classes for four or more consecutive days.
# Your graduation ceremony is on the last day of the academic year,
# which is the Nth day.
#
#   Your task is to determine the following:
#
# 1. The number of ways to attend classes over N days.
# 2. The probability that you will miss your graduation ceremony.
#
# Represent the solution in the string format as "Answer of (2) / Answer
# of (1)", don't actually divide or reduce the fraction to decimal


def find_probability(number_of_missing_days, current_day, number_of_days_till_now, ways_to_attend, prob_of_miss, total_number_of_days):
    """

    :param number_of_missing_days: number of consecutive missing days, if present on a day, number of missig days will become 0
    :param current_day: value will be '0' or '1' 0 - Absent, 1 - Present
    :param number_of_days_till_now: Number of days completed till now.
    :return:ways_to_attend  - total ways to attend , prob_of_miss - number of ways to miss grad day.
    """

    if number_of_missing_days >= 4:
        return prob_of_miss, ways_to_attend

    if number_of_days_till_now == total_number_of_days:
        ways_to_attend += 1
        if current_day == '0':
            prob_of_miss += 1
        return prob_of_miss, ways_to_attend

    prob_of_miss, ways_to_attend = find_probability(number_of_missing_days+1, '0', number_of_days_till_now+1, ways_to_attend, prob_of_miss, total_number_of_days)
    prob_of_miss, ways_to_attend = find_probability(0, '1', number_of_days_till_now+1, ways_to_attend, prob_of_miss, total_number_of_days)

    return prob_of_miss, ways_to_attend

N = 5
p, s = find_probability(0,'0',0, 0, 0, N)
print(str(p)+ "/" +str(s))