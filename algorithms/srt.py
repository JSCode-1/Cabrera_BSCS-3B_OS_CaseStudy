from utils import compress_gantt, calculate_averages


def get_shortest_remaining(process):
    return process.remaining_time


# SRT (Shortest Remaining Time): Process with shortest remaining time executes first (preemptive)
def srt(processes):

    time = 0

    completed = 0

    n = len(processes)

    gantt = []

    # Loop: initialize remaining time for each process
    for process in processes:
        process.remaining_time = process.burst_time

    # Loop: continue until all processes finish
    while completed < n:

        ready = []

        # Loop: find all processes ready to run
        for process in processes:

            # Condition: process arrived and still has work
            if (
                process.arrival_time <= time
                and process.remaining_time > 0
            ):

                ready.append(process)

        # Condition: no process ready, CPU is idle
        if len(ready) == 0:

            gantt.append((
                "IDLE",
                time,
                time + 1
            ))

            time += 1

            continue

        # Select process with shortest remaining time
        current = min(
            ready,
            key=get_shortest_remaining
        )

        start = time

        current.remaining_time -= 1

        time += 1

        gantt.append((
            current.pid,
            start,
            time
        ))

        # Condition: process is now complete
        if current.remaining_time == 0:

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