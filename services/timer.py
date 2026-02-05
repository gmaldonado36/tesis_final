import time

def start_timer():
    return time.time()

def stop_timer(start):
    return round(time.time() - start, 3)
