#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s Explore some US Bikeshare Data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
city = input("Please choose one of the three cities: chicago, new york city, washington:\n").lower()
while city not in ["chicago", "new york city", "washington"]:
    print("You did not type the correct name, please try it again:\n")
    city = input("Please choose one of the three cities: chicago, new york city, washington:\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
month = input("Please choose one of the following months: january, februrary, march, april, may, june, all:\n").lower()
while month not in ["january", "february", "march", "april", "may", "june", "all"]:
    print("You did not type the correct name, please try it again:\n")
    month = input("Please choose one of the following months: january, februrary, march, april, may, june, all:\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
day = input("Please choose one of the following day of week: monday, tuesday, wednesday, thursday, friday, all:\n").lower()
while day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "all"]:
    print("You did not type the correct name, please try it again:\n")
    day = input("Please choose one of the following day of week: monday, tuesday, wednesday, thursday, friday, all:\n").lower()



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
df = pd.read_csv(CITY_DATA[city])
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['month'] = df['Start Time'].dt.month
df['day_of_week'] = df['Start Time'].dt.weekday_name
if month != 'all':
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1
            df = df[df['month'] == month]
if day != 'all':
          df = df[df['day_of_week'] == day.title()]


return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()
    print("The most common month: ")
    print(popular_month)


    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day_of_week = df['day_of_week'].mode()
    print("The most common day of week: ")
    print(popular_day_of_week)



    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most common start hour: ")
    print(popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()
    print("The most commonly used start station: ")
    print(popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()
    print("The most commonly used end station: ")
    print(popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_startandend_stations = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).nlargest(1)
    print("The most commonly used start and end stations: ")
    print(popular_startandend_stations)

    print("\nTotal time: %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time: ")
    print(total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time: ")
    print(mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_types = df['User Type'].value_counts()
        print("The counts of user types: ")
        print(user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value.counts()
        print(" The counts of gender: ")
        print(gender)
    except:
        print("There is no gender information available in this city")



    # TO DO: Display earliest, most recent, and most common year of birth
    try:
            earliest_birth = min(df['Birth Year'])
            print("Earliest year of birth: ")
            print(earliest_birth)

            most_recent_birth = max(df['Birth Year'])
            print("Most recent year of birth: ")
            print(most_recent_birth)

            most_common_birth = df['Birth Year'].mode()
            print(" Most common year of birth: ")
            print(most_common_birth)

    except:
            print("There is no birth year information available in this city")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    raw_data = input(" Would you like to see some raw data? Enter yes or no.\n").lower()
    n = 0
    while raw_data == 'yes':
        print(df[n:n+5])
        n += 5
    raw_data = input(" Would you like to see some raw data? Enter yes or no.\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:
