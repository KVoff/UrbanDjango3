from django.core.paginator import Paginator
from django.shortcuts import render

from Task.models import Article


def articles_template(request):
    # Получаем все записи из модели
    articles = Article.objects.all()

    per_page = request.GET.get('per_page', 1)

    paginator = Paginator(articles, per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'per_page': per_page

    }

    return render(request, 'articles.html', context)







# # Создание статей с использованием object.create
# Article.objects.create(title='Четвертая статья',
#                        content='Это четвертая статья.',
#                        author='admin',
#                        created_at='2024-11-17')
# Article.objects.create(title='Пятая статья',
#                        content='Это пятая статья.',
#                        author='admin',
#                        created_at='2024-11-15')
# Article.objects.create(title='Шестая статья',
#                        content='Это шестая статья.',
#                        author='user',
#                        created_at='2024-11-16')


# # Получение объекта и изменение заголовка
# post = Article.objects.get(id=1)
# post.title = 'Меняем заголовок'
# post.save()

# # Получение всех объектов
# all_articles = Article.objects.all()
# for article in all_articles:
#     print(article.title, article.author)


# # Удаление объекта с id=2
# article_to_delete = Article.objects.get(id=2)
# article_to_delete.delete()

# # Фильтрация статей, созданных пользователем user
# user_articles = Article.objects.filter(author='user')
# print(user_articles)
# #
# # # Фильтрация статей, опубликованных в 2024 году
# articles_2024 = Article.objects.filter(created_at__year=2024)
# print(articles_2024)
