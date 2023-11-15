from datetime import datetime

def group_and_sort_blog_posts(posts):
    # Создаем словарь для хранения записей по тегам
    grouped_posts = {}

    # Проходимся по каждой записи блога
    for post in posts:
        # Проходимся по каждому тегу в записи
        for tag in post['tags']:
            # Если тега еще нет в словаре, добавляем его
            if tag not in grouped_posts:
                grouped_posts[tag] = []

            # Добавляем запись в соответствующую группу (по тегу)
            grouped_posts[tag].append(post)

    # Сортируем записи внутри каждой группы по дате
    for tag, posts in grouped_posts.items():
        grouped_posts[tag] = sorted(posts, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'))

    return grouped_posts

# Пример использования
blog_posts = [
    {'title': 'Запись 1', 'date': '2023-11-15', 'tags': ['Python', 'Programming']},
    {'title': 'Запись 2', 'date': '2023-11-14', 'tags': ['Data Science', 'Python']},
    {'title': 'Запись 3', 'date': '2023-11-16', 'tags': ['Programming', 'Tips']},
    # ... другие записи блога ...
]

grouped_and_sorted_posts = group_and_sort_blog_posts(blog_posts)

# Выводим результат
for tag, posts in grouped_and_sorted_posts.items():
    print(f"Тег: {tag}")
    for post in posts:
        print(f"  Заголовок: {post['title']}, Дата: {post['date']}")
