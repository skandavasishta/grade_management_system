from functions import *

assert get_list_avg([[10, 0, 2], [5, 10, 6], [7, 8, 9]]) == [4.0, 7.0, 8.0]
assert get_list_avg([[10, 0, 2], [5, 10, 6], [7, 8, 9], [5, 10, 6]]) == [4.0, 7.0, 8.0, 7.0]
assert get_list_avg([[10, 0, 2, 5, 10, 6], [7, 8, 9]]) == [5.5, 8.0]

all_grades = [
    { "category": "PA",
      "weight" : 5,
      "grades" : [100.0, 100.0, 100.0, 100.0, 100.0, 0.0, 95.0]
    },
    { "category": "CA",
      "weight" : 15,
      "grades" : [100.0, 100.0, 98.0, 95.0, 0.0, 100.0]
    },
    { "category": "LA",
      "weight" : 25.0,
      "grades" : [100.0, 100.0, 100.0, 5.0, 0.0, 70.0] 
    },
    { "category": "Quiz",
      "weight" : 25,
      "grades" : []
    },
    { "category": "Project",
      "weight" : 25,
      "grades" : []
    }
]

only_grades = [[100.0, 100.0, 100.0, 100.0, 100.0, 0.0, 95.0], [100.0, 100.0, 98.0, 95.0, 0.0, 100.0], [100.0, 100.0, 100.0, 5.0, 0.0, 70.0], [], []]
assert get_grades(all_grades) == only_grades

only_grades_test = [
    { "grades" : [100.0, 100.0, 100.0, 100.0, 100.0, 0.0, 95.0] },
    { "grades" : [100.0, 100.0, 98.0, 95.0, 0.0, 100.0] },
    { "grades" : [100.0, 100.0, 100.0, 5.0, 0.0, 70.0] },
    { "grades" : [] },
    { "grades" : [] }
] # same as all_grades but without the other keys
assert get_grades(only_grades_test) == only_grades

avg_grades = [85.0, 82.16666666666667, 62.5, 0, 0]
assert get_list_avg(only_grades) == avg_grades

assert get_total_grade(all_grades) - 32.20 <= 0.001
assert int(get_total_grade([])) == 0

######## ADD CATEGORY OPTION ########
assert is_num("8") == True
assert is_num(8) == False
assert is_num("3.95") == True
assert is_num("8.1.1") == False
assert is_num("8.apple") == False

# Edge cases causing errors
assert create_category("Quiz") == -2
assert create_category("Quiz Quiz Quiz") == -2
assert create_category("Quiz 15 0") == -2

assert create_category("Q 15") == -1
assert create_category("Q,Q 15") == -1

assert create_category("Quiz A") == 0
assert create_category("Quiz 15.A") == 0
assert create_category("Quiz 15.5.5") == 0

# test creation of a category dictionary
arg = "Quiz 25"
result = create_category(arg)
expected_result = { 'category': 'Quiz', 'weight': 25.0, 'grades': [] }
print(f"--> create_category({arg}) returned\n`{result}`\n")
assert result == expected_result

assert create_category("PA 5") == { 'category': 'PA', 'weight': 5.0, 'grades': [] }

######## ADD - GRADES OPTION ########
assert is_valid_index('0', ["Quizzes", 25.5]) == True
assert is_valid_index('1', ["Quizzes", 25.5]) == True
assert is_valid_index('2', ["Quizzes", 25.5]) == False
assert is_valid_index('2', ["Quizzes", 25.5], 1) == True # overwriting the default

######## UPDATE CATEGORY OPTION ########

# Edge cases causing errors (same as for create_category())
assert update_category(all_grades, 3, "Quiz") == -2
assert update_category(all_grades, 3, "Quiz Quiz Quiz") == -2
assert update_category(all_grades, 3, "Quiz 15 0") == -2

assert update_category(all_grades, 3, "Q 15") == -1
assert update_category(all_grades, 3, "Q,Q 15") == -1

assert update_category(all_grades, 3, "Quiz A") == 0
assert update_category(all_grades, 3, "Quiz 15.A") == 0
assert update_category(all_grades, 3, "Quiz 15.5.5") == 0

# change the Quiz
assert update_category(all_grades, 3, "zzz 0") == { 'category': 'zzz', 'weight': 0.0, 'grades': [] }
assert all_grades[3] == { 'category': 'zzz', 'weight': 0.0, 'grades': [] }
# undo the previous call by restoring the Quiz back
assert update_category(all_grades, 3, "Quiz 25") == { 'category': 'Quiz', 'weight': 25.0, 'grades': [] }
assert all_grades[3] == { 'category': 'Quiz', 'weight': 25.0, 'grades': [] }

# Verify that grades are untouched
"""
la_20_dict = { 'category': 'LA', 'weight': 20.0, 'grades': [100.0, 100.0, 100.0, 5.0, 0.0, 70.0] }
assert update_category(all_grades, 2, "LA 20") == la_20_dict
assert all_grades[2] == la_20_dict
"""
######## DELETE OPTION ########

assert delete_item([], 1, 1) == 0
assert delete_item([1], '-2') == -1
assert delete_item([1, 2, 3], '2') == 3
