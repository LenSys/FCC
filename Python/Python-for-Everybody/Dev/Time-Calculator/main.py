# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


# print(add_time("11:06 PM", "2:02"))

# print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

# print(add_time("8:16 PM", "466:02", "tuesday"))

print(add_time("11:59 PM", "24:05", "Wednesday"))
print("expected: 12:04 AM, Friday (2 days later)")
# "11:59 PM", "24:05", "Wednesday" to return "12:04 AM, Friday (2 days later)"

# Run unit tests automatically
main(module='test_module', exit=False)