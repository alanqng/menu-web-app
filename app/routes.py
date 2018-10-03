from app import app


@app.route('/')
@app.route('/restaurants')
def show_restaurants():
    return render_template('restaurants.html')

@app.route('/restaurant/new')
def new_restaurant():
    return render_template('newRestaurant.html')

@app.route('/restaurant/restaurant_id/edit')
def edit_restaurant():
    return render_template('editRestaurant.html')

@app.route('/restaurant/restaurant_id/delete')
def delete_restaurant():
    return render_template('deleteRestaurant.html')

@app.route('/restaurant/restaurant_id')
@app.route('/restaurant/restaurant_id/menu')
def show_menu():
    return render_template('menu.html')

@app.route('/restaurant/restaurant_id/menu/new')
def new_menu_item():
    return render_template('newMenu.html')

@app.route('/restaurant/restaurant_id/menu/menu_id/edit')
def edit_menu_item():
    return render_template('editMenu.html')

@app.route('/restaurant/restaurant_id/menu/menu_id/delete')
def delete_menu_item():
    return render_template('deleteMenu.html')




    #Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}