CPU Scheduling 
=======================

This project is a CPU scheduling simulator for operating system process scheduling algorithms.
It lets you define a set of processes and run several scheduling strategies to compare Gantt charts,
average waiting time, and average turnaround time.

Supported algorithms
--------------------
- First-Come, First-Served (FCFS)
- Shortest Job First (SJF)
- Shortest Remaining Time (SRT)
- Round Robin (RR)
- Priority Scheduling
- Priority Scheduling with Round Robin

Files
-----
- **CabreraJacobStephenBSCS3B.exe** - main executable file for the program
- main.py - entry point for the application and user input flow
- process.py - Process class definition
- utils.py - helper functions for printing tables, computing averages, and compressing Gantt data
- gantt.py - prints the Gantt chart to the console
- algorithms/ - scheduling algorithm implementations
  - fcfs.py
  - sjf.py
  - srt.py
  - round_robin.py
  - priority.py
  - priority_rr.py

**How to run**
----------
1. Install the **CabreraJacobStephenBSCS3B.exe** file
2. Run the **CabreraJacobStephenBSCS3B.exe** to start the program
3. Enter the number of processes, then provide each process's:
   - Process ID
   - Arrival time
   - Burst time (This will not accept 0 as a value)
   - Priority
4. Choose a scheduling algorithm from the menu by inputting the number of the desired algorithm (1.FCFS -- input "1" and press Enter to proceed with FCFS).
5. If Round Robin or Priority Round Robin is selected, enter a time quantum.
6. Review the displayed Gantt chart and statistics.
7. Press Enter to exit the program

Notes
-----
- The project assumes a Python environment with at least Python 3.
- The app handles idle CPU time when no process is ready to run.
- Process arrival order may affect results for algorithms with ties.
- Error handling is available for incorrect data type inputs
