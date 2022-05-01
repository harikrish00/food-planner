import json
import random


def pick_random_side_dish(side_dish_list: list) -> str:
    return random.choice(side_dish_list)


def food_schedule_of_the_week(food_items: dict):
    NUM_OF_DAYS = 5
    main_dish_list: list = food_items['mainDish']
    vegetables_needed = []
    for i in range(NUM_OF_DAYS):
        len_of_main_dish_list: int = len(main_dish_list)
        chosen_main_dish: dict = random.randint(0,len_of_main_dish_list-1)
        print(main_dish_list[chosen_main_dish])
        side_dish: str = pick_random_side_dish(main_dish_list[chosen_main_dish]["sideDish"])
        print(f'side dish:{side_dish}')
        main_dish_list.pop(chosen_main_dish)
        
    #number of days
    #for each day pick a random main dish
    #for picked mainDish, get the side dish
    #fetch the sideDish object from DB and get the vegetables/ingredients 
    #Store it in dict with mainDish as key
    #iterate to next day, pick a random mainDish, check if thats not already picked
    #if picked, fetch another one





def lambda_handler(event, context):
    food_db_file = open('food_db.json')
    food_items = json.load(food_db_file)
    # print(food_items)
    food_schedule_of_the_week(food_items)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


if __name__ == ('__main__'):
    lambda_handler('test','test')