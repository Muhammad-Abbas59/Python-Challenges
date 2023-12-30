from datetime import datetime

def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    time1 = datetime.strptime(t1, fmt)
    time2 = datetime.strptime(t2, fmt)
    delta_seconds = abs(int((time1 - time2).total_seconds()))
    return delta_seconds

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)