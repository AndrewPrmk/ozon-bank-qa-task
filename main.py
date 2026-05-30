import requests

def get_highest_hero(gender, has_work):
    try:
        response = requests.get("https://akabab.github.io/superhero-api/api/all.json")
        response.raise_for_status()
        heroes = response.json()
    except Exception as e:
        print(f"Ошибка загрузки API: {e}")
        return None

    filtered_heroes = []
    for hero in heroes:
        hero_gender = hero.get('appearance', {}).get("gender")
        occupation = hero.get("work", {}).get("occupation")
        has_work_flag = occupation not in [None, "-", ""]

        if hero_gender == gender and has_work_flag == has_work:
            filtered_heroes.append(hero)

    if not filtered_heroes:
        return None

    highest_hero = max(filtered_heroes, key=get_height_in_cm)
    return highest_hero

def get_height_in_cm(hero):
    data = hero.get("appearance", {}).get("height", ["", "0 cm"])
    data_str = data[1].strip().lower()

    if data_str.endswith("cm"):
        return float(data_str.replace("cm", "").strip())
    elif data_str.endswith("meters"):
        return float(data_str.replace("meters", "").strip()) * 100
    elif data_str.endswith("m") and not data_str.endswith("cm"):
        return float(data_str.replace("m", "").strip()) * 100
    else:
        return 0.0

if __name__ == "__main__":
    hero = get_highest_hero("Male", True)
    if hero:
        print("Самый высокий герой:")
        print(f"Имя: {hero["name"]}, рост: {hero['appearance']['height'][1]}")



