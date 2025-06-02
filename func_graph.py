import matplotlib.pyplot as plt
from matplotlib import font_manager
import platform

if platform.system() == 'Windows':
    font_path = "c:/Windows/Fonts/malgun.ttf"
elif platform.system() == 'Darwin':
    font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
else:
    font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"

font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

def get_color(pm10):
    try:
        val = int(pm10)
        if val <= 30:
            return 'yellowgreen'
        elif val <= 80:
            return 'orange'
        elif val <= 150:
            return 'red'
        else:
            return 'black'
    except:
        return 'gray'

def plot_dust_graph(data_list, location):
    valid_data = [(station, int(pm10)) for station, pm10 in data_list if pm10.isdigit()]
    
    if not valid_data:
        print("그래프를 출력할 유효한 데이터가 없습니다.")
        return

    stations, pm10_values = zip(*valid_data)
    colors = [get_color(pm10) for pm10 in pm10_values]

    plt.figure(figsize=(14, 6))
    plt.bar(stations, pm10_values, color=colors)
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("PM10 농도 (㎍/㎥)")
    plt.title(f"{location} 지역의 측정소별 PM10 농도")
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()
