from django.conf import settings


class History(object):
    def __init__(self, request):
        self.session = request.session
        history = self.session.get(settings.HISTORY_SESSION_ID)
        if not history:
            # сохранение пустой корзины в сессии
            history = self.session[settings.HISTORY_SESSION_ID] = []
        self.history = history

    def add(self, city):
        # Добавить продукт в корзину или обновить его количество.

        if city not in self.history:
            self.history.insert(0, city)
        else:
            self.history.remove(city)
            self.history.insert(0, city)
        self.save()

    def save(self):
        # Обновление сессии history
        self.session[settings.HISTORY_SESSION_ID] = self.history
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, city):
        if city in self.history:
            self.history.remove(city)
            self.save()

    def __iter__(self):
        # Перебор элементов в массиве истории.
        for item in self.history:
            yield item

    def __len__(self):
        # Подсчет количества городов.
        return len(self.history)

    def clear(self):
        # удаление истории из сессии
        del self.session[settings.HISTORY_SESSION_ID]
        self.session.modified = True