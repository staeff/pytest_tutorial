import test_spam

# Example how to modify the pytest output.
# A bit contrived, because the unreadable output could have
# been fixed by defining __repr__ on Spam.
def pytest_assertrepr_compare(config, op, left, right):
    left_spam = isinstance(left, test_spam.Spam)
    right_spam = isinstance(right, test_spam.Spam)
    if left_spam and right_spam and op == '==':
        return [
            'Comparing Spam instances:',
            f'    counts: {left.count} != {right.count}'
        ]
