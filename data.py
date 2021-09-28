import requests


def check(url):
    try:
        data = requests.get(url)
        return data
    except (requests.ConnectionError, requests.Timeout):
        print("No internet connection")
        exit()


print('''
 ██████╗ ██╗   ██╗██╗███████╗     ██████╗ ██╗   ██╗███████╗███████╗████████╗
██╔═══██╗██║   ██║██║╚══███╔╝    ██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝
██║   ██║██║   ██║██║  ███╔╝     ██║   ██║██║   ██║█████╗  ███████╗   ██║   
██║▄▄ ██║██║   ██║██║ ███╔╝      ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   
╚██████╔╝╚██████╔╝██║███████╗    ╚██████╔╝╚██████╔╝███████╗███████║   ██║   
 ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝     ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   
 No. of questions: 10                                                                             
'''
      )

categories = check("https://opentdb.com/api_category.php")
categories = (categories.json())["trivia_categories"]
categories = {i+1: {categories[i]["id"]: categories[i]["name"]}
              for i in range(len(categories))}
print("Available Categories: ")
for i in categories:
    print(f"{'%02d'%i}: {list(categories[i].values())[0]}")
id = list(
    categories[(int(input("\nEnter Category number from above: ")))].keys())[0]
lvl = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
if lvl == "hard":
    lvl = "medium"
questions = check(
    f"https://opentdb.com/api.php?amount=10&category={id}&difficulty={lvl}&type=boolean").json()
if(questions["response_code"] != 0):
    print("Sorry no questions available.")
    exit()
questions = questions["results"]
print()
