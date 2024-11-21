from flask import Blueprint, render_template, request, redirect, url_for
from .models import Item


main = Blueprint('main', __name__)

@main.route('/')
def index():
    items = Item.get_all_items()
    return render_template('index.html', items=items)

@main.route('/add', methods=('POST',))
def add_item():
    text = request.form.get('text')
    if text:
        item = Item(text=text)
        item.add_to_db()
    return redirect(url_for('main.index'))

@main.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit_item(id):
    item = Item.find_item_by_id(int(id))
    if request.method == 'POST':
        item.text = request.form.get('text')
        item.update_db()
        return redirect(url_for('main.index'))
    return render_template('edit.html', item=item)

@main.route('/delete/<int:id>')
def delete_item(id):
    item = Item.find_item_by_id(int(id))
    item.delete_from_db()
    return redirect(url_for('main.index'))
