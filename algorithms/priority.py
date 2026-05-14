from utils import compress_gantt, calculate_averages


def get_priority(process):
    return process.priority


# Priority Scheduling: Process with the highest priority (lowest number) executes first
def priority_scheduling(processes):

    time = 0

    completed = 0

    n = len(processes)

    gantt = []

    finished = []

    # Loop: continue until all processes complete
    while completed < n:

        ready = []

        # Loop: find all ready processes
        for process in processes:

            # Condition: process has arrived and is not finished
            if (
                process.arrival_time <= time
                and process not in finished
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

        # Select process with highest priority (minimum priority number)
        current = min(
            ready,
            key=get_priority
        )

        start = time

        end = time + current.burst_time

        current.waiting_time = (
            start - current.arrival_time
        )

        current.turnaround_time = (
            end - current.arrival_time
        )

        gantt.append((
            current.pid,
            start,
            end
        ))

        time = end

        finished.append(current)

        completed += 1

    gantt = compress_gantt(gantt)

    avg_wt, avg_tat = calculate_averages(processes)

    return processes, gantt, avg_wt, avg_tat