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



if __name__ == "__main__":
    routes = load_routes("hw_02/routes.csv")
    print("Загружено маршрутов:", len(routes))
    print("Маршрут 1:", routes.get(1))
    print("Поиск ID=1:", find_route(routes, 1))
    print("Поиск ID=999:", find_route(routes, 999))

