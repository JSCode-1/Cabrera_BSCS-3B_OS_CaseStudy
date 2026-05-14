# Print a visual Gantt chart showing process execution timeline
def print_gantt(gantt):

    # Guard: no data to display
    if not gantt:
        print("No Gantt data available.")
        return

    print("\nGantt Chart:")

    # Loop 1: print process names across the top row
    for item in gantt:
        print(f"| {item[0]} ", end="")

    print("|")

    # Print first time value
    print(gantt[0][1], end="")

    # Loop 2: print end times for each item along bottom
    for item in gantt:
        print(f"    {item[2]}", end="")

    print()