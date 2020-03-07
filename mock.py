from unittest.mock import MagicMock
from unittest.mock import patch

# all this from https://docs.python.org/3/library/unittest.mock.html

# ----------------------------------------------------------------------

# first, just overwrite the underlying input() method, saving the
# original for later
save_input = __builtins__.input
__builtins__.input = MagicMock(return_value='world')

answer = input()
print("Hello " + answer + "!")

# restore the original
__builtins__.input = save_input

# ----------------------------------------------------------------------

# now, use patch that automatically saves and restores
mock = MagicMock(return_value="wirled")
with patch('builtins.input', mock):
    answer = input()
    print("Hello " + answer + "!")

# ----------------------------------------------------------------------

# do the same for print
save_print = __builtins__.print
__builtins__.print = MagicMock()

print("Hello world!")

# make sure it was called with the expected value and restore
__builtins__.print.assert_called_once_with("Hello world!")
__builtins__.print = save_print

# ----------------------------------------------------------------------

# and patch for print
mock = MagicMock()
with patch('builtins.print', mock):
    print("Hello world!")
    mock.assert_called_once_with("Hello world!")

# ----------------------------------------------------------------------

# now, combine the two to do I/O
input_mock = MagicMock(return_value="wirled")
output_mock = MagicMock()
with patch('builtins.input', input_mock):
    with patch('builtins.print', output_mock):
        answer = input()
        print("Hello " + answer + "!")
        output_mock.assert_called_once_with("Hello wirled!")

# ----------------------------------------------------------------------

# now use a annotation/decorator for a method. this is probably how you
# want to structure your unit tests

input_mock.reset_mock()
output_mock.reset_mock()

@patch('builtins.input', input_mock)
@patch('builtins.print', output_mock)
def foo():
    answer = input()
    print("Hello " + answer + "!")
    output_mock.assert_called_once_with("Hello wirled!")

foo()
