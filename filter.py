import requests


def check_link(url):
    try:
        # Отправляем HEAD-запрос для проверки работоспособности ссылки
        response = requests.head(url, allow_redirects=True)
        # Проверяем, успешен ли запрос (статус код 200-399)
        return response.status_code >= 200 and response.status_code < 400
    except requests.RequestException:
        return False


def filter_working_links(input_file, output_file):
    working_links = []
    # Читаем ссылки из файла
    with open(input_file, 'r', encoding='utf-8') as file:
        links = file.readlines()

    # Проверяем каждую ссылку
    for link in links:
        link = link.strip()  # Удаляем пробелы и символы новой строки
        if check_link(link):
            working_links.append(link)
            print(f'Ссылка работает:{link}')
        else:
            print(f'Ссылка не работает: {link}')

    # Сохраняем только рабочие ссылки в новый файл
    with open(output_file, 'w', encoding='utf-8') as file:
        for link in working_links:
            file.write(link + '\n')
    print(f'Рабочие ссылки успешно сохранены в {output_file}')


def main():
    input_file = 'links.txt'  # Имя входного файла с ссылками
    output_file = 'working_links.txt'  # Имя выходного файла для рабочих ссылок
    filter_working_links(input_file, output_file)


if __name__ == '__main__':
    main()