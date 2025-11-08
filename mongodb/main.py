from pymongo import MongoClient


def main():
    print("Hello from mongodb!")
    client = MongoClient()
    db = client.rptutorials

    tutorial1 = {
        "title": "Working With JSON Data in Python",
        "author": "Lucas",
        "contributors": ["Aldren", "Dan", "Joanna"],
        "url": "https://realpython.com/python-json/",
    }


if __name__ == "__main__":
    main()
