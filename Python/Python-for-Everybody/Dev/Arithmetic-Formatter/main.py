# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# print(arithmetic_arranger(['3801 - 2', '123 + 49']))
# expected_output = '  3801      123\n-    2    +  49\n------    -----'
# Run unit tests automatically
main(['-vv'])
