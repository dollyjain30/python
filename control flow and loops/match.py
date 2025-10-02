# What is Match-Case?
# Match-case is a new feature introduced in Python 3.10 for pattern matching.
# It simplifies complex conditional logic.
# Syntax:
# match value:
#     case pattern1:
#         # Code to execute if value matches pattern1
#     case pattern2:
#         # Code to execute if value matches pattern2
#     case _:
#         # Default case (if no patterns match)
status = 200

match status:
    case 200:
        print("Success!")
    case 404:
        print("Not Found")
    case _:
        print("Unknown Status")