from flask import Blueprint, render_template, request, redirect, url_for
from .models import Item
from .extensions import redis_client
import json


main = Blueprint('main', __name__)

@main.route('/')
def index():
    items = redis_client.get('items_list')
    if items is None:
        items = [item.to_dict() for item in Item.get_all_items()]
        redis_client.set('items_list', json.dumps(items), ex=60)
    else:
        items = json.loads(items)
    return render_template('index.html', items=items)

@main.route('/add', methods=('POST',))
def add_item():
    text = request.form.get('text')
    if text:
        item = Item(text=text)
        item.add_to_db()
        redis_client.delete('items_list')
    return redirect(url_for('main.index'))

@main.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit_item(id):
    item = Item.find_item_by_id(int(id))
    if request.method == 'POST':
        item.text = request.form.get('text')
        item.update_db()

        items = redis_client.get('items_list')
        if items:
            items = json.loads(items)
            for cached_item in items:
                if cached_item['id'] == id:
                    cached_item['text'] = item.text
                    break
            redis_client.set('items_list', json.dumps(items), ex=60)
        return redirect(url_for('main.index'))
    return render_template('edit.html', item=item)

@main.route('/delete/<int:id>')
def delete_item(id):
    item = Item.find_item_by_id(int(id))
    item.delete_from_db()
    redis_client.delete('items_list')
    return redirect(url_for('main.index'))
