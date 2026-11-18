
import requests

url = "https://api.github.com/search/repositories"

topic = input("Enter a topic to search: ")
print("1. Most Starred Projects")
print("2. Most Forked Projects")

choice = input("Choose an option (1 or 2): ")

if choice == "1":
    sort_option = "stars"
elif choice == "2":
    sort_option = "forks"
else:
    sort_option = "stars"
params = {
    "q": topic,
    "sort": sort_option,
    "per_page": 5
}

response = requests.get(url, params=params)

print("Status Code:", response.status_code)

if response.status_code == 200:

    data = response.json()

    if len(data["items"]) == 0:
        print("No projects found!")

    else:
        for repo in data["items"]:
            print("Project:", repo["name"])
            print("Description:", repo["description"])
            print("Stars:", repo["stargazers_count"])
            print("Link:", repo["html_url"])
            print("-" * 40)

else:
    print("Something went wrong! Try again.")

input("Press Enter to exit...")
