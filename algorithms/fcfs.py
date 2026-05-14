from utils import compress_gantt, calculate_averages


def get_arrival(process):
    return process.arrival_time


# FCFS (First-Come, First-Served): Processes execute in the order they arrive
def fcfs(processes):

    processes.sort(key=get_arrival)

    time = 0

    gantt = []

    # Loop: process each job in arrival order
    for process in processes:

        # Condition: CPU is idle before this process arrives
        if time < process.arrival_time:

            gantt.append((
                "IDLE",
                time,
                process.arrival_time
            ))

            time = process.arrival_time

        start = time

        end = start + process.burst_time

        process.waiting_time = (
            start - process.arrival_time
        )

        process.turnaround_time = (
            end - process.arrival_time
        )

        gantt.append((
            process.pid,
            start,
            end
        ))

        time = end

    gantt = compress_gantt(gantt)

    avg_wt, avg_tat = calculate_averages(processes)

    return processes, gantt, avg_wt, avg_tat