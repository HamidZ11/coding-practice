data = {
    "page": 1,
    "total_pages": 3,
    "data": [
        {"name": "A", "rating": 8.2},
        {"name": "B", "rating": 7.9}
    ]
}

for movie in data["data"]:
    print(movie["name"])



for record in data["data"]:
    if record["rating"] > 8:
        print(record["rating"])