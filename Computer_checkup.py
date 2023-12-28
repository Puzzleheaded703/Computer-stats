import psutil

def get_process_info():
    processes = []
    for process in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent']):
        processes.append({
            'pid': process.info['pid'],
            'name': process.info['name'],
            'status': process.info['status'],
            'cpu_percent': process.info['cpu_percent']
        })
    return processes

if __name__ == "__main__":
    running_processes = get_process_info()

    print("Running Processes:")
    for process in running_processes:
        print(f"PID: {process['pid']}, Name: {process['name']}, Status: {process['status']}, cpu_process: {process['cpu_percent']}")
