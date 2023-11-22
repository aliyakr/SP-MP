from datetime import datetime
from functools import reduce

def group_and_sort_blog_posts_recursive(posts, result=None):
    # Если это первый вызов функции, инициализируем пустой результат
    if result is None:
        result = {}

    # Функция для обработки одной записи блога
    def process_post(post, acc):
        # Разбиваем запись по тегам и добавляем в аккумулятор
        return reduce(lambda a, t: {**a, t: a.get(t, []) + [post]}, post['tags'], acc)

    # Применяем функцию process_post к каждой записи блога с использованием reduce
    result = reduce(lambda acc, post: process_post(post, acc), posts, result)

    # Сортируем записи внутри групп по дате с использованием map
    result = {tag: sorted(posts, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d')) for tag, posts in result.items()}

    return result

# Пример использования
blog_posts = [
    {'title': 'Запись 1', 'date': '2023-11-15', 'tags': ['Python', 'Programming']},
    {'title': 'Запись 2', 'date': '2023-11-14', 'tags': ['Data Science', 'Python']},
    {'title': 'Запись 3', 'date': '2023-11-16', 'tags': ['Programming', 'Tips']},
    # ... другие записи блога ...
]

grouped_and_sorted_posts = group_and_sort_blog_posts_recursive(blog_posts)

# Выводим результат
for tag, posts in grouped_and_sorted_posts.items():
    print(f"Тег: {tag}")
    for post in posts:
        print(f"  Заголовок: {post['title']}, Дата: {post['date']}")