class User:
    
    def __init__ (self,username,email,password):
        self.username =username
        self.email =email
        self.password =password
        self.recipe_categories =[]

    def add_recipe_category(self,recipe_category):
        if recipe_category not in self.recipe_categories:
            self.recipe_categories.append(recipe_category)
            return "recipe category is added succesfully"
        return "recipe category already exists"

    def edit_recipe_category(self,newname,oldname):
        if oldname in self.recipe_categories:
            self.recipe_category =[newname for oldname  in self.recipe_categories]
            return "recipe_category edited succesfully"
        return "recipe_category not found"

    def delete_recipe_category(self,recipe_category):
        if recipe_category in self.recipe_categories:
            self.recipe_categories.remove(recipe_category)
            return "recipe_category deleted"
        return "recipe_category not found"

    def view_recipe_category(self,item):
        for item in self.recipe_categories:
            return self.recipe_categories
        return "recipe_categories is empty"

class Recipe_category:
    
    def __init__(self,title):
        self.title = title
        self.recipes =[]

    def add_recipe(self, recipe):
        if recipe not in self.recipes:
            self.recipes.append(recipe)
            return "recipe added succesfully"
        return "recipe already exists"

    def edit_recipe(self,newrecipe,oldrecipe):
        if oldrecipe in self.recipes:
            self.recipes= [newrecipe for oldrecipe in self.recipes]
            return "recipe added successfully"
        return "no recipe to edit"
    
    def delete_recipe(self,recipe):
        if recipe in self.recipes:
            self.recipes.remove(recipe)
            return "recipe deleted"
        return "No recipe to delete"

    def view_recipe(self,recipe):
        for recipe in self.recipes:
            return self.recipes
        return "no recipe found"

class Recipe:

    def __init__(self, recipe):
        self.recipe = recipe
    

class repository(object):
    
    def __init__(self):
        self.users = {}
        self.recipe_categories ={}

    def commit_user(self,user):
        self.users[user.username] = user 

    def get_user(self,username):

        return  self.users[username]  

    def get_all_users(self):
        
        return self.users

    def commit_recipe_category(self,user):
        self.user[user.username] = user 

    def get_recipe_category(self,username):

        return  self.users[username]  

    def get_all_recipe_categories(self):
        
        recipe_category=[v for v in self.recipe_categories.itervalues()]
        
        return recipe_category




