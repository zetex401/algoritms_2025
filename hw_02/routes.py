import csv


def load_routes(filename: str) -> dict:
    """Возвращает {route_id: {"name": str, "stops": list}}"""
    routes = {}
    with open(filename, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            route_id = int(row["route_id"])
            route_name = row["route_name"].strip()
            stops = [s.strip() for s in row["stops"].split(",") if s.strip()]
            routes[route_id] = {
                "name": route_name,
                "stops": stops
            }
    return routes
def find_route(routes: dict, route_id: int):
    """O(1) поиск. None если не найден."""
    return routes.get(route_id)
def build_stop_index(routes: dict) -> dict:
    """Индекс: {"Алматы": [1, 2, 5], "Астана": [1, 3], ...}"""
    index = {}
    for route_id, info in routes.items():
        for stop in info["stops"]:
            index.setdefault(stop, []).append(route_id)
    return index


def find_routes_by_stop(stop_index: dict, stop_name: str) -> list:
    """O(1) поиск. Пустой список если не найдено."""
    return stop_index.get(stop_name, [])




if __name__ == "__main__":
    routes = load_routes("hw_02/routes.csv")

    print("Загружено маршрутов:", len(routes))
    print("Поиск ID=1:", find_route(routes, 1))
    print("Поиск ID=999:", find_route(routes, 999))

    stop_index = build_stop_index(routes)
    print("Маршруты через 'Алматы':", find_routes_by_stop(stop_index, "Алматы"))
    print("Маршруты через 'НЕТ_ТАКОЙ':", find_routes_by_stop(stop_index, "НЕТ_ТАКОЙ"))

