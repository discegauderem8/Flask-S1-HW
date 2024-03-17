# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def start():
    context = {"title": "Магазин одежды"}
    return render_template("base.html", **context)


@app.route('/clothes/')
def clothes():
    _items = [
        {"name": "Рубашка", "price": "7000 руб.", "picture": url_for('static', filename='img/clothes_1.jpeg')},
        {"name": "Футболка", "price": "8000 руб.", "picture": url_for('static', filename='img/clothes_2.jpg')},
        {"name": "Куртка", "price": "12000 руб.", "picture": url_for('static', filename='img/clothes_3.jpg')}
    ]
    context = {"items": _items}
    return render_template("clothes.html", **context)




@app.route('/shoes/')
def shoes():
    _items = [
        {"name": "Ботинки", "price": "7000 руб.", "picture": url_for('static', filename='img/shoes_1.jpg')},
        {"name": "Ботинки", "price": "8000 руб.", "picture": url_for('static', filename='img/shoes_2.jpeg')},
        {"name": "Кроссовки", "price": "12000 руб.", "picture": url_for('static', filename='img/shoes_3.jpeg')}
    ]
    context = {"items": _items}
    return render_template("shoes.html", **context)




@app.route('/accessories/')
def accessories():
    _items = [
        {"name": "Ожерелье", "price": "7000 руб.", "picture": url_for('static', filename='img/necklace_1.jpeg')},
        {"name": "Ожерелье", "price": "8000 руб.", "picture": url_for('static', filename='img/necklace_2.jpeg')},
        {"name": "Ожерелье", "price": "12000 руб.", "picture": url_for('static', filename='img/necklace_3.jpeg')}
    ]
    context = {"items": _items}
    return render_template("accessories.html", **context)


if __name__ == '__main__':
    app.run()
