from collections import deque

from utils import compress_gantt, calculate_averages


# Round Robin (RR): Each process gets a fixed time slice (quantum); unfinished processes go to the back of the queue
def round_robin(processes, quantum):

    time = 0

    completed = 0

    n = len(processes)

    gantt = []

    queue = deque()

    added = []

    # Loop: initialize remaining time for each process
    for process in processes:
        process.remaining_time = process.burst_time

    # Loop: continue until all processes complete
    while completed < n:

        # ADD ARRIVED PROCESSES - Loop: check for new arrivals
        for process in processes:

            # Condition: process arrived and not yet added to queue
            if (
                process.arrival_time <= time
                and process not in added
            ):

                queue.append(process)

                added.append(process)

        # Condition: queue is empty, CPU is idle
        if len(queue) == 0:

            gantt.append((
                "IDLE",
                time,
                time + 1
            ))

            time += 1

            continue

        current = queue.popleft()

        start = time

        execute = quantum

        # Condition: remaining time is less than quantum
        if current.remaining_time < quantum:
            execute = current.remaining_time

        current.remaining_time -= execute

        time += execute

        gantt.append((
            current.pid,
            start,
            time
        ))

        # CHECK NEW ARRIVALS - Loop: check for arrivals during execution
        for process in processes:

            # Condition: process arrived and not yet added
            if (
                process.arrival_time <= time
                and process not in added
            ):

                queue.append(process)

                added.append(process)

        # Condition: process still needs CPU time
        if current.remaining_time > 0:

            queue.append(current)

        else:
            # Process is complete

            completed += 1

            current.turnaround_time = (
                time - current.arrival_time
            )

            current.waiting_time = (
                current.turnaround_time
                - current.burst_time
            )

    gantt = compress_gantt(gantt)

    avg_wt, avg_tat = calculate_averages(processes)

    return processes, gantt, avg_wt, avg_tat