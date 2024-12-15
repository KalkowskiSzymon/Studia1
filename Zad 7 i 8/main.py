import requests
import argparse
from typing import List


class Brewery:
    def __init__(
        self,
        id: int,
        name: str,
        brewery_type: str,
        city: str,
        state: str,
        street: str,
        postal_code: str,
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.state = state
        self.street = street
        self.postal_code = postal_code

    def __str__(self):
        return f"Brewery ID: {self.id}\nName: {self.name}\nType: {self.brewery_type}\nCity: {self.city}\nState: {self.state}\nStreet: {self.street}\nPostal Code: {self.postal_code}\n"


def fetch_breweries(city: str = "") -> List[Brewery]:
    url = "https://api.openbrewerydb.org/breweries"
    params = {"by_city": city} if city else {}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        breweries = []
        for brewery_data in data:
            brewery = Brewery(
                id=brewery_data.get("id"),
                name=brewery_data.get("name"),
                brewery_type=brewery_data.get("brewery_type"),
                city=brewery_data.get("city", "N/A"),
                state=brewery_data.get("state", "N/A"),
                street=brewery_data.get("street", "N/A"),
                postal_code=brewery_data.get("postal_code", "N/A"),
            )
            breweries.append(brewery)
        return breweries
    else:
        print("Error fetching data from API.")
        return []


def parse_arguments():
    parser = argparse.ArgumentParser(description="Fetch breweries data.")
    parser.add_argument("--city", type=str, help="City to filter breweries by")
    return parser.parse_args()


def main():
    args = parse_arguments()
    city = args.city if args.city else ""

    breweries = fetch_breweries(city)

    if breweries:
        for brewery in breweries:
            print(brewery)
    else:
        print("No breweries found.")


if __name__ == "__main__":
    main()
