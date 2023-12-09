#Task 1
import requests

if __name__ == "__main__":
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url)
    data= response.json()
    joke = data['value']
    print(joke)

