# Calculate average waiting time and turnaround time for all processes
def calculate_averages(processes):
    # Guard clause: exit early if no processes
    if not processes:
        return 0.0, 0.0

    # Loop through all processes to sum waiting times
    avg_wt = sum(p.waiting_time for p in processes) / len(processes)
    avg_tat = sum(p.turnaround_time for p in processes) / len(processes)

    return avg_wt, avg_tat


# Print a table showing process details: PID, Arrival Time, Burst Time, Priority, Waiting Time, Turnaround Time
def print_table(processes):
    print("\nPID\tAT\tBT\tPR\tWT\tTAT")

    # Loop: iterate through each process and print its details
    for p in processes:
        print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.priority}\t{p.waiting_time}\t{p.turnaround_time}")

# Combine consecutive entries in the Gantt chart if they belong to the same process
def compress_gantt(gantt):

    # Guard: return empty list if no gantt data
    if len(gantt) == 0:
        return []

    compressed = []

    current = gantt[0]

    # Loop: check each item after the first to see if it merges with current
    for i in range(1, len(gantt)):

        next_item = gantt[i]

        # Condition: same process AND next starts when current ends (mergeable)
        if current[0] == next_item[0] and current[2] == next_item[1]:

            # Merge: extend current to next item's end time
            current = (
                current[0],
                current[1],
                next_item[2]
            )

        else:
            # No merge: save current and move to next
            compressed.append(current)

            current = next_item

    compressed.append(current)

    return compressed