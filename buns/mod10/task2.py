import requests
import re


def get_subheadings(url):
    response = requests.get(url)

    # Используем регулярное выражение для поиска подзаголовков
    pattern = re.compile(r'<h3.*?>(.*?)<\/h3>', re.DOTALL)
    matches = pattern.findall(response.text)

    # Очищаем найденные подзаголовки от HTML-тегов
    subheadings = [re.sub(r'<.*?>', '', match).strip() for match in matches]

    return subheadings


if True:
    # Если нужно протестировать на другом сайте, то измените этот параметр
    url_of_web_page = "http://www.columbia.edu/~fdc/sample.html"

    subheadings_of_web_page = get_subheadings(url_of_web_page)
    print(subheadings_of_web_page)
