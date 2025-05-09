#!/usr/bin/env python3

from data_structures import get_names, get_spiciest_foods, print_spicy_foods,\
                                create_spicy_food, get_spicy_food_by_cuisine, \
                                print_spiciest_foods, get_average_heat_level

import io
import sys

class TestDataStructures:
    '''Module data_structures.py'''

    SPICY_FOODS = [
        {
            "name": "Green Curry",
            "cuisine": "Thai",
            "heat_level": 9,
        },
        {
            "name": "Buffalo Wings",
            "cuisine": "American",
            "heat_level": 3,
        },
        {
            "name": "Mapo Tofu",
            "cuisine": "Sichuan",
            "heat_level": 6,
        }
    ]

    def test_get_names(self):
        '''contains function get_names() that retrieves names from list of foods.'''
        assert(get_names(TestDataStructures.SPICY_FOODS) == ['Green Curry', 'Buffalo Wings', 'Mapo Tofu'])

    def test_get_spiciest_foods(self):
        '''contains function get_spiciest_foods() that returns foods with a heat_level over 5.'''
        for food in get_spiciest_foods(TestDataStructures.SPICY_FOODS):
            assert(food["heat_level"]) > 5
    
    def test_print_spicy_foods(self):
        '''contains function print_spicy_foods that returns all foods formatted with 🌶  emojis.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_spicy_foods(TestDataStructures.SPICY_FOODS)
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶\n" +
            "Buffalo Wings (American) | Heat Level: 🌶🌶🌶\n" +
            "Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶\n")

    def test_get_spicy_food_by_cuisine(self):
        '''contains function get_spicy_food_by_cuisine that returns the food that matches a cuisine.'''
        assert(get_spicy_food_by_cuisine(TestDataStructures.SPICY_FOODS, "American") == {
            "name": "Buffalo Wings",
            "cuisine": "American",
            "heat_level": 3,
        })

    def test_print_spiciest_foods(self):
        '''contains function print_spiciest_foods that returns foods with heat_level over 5 formatted with 🌶  emojis.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_spiciest_foods(TestDataStructures.SPICY_FOODS)
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶\n" +
            "Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶\n")

    def test_get_average_heat_level(self):
        '''contains function get_average_heat_level that returns average of heat_levels in spicy_foods.'''
        assert(get_average_heat_level(TestDataStructures.SPICY_FOODS) == 6)

    def test_create_spicy_food(self):
        '''contains function create_spicy_food that returns original list of spicy_foods with new spicy_food added.'''
        new_spicy_foods = create_spicy_food(
           TestDataStructures.SPICY_FOODS,
            {
                'name': 'Griot',
                'cuisine': 'Haitian',
                'heat_level': 10,
            }
        )

        assert new_spicy_foods == [
            {
                "name": "Green Curry",
                "cuisine": "Thai",
                "heat_level": 9,
            },
            {
                "name": "Buffalo Wings",
                "cuisine": "American",
                "heat_level": 3,
            },
            {
                "name": "Mapo Tofu",
                "cuisine": "Sichuan",
                "heat_level": 6,
            },
            {
                "name": "Griot",
                "cuisine": "Haitian",
                "heat_level": 10,
            },
        ]

    def test_get_names_empty_list(self):
        '''get_names should return an empty list when given an empty list.'''
        assert get_names([]) == []

    def test_get_spiciest_foods_empty_list(self):
        '''get_spiciest_foods should return an empty list when given an empty list.'''
        assert get_spiciest_foods([]) == []

    def test_get_spiciest_foods_no_spicy_foods(self):
        '''get_spiciest_foods should return an empty list when no foods have heat_level > 5.'''
        foods = [
            {"name": "Mild Curry", "cuisine": "Indian", "heat_level": 2},
            {"name": "Sweet Wings", "cuisine": "American", "heat_level": 3},
        ]
        assert get_spiciest_foods(foods) == []

    def test_print_spicy_foods_empty_list(self):
        '''print_spicy_foods should not print anything when given an empty list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_spicy_foods([])
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == ""

    def test_get_spicy_food_by_cuisine_not_found(self):
        '''get_spicy_food_by_cuisine should return None when no food matches the given cuisine.'''
        assert get_spicy_food_by_cuisine(TestDataStructures.SPICY_FOODS, "Mexican") is None

    def test_get_average_heat_level_empty_list(self):
        '''get_average_heat_level should return 0 when given an empty list.'''
        assert get_average_heat_level([]) == 0

    def test_create_spicy_food_empty_list(self):
        '''create_spicy_food should return a list with the new food when given an empty list.'''
        new_food = {"name": "Griot", "cuisine": "Haitian", "heat_level": 10}
        assert create_spicy_food([], new_food) == [new_food]

    def test_create_spicy_food_duplicate(self):
        '''create_spicy_food should allow adding duplicate foods to the list.'''
        new_food = {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}
        updated_list = create_spicy_food(TestDataStructures.SPICY_FOODS, new_food)
        assert updated_list.count(new_food) == 2
