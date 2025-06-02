def get_user_input():
    location = input("지역을 입력하세요 (예: 서울, 경기, 부산 등): ").strip()
    detail_location = input("세부 지역을 입력하세요 (예: 서대문구, 종로구 등): ").strip()
    return location, detail_location

