from app import app


@app.route('/')
@app.route('/restaurants')
def show_restaurants():
    return 'This page will show all my restaurants'

@app.route('/restaurant/new')
def new_restaurant():
    return 'This page will be for making a new restaurant'

@app.route('/restaurant/restaurant_id/edit')
def edit_restaurant():
    return f'This page will be for editing restaurant {restaurant_id}'

@app.route('/restaurant/restaurant_id/delete')
def delete_restaurant():
    return f'This page will be for deleting restaurant {restaurant_id}'

@app.route('/restaurant/restaurant_id/menu/new')
def new_menu_item():
    return f'This page is for making a new item for restaurant {restaurant_id}'

@app.route('/restaurant/restaurant_id/menu/menu_id/edit')
def edit_menu_item():
    return f'This page will be for editing menu {menu_id}'

@app.route('/restaurant/restaurant_id/menu/menu_id/delete')
def delete_menu_item():
    return f'This page will be for deleting menu {menu_id}'