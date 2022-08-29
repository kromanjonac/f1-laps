import urllib.request, json
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import sys


def update_ticks(x, pos):
    a = x // 60
    b = x - a * 60
    return str(int(a)) + ":" + str(round(b,3))

def convert(s):
    s = s.split(":")
    return int(s[0]) * 60 + float(s[1])

def get_laps(driver, season, race):
    driver_lap_url = "http://ergast.com/api/f1/" + season + "/" + race + "/drivers/" + driver + "/laps.json?limit=150"

    with urllib.request.urlopen(driver_lap_url) as result:
        data = json.load(result)['MRData']['RaceTable']['Races'][0]['Laps']

        ret = []

        for i in data:
            ret.append(convert(i["Timings"][0]["time"]))

        return ret

def plot_driver_vs_driver(driver1, driver2, season, race):
    laps1 = get_laps(driver1, season, race)
    laps2 = get_laps(driver2, season, race)
    laps_all = []
    laps_all.extend(laps1)
    laps_all.extend(laps2)
    min_laps = min(laps_all)
    ymin = min_laps * 0.95
    mean_lap = sum(laps_all) / len(laps_all)
    ymax = mean_lap * 1.2
    
    fig, ax = plt.subplots()
    ax.plot(laps1, label = driver1, marker = "o")
    ax.plot(laps2, label = driver2, marker = "o")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(update_ticks))
    plt.ylim(ymin, ymax)
    plt.ylabel('lap times')
    plt.xlabel('laps')
    plt.legend(loc="upper right")
    fig.set_size_inches(15, 9)
    plt.savefig(driver1 + '_vs_' + driver2 + '_' + season + '_' + race + '.png', dpi = 600)
    plt.show()

def plot_lap_diff(driver1, driver2, season, race):
    laps1 = get_laps(driver1, season, race)
    laps2 = get_laps(driver2, season, race)
    diff = []

    for i in range(len(laps1)):
        if i < len(laps2):
            diff.append(laps1[i] - laps2[i])
        else:
            break
    fig, ax = plt.subplots()    
    ax.plot(diff)
    plt.ylabel('lap difference from ' + driver1 + 'vs ' + driver2)
    plt.xlabel('laps')
    fig.set_size_inches(15, 9)
    plt.savefig(driver1 + '_diff_' + driver2 + '_' + season + '_' + race + '.png', dpi = 600)
    plt.show()



if sys.argv[1] == 'vs':
    plot_driver_vs_driver(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

elif sys.argv[1] == 'diff':
    plot_lap_diff(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    
    
            

    
            

    
    
            
