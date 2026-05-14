from process import Process
from gantt import print_gantt
from utils import print_table

from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.srt import srt
from algorithms.round_robin import round_robin
from algorithms.priority import priority_scheduling
from algorithms.priority_rr import priority_rr


# Read and validate an integer input from the user
def read_int(prompt, min_value=None, max_value=None):
    # Loop: keep asking until valid input received
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            # Catch: input was not a valid integer
            print("Invalid input. Please enter a valid integer.")
            continue
        except KeyboardInterrupt:
            # Catch: user pressed Ctrl+C
            print("\nInput cancelled.")
            raise

        # Condition: check if value is below minimum
        if min_value is not None and value < min_value:
            print(f"Value must be at least {min_value}.")
            continue
        # Condition: check if value is above maximum
        if max_value is not None and value > max_value:
            print(f"Value must be at most {max_value}.")
            continue

        # All validation passed: return the value
        return value


# Read a non-empty string input from the user
def read_nonempty_string(prompt):
    # Loop: keep asking until non-empty string received
    while True:
        try:
            text = input(prompt).strip()
        except KeyboardInterrupt:
            # Catch: user pressed Ctrl+C
            print("\nInput cancelled.")
            raise

        # Condition: string has content
        if text:
            return text
        # Else: string was empty or only whitespace
        print("Value cannot be empty.")


# Main program: Get process details from user and run selected scheduling algorithm
def main():
    processes = []

    try:
        # Get number of processes
        n = read_int("Enter number of processes (minimum 3): ", min_value=3)

        # Get details for each process
        for i in range(n):
            print(f"\nProcess {i + 1}")

            # Collect process information from user
            pid = read_nonempty_string("Process ID: ")
            arrival = read_int("Arrival Time: ", min_value=0)
            burst = read_int("Burst Time: ", min_value=1)
            priority = read_int("Priority: ")

            processes.append(Process(pid, arrival, burst, priority))

        # Display scheduling algorithm options
        print("\nCPU Scheduling Algorithms")
        print("1. FCFS")
        print("2. SJF")
        print("3. SRT")
        print("4. Round Robin")
        print("5. Priority Scheduling")
        print("6. Priority Scheduling with Round Robin")

        # Get user's algorithm choice
        choice = read_int("Choose algorithm: ", min_value=1, max_value=6)

        # Conditional: route to selected algorithm
        if choice == 1:
            # User selected FCFS
            completed, gantt, avg_wt, avg_tat = fcfs(processes)

        elif choice == 2:
            # User selected SJF
            completed, gantt, avg_wt, avg_tat = sjf(processes)

        elif choice == 3:
            # User selected SRT
            completed, gantt, avg_wt, avg_tat = srt(processes)

        elif choice == 4:
            # User selected Round Robin: get time quantum
            quantum = read_int("Enter Time Quantum: ", min_value=1)
            completed, gantt, avg_wt, avg_tat = round_robin(processes, quantum)

        elif choice == 5:
            # User selected Priority Scheduling
            completed, gantt, avg_wt, avg_tat = priority_scheduling(processes)

        else:
            # Default: choice == 6, Priority RR: get time quantum
            quantum = read_int("Enter Time Quantum: ", min_value=1)
            completed, gantt, avg_wt, avg_tat = priority_rr(processes, quantum)

    except KeyboardInterrupt:
        # Catch: user interrupted program with Ctrl+C
        print("\nProgram terminated by user.")
        return
    except Exception as exc:
        # Catch: any unexpected error occurred
        print(f"An unexpected error occurred: {exc}")
        return

    # Display results
    print_gantt(gantt)
    print_table(completed)

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()