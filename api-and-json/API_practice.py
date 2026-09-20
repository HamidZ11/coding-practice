response = requests.get(url, params=params)   # send GET request
data = response.json()                        # turn JSON into Python data

for record in data["data"]:
    print(record["name"])                     # process records from this response


for page in range(1, data["total_pages"] + 1):   # loop through every page
    params = {"page": page}                      # set current page
    response = requests.get(url, params=params)  # request that page
    page_data = response.json()                  # parse that page's JSON

all_records = []

for record in page_data["data"]:
    all_records.append(record)                # add records from page_data