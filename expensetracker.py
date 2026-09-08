# #python expense_cli.py add "Lunch" 20
# python expense_cli.py add "Coffee" 5
# python expense_cli.py list
# python expense_cli.py summary
# python expense_cli.py update 1 "Lunch with client" 25
# python expense_cli.py list
# python expense_cli.py delete 2
# python expense_cli.py list

import os
import sys
import json
from datetime import datetime



FICHIER='dépenses.json'

def load_depenses():
    if not os.path.exists(FICHIER):
        return []
    with open(FICHIER, 'r') as file:
        return json.load(file)

    
def save_depenses(depenses):
    if not os.path.exists(FICHIER):
        return []
    with open(FICHIER,'w') as file:
            
            return json.dump(depenses, file, indent=2)


def get_next_id(depenses):
    if not depenses:
        return 1
    return max(depense['id'] for depense in depenses) + 1

def find_depense_id(depenses, depense_id):
    # [{"id": 1,...}, {"id": 2,...}]
    for d in depenses:
        if d['id'] == depense_id:
            return d
    return None

def main():

# python expense_cli.py update 1 "Lunch with client" 25
# python expense_cli.py list

    args= sys.argv[1:]# [ ADD, "COFEE", 5]  OR [ LIST] OR [DELETE ,1] NO SCRIPT NAME

    if len(args)==0:
        print("No command provided. Available commands: add, list, summary, update, delete")
        return

    command=args[0] # ADD, LIST, SUMMARY, UPDATE, DELETE

    if command=="add":
        #python expense_cli.py add "Coffee" 5##########
        #######Expense added successfully (ID: 1)#########

        try:
            description=args[1]
            prix=float(args[2])
        except (IndexError, ValueError):
            print("Error: Invalid arguments for 'add' command.")
            return

        depenses=load_depenses()
        next_id=get_next_id(depenses)
        nouv_depense={
            "id": next_id,
            "description": description,
            "prix": prix,
        }
        
        depenses.append(nouv_depense)
        save_depenses(depenses)
        print(f"Expense added successefully (ID: {next_id})")

        #python expense_cli.py list
        #####1: Lunch - $20.0
        #####2: Coffee - $5.0
    elif command=="list":
        if len(args)>1:
            print("Error: 'list' command does not take any arguments.")
            return

        depenses=load_depenses()
        if not depenses:
            print("No expenses found.")
            return
        for d in depenses:
            print( f"{d['id']}: {d['description']} - ${d['prix']}")

        #python expense_cli.py summary
        #####Total expenses: $25.0 

    elif command=="summary":
        if len(args)>0:
            print("Error: 'summary' command does not take any arguments.")
            return
        expenses=load_depenses()
        total= sum(e['prix'] for e in expenses)
        print(f"Total expenses: ${total}")

    elif command=="delete":
        #[DELETE , 2 ] SO ARGS LENGTH IS 2
        if len(args)<2 or len(args)>2:
            print("Error: MAke sure only one expense ID is provided.")
            return

        depense_id_to_delete= int(args[1]) # INDEX 1 IS THE ID OF THE EXPENSE TO DELETE
      
        depenses=load_depenses()

        #depense_to_delete is the subset of the dictionary in the list of dictionaries that matches the ID to delete
        depense_to_delete=find_depense_id(depenses, depense_id_to_delete)
        print("DEBUG - found:", depense_to_delete)
        if not depense_to_delete:
            print(f"Error: Expense with ID {depense_id_to_delete} not found.")
            return
        
        depenses.remove(depense_to_delete)
        print("DEBUG - list right before saving:", depenses)
        save_depenses(depenses)
        print(f"Expense  {depense_id_to_delete} deleted .")


    ## python expense_cli.py update 1 "Lunch with client" 25
    #####Expense 1 updated.
    elif command=="update":
        if len(args)<4 or len(args)>4:
            print("Error: Missing depense ID, description or price.")
            return

        depense_id_to_update=int(args[1])
        new_description=args[2]
        try:
            new_prix=float(args[3])
        except ValueError:
            print("Error: Price must be a number.")
            return

        depenses=load_depenses()
        depense_to_update=find_depense_id(depenses, depense_id_to_update)
        if not depense_to_update:
            print(f"Error: Expense with ID {depense_id_to_update} not found.")
            return
        
        depense_to_update['description']=new_description
        depense_to_update['prix']=new_prix
        save_depenses(depenses)
        print(f"Expense with ID {depense_id_to_update} updated successfully.")

    
    else:
        print(f"Error: Unknown command '{command}'. Available commands: add, list, summary, update, delete")




if __name__=="__main__":
    main()