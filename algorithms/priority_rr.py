from collections import deque

from utils import compress_gantt, calculate_averages


# Priority Scheduling with Round Robin: Processes grouped by priority; each group uses round robin with time quantum
def priority_rr(processes, quantum):

    time = 0
    completed = 0
    n = len(processes)
    gantt = []

    # Loop: initialize each process
    for process in processes:
        process.remaining_time = process.burst_time
        process.waiting_time = 0
        process.turnaround_time = 0

    # Get all unique priority levels sorted
    priorities = sorted({process.priority for process in processes})
    # Create a queue for each priority level
    queues = {priority: deque() for priority in priorities}
    # Track which processes have been added to queues
    added = {priority: set() for priority in priorities}

    # Function to add ready processes to their priority queues
    def add_ready_processes():
        # Loop: check all processes for readiness
        for process in processes:
            # Condition: process arrived, has work, and not queued
            if (
                process.arrival_time <= time
                and process.remaining_time > 0
                and process.pid not in added[process.priority]
            ):
                queues[process.priority].append(process)
                added[process.priority].add(process.pid)

    add_ready_processes()

    # Loop: continue until all processes complete
    while completed < n:
        current_priority = None

        # Loop: find highest priority queue with ready processes
        for priority in priorities:
            # Condition: this priority queue has processes
            if queues[priority]:
                current_priority = priority
                break

        # Condition: no processes ready, CPU is idle
        if current_priority is None:
            gantt.append(("IDLE", time, time + 1))
            time += 1
            add_ready_processes()
            continue

        current = queues[current_priority].popleft()
        start = time
        # Determine execution time: min of quantum or remaining time
        execute = quantum if current.remaining_time >= quantum else current.remaining_time

        current.remaining_time -= execute
        time += execute
        gantt.append((current.pid, start, time))

        add_ready_processes()

        # Condition: process still has work remaining
        if current.remaining_time > 0:
            queues[current_priority].append(current)
        else:
            # Process is complete
            completed += 1
            current.turnaround_time = time - current.arrival_time
            current.waiting_time = current.turnaround_time - current.burst_time

    gantt = compress_gantt(gantt)
    avg_wt, avg_tat = calculate_averages(processes)

    return processes, gantt, avg_wt, avg_tat