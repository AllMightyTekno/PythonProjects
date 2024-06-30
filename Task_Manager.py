import time 
import psutil 

def get_running_processes():
       processes = [] #Creates a list to store the processes
       for proc in psutil.process_iter(['pid', 'name', 'username']):
            processes.append({
            'pid': proc.info['pid'],
            'name': proc.info['name'],
            'username': proc.info['username'],
        })
       return processes

def display_running_processes():
    while True:

        print("Currently Running Processes:")

        running_processes = get_running_processes()
        for processes in running_processes:
                print(f"PID: {processes['pid']}, Application: {processes['name']}, User: {processes['username']}")

            #Update data
                time.sleep(1)

def main():
 display_running_processes()

if __name__ == "__main__":
    main()
    