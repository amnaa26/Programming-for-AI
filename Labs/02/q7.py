'''
 Programmer: Amna(23k-0066)
 Date: 28/Aug/2024
 Q7) You have a list of daily temperatures recorded over a month. Write code to:
    • Calculate and print the average temperature for the month.
    • Find and print the highest and lowest temperatures.
    • Sort the temperatures in ascending order.
    • Remove the temperature record for a specific day
'''

def process_temperatures(temperatures, day_to_remove=None):
    if not temperatures:
        print("No temperature data available.")
        return

    # Calculate and print the average temperature
    average_temp = sum(temperatures) / len(temperatures)
    print(f"Average temperature for the month: {average_temp:.2f}°C")

    # Find and print the highest and lowest temperatures
    highest_temp = max(temperatures)
    lowest_temp = min(temperatures)
    print(f"Highest temperature: {highest_temp}°C")
    print(f"Lowest temperature: {lowest_temp}°C")

    # Sort the temperatures in ascending order
    sorted_temperatures = sorted(temperatures)
    print(f"Temperatures in ascending order: {sorted_temperatures}")

    # Remove the temperature record for a specific day
    if day_to_remove is not None and 0 <= day_to_remove < len(temperatures):
        removed_temp = temperatures.pop(day_to_remove)
        print(f"Temperature record for day {day_to_remove + 1} removed: {removed_temp}°C")
        # Recompute the average, highest, lowest, and sorted list after removal
        average_temp = sum(temperatures) / len(temperatures) if temperatures else 0
        highest_temp = max(temperatures) if temperatures else "N/A"
        lowest_temp = min(temperatures) if temperatures else "N/A"
        sorted_temperatures = sorted(temperatures)

        print(f"Updated average temperature for the month: {average_temp:.2f}°C")
        print(f"Updated highest temperature: {highest_temp}°C")
        print(f"Updated lowest temperature: {lowest_temp}°C")
        print(f"Updated temperatures in ascending order: {sorted_temperatures}")
    else:
        print("No temperature record was removed as the value of day to remove doesnot exist in the list.")



daily_temperatures = [22.5, 24.0, 19.5, 23.5, 25.0, 20.0, 21.5, 26.0, 22.0, 21.0, 20.5, 23.0]

day_to_remove = 5
process_temperatures(daily_temperatures, day_to_remove)

print("\n\n\n")
day_to_remove = 25
process_temperatures(daily_temperatures, day_to_remove)