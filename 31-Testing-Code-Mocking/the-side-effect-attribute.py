from unittest import mock
from unittest.mock import Mock
from random import randint

def generate_number():
    return randint(1, 10)

call_me_maybe = Mock(side_effect= generate_number)
print(call_me_maybe.side_effect)

# call_me_maybe.side_effect = generate_number
print(call_me_maybe())
print(call_me_maybe())
print(call_me_maybe())
print(call_me_maybe())

three_itme_list = Mock()
three_itme_list.pop.side_effect = [3, 2, 1, IndexError("pop from empty list")]

print(three_itme_list.pop())
print(three_itme_list.pop())
print(three_itme_list.pop())
# print(three_itme_list.pop())

mock = Mock(side_effect= NameError("Some eror message"))
mock.side_effect = None
print(mock())