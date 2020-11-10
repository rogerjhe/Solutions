import requests

def main():
    while True:
        keyword = input("What is your keyword? \nType 'quit' to exit\n")
        if keyword == "quit":
            break
        response = requests.get('https://api.publicapis.org/entries')
        array = response.json()['entries']
        url_list = []
        checks = ['API', 'Description', 'Category']
        for entry in range(len(array)):
            individual = array[entry]
            for i in checks:
                if keyword.lower() in str(individual[i]).lower():
                    url_list.append(individual['Link'])
                    continue
        for url in range(len(url_list)):
            print(url_list[url])
    return

if __name__ == '__main__':
    main()

