import requests
from bs4 import BeautifulSoup
def fetch_links(url, tag, parameter):
    # Отправляем GET-запрос к сайту
    response = requests.get(url)
    # Проверяем, успешен ли запрос
    if response.status_code == 200:
        # Декодируем контент в UTF-8
        response.encoding = 'utf-8'
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        # Находим все теги по указанному тегу
        tags = soup.find_all(tag)
        # Извлекаем ссылки из найденных тегов с определенным параметром
        links = [a['href'] for a in tags if a.name == 'a' and 'href' in a.attrs and parameter in a['href']]
        return links
    else:
        print(f'Ошибка {response.status_code}: Не удалось получить данные с сайта.')
        return []
def save_links_to_file(links, filename):
    # Открываем файл для записи
    with open(filename, 'w', encoding='utf-8') as file:
        for link in links:
            file.write(link + '\n')
    print(f'Ссылки успешно сохранены в {filename}')
def main():
    url = 'https://primgazeta.ru/news/'  # Укажите свой URL
    tag = 'a'  # Укажите тег, по которому хотите искать
    links = fetch_links(url, tag)
    if links:
        save_links_to_file(links, 'links.txt')
if __name__ == '__main__':
    main()

