'''
Created on Dec 28, 2022

@author: Jim Lakis
 
'''

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/cars")
def objMethodInput():
    
    class OurClass:
        def __init__(self, car = None):
            self._car = car
    
        @property
        def our_attribute(self):
            return self._car
        
        @our_attribute.setter
        def our_attribute(self, val):
            self._car = val
            
    car = OurClass()
    car.our_attribute = "Stingray"
    
    return render_template("car_model.html", name = car.our_attribute)

@app.route("/cars_global")
def objMethodInput2():
    return render_template("car_model.html", name = car.our_attribute)

def main():
    app.run(debug=True)

# Global Scope
if __name__ == '__main__':

    class OurClass2:
        def __init__(self, car = None):
            self._car = car
    
        @property
        def our_attribute(self):
            return self._car
        
        @our_attribute.setter
        def our_attribute(self, val: int = str):
            self._car = val
            
    car2 = OurClass2()
    car2.our_attribute = "Mustang"

    main()