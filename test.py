import psutil
import psutil
import pychrome


def get_background_processes():
    background_processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username', 'status']):
        if proc.info['status'] == psutil.STATUS_RUNNING:
            background_processes.append(proc.info)
    return background_processes

def get_chrome_url(pid):
    # Check if the process with the given PID is Google Chrome
    process = psutil.Process(pid)
    if process.name().lower() != 'chrome.exe':
        return None

    # Connect to the Google Chrome browser using pychrome
    browser = pychrome.Browser()
    try:
        browser.connect()

        # Get all available tabs
        tabs = browser.list_tab()
        for tab in tabs:
            if tab.get('pid') == pid and 'url' in tab:
                return tab['url']

    finally:
        browser.close_tab()

    return None 

def get_urls(pids):
    for pid in pids:
        url = get_chrome_url(pid)
        if url:
            print(f"Process ID {pid} is running URL: {url}")
        else:
            print(f"Process ID {pid} is not a Google Chrome process or does not have an active URL.")

if __name__ == "__main__":
    background_processes = get_background_processes()
    pids = []
    for process in background_processes:
        print(f"PID: {process['pid']}, Name: {process['name']}")
        pids.append(process['pid'])

    print(pids)
    print(len(pids))

    get_urls(pids)


        
