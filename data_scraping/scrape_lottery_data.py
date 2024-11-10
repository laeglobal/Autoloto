import requests
from bs4 import BeautifulSoup
import csv

def scrape_ny_lottery():
    url = 'https://nylottery.ny.gov/'  # Página de la lotería de NY
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Este ejemplo necesita ajustes según la estructura HTML de la página de resultados
    results = []
    for game_section in soup.find_all('div', class_='game-result'):  # Ajustar la clase según la página real
        date = game_section.find('span', class_='result-date').text  # Ajustar la clase según la página real
        numbers = game_section.find('span', class_='winning-numbers').text  # Ajustar la clase según la página real
        results.append([date, numbers])

    # Guardar los resultados en un archivo CSV
    with open('data/ny_lottery_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Numbers'])
        writer.writerows(results)

if __name__ == '__main__':
    scrape_ny_lottery()
