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


if __name__ == "__main__":
    routes = load_routes("routes.csv")
    print("Загружено маршрутов:", len(routes))
    print("Маршрут 1:", routes.get(1))
