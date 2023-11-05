import pandas as pd

def parse_mess_menu_excel(excel_file_path):
    """Parses an Excel spreadsheet containing the mess menu and converts its contents into a list of Meal objects.

    Args:
        excel_file_path: The path to the Excel spreadsheet.

    Returns:
        A list of Meal objects.
    """

    df = pd.read_excel(excel_file_path)

    l=[]
    a=[]
   

    for col in df.columns:
        a.append(col)
    for j in range(15):
        meals=[]

        for i, row in df.iterrows():
        
            meal = row[a[j]]
            if str(meal) in "************************":
                pass
            elif(pd.isnull(meal)):
                pass
                

               
                
            else:
                meals.append(meal)
            
        l.append(meals)
   
    w=[]
    for y in range(15):
        
    
        d=l[y][23:29][:]
        
        b=l[y][1:10][:]
        
        t=l[y][12:21][:]
       
        e={str(a[y])[0:11]:{"Breakfast":b,"Lunch":t,"Dinner":d}}
        w.append(e)
    return w
  


 
   
   
    
   
         

def main():
    excel_file_path = 'Mess Menu Sample.xlsx'

    parse_mess_menu_excel(excel_file_path)
   
   

if __name__ == '__main__':
    main()

import json

class MealEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Meal):
            return obj.__dict__
        else:
            return super().default(obj)

def serialize_meals_to_json(meals, json_file_path, encoder=MealEncoder):
    """Serializes a list of Meal objects to a JSON file using a custom JSON encoder.

    Args:
        meals: A list of Meal objects.
        json_file_path: The path to the JSON file.
        encoder: A custom JSON encoder.
    """


    l=[]
    with open(json_file_path, 'w') as f:
     
            
            
           
            
         
            
      
        
       
        json.dump(meals,f, indent=4, cls=encoder)

def main():
    excel_file_path = 'Mess Menu Sample.xlsx'
    json_file_path = 'tr.json'

    meals = parse_mess_menu_excel(excel_file_path)

    serialize_meals_to_json(meals, json_file_path)

if __name__ == '__main__':
    main()
