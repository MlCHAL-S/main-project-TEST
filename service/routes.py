from flask import render_template, request, redirect, url_for
from . import app
from service.models import Item

@app.route('/')
def index():
    items = Item.get_all_accounts()
    return render_template('index.html', items=items)

@app.route('/add', methods=('POST',))
def add_item():
    text = request.form.get('text')
    if text:
        item = Item(text=text)
        item.add_to_db()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit_item(id):
    item = Item.find_account_by_id(int(id))
    if request.method == 'POST':
        item.text = request.form.get('text')
        item.update_db()
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

@app.route('/delete/<int:id>')
def delete_item(id):
    item = Item.find_account_by_id(int(id))
    item.delete_from_db()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
