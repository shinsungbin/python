def get_advice(pm10_value):
    try:
        pm10 = int(pm10_value)
        if pm10 <= 30:
            return "좋음 😄 - 야외 활동 적합"
        elif pm10 <= 80:
            return "보통 🙂 - 마스크 착용 권장"
        elif pm10 <= 150:
            return "나쁨 😷 - 외출 자제"
        else:
            return "매우 나쁨 ⚠️ - 실내 활동 권장"
    except:
        return "데이터 오류 - 미세먼지 값을 확인할 수 없음"
