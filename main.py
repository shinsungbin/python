from func_get_data import get_pm_data
from func_user_input import get_user_input
from func_advice import get_advice
from func_save import save_result
from func_graph import plot_dust_graph

api_key = 'B1IPLPYPSQ0pn7RP1pD9lTlDPOs2pt09FRJqoABGxySSDcD89WnEka3Kop4tQbCvq3svujM7lero1hNeaBezbg=='

def main():
    location, detail_location = get_user_input()
    data_list = get_pm_data(location, api_key)

    for station, pm10 in data_list:
        if detail_location in station:
            advice = get_advice(pm10)
            print(f"[{station}] PM10: {pm10}  ➝  {advice}")
            save_result(location, station, pm10, advice)

    show_graph = input("그래프로 확인하시겠습니까? (Y/N): ").strip().upper()
    if show_graph == 'Y':
        plot_dust_graph(data_list, location)

if __name__ == "__main__":
    main()
