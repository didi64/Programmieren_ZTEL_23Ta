_ESC = chr(27)
_RESET = _ESC + '[0m'
_RED = _ESC + '[1;31m'
_GREEN = _ESC + '[0;32m'
_BLUE = _ESC + '[0;34m'
BLUE = f'{_BLUE}{{}}{_RESET}'
GREEN = f'{_GREEN}{{}}{_RESET}'
RED = f'{_RED}{{}}{_RESET}'


def run_test(fun, args, results):
    success = True
    help(fun)
    for arg, res in zip(args, results):
        call = BLUE.format(f'{fun.__name__}{arg}')
        print(f'calling {call}')
        if res == fun(*arg):
            print(GREEN.format('test passed'))
        else:
            print(RED.format('test failed'))
            success = False
    print('-' * 80)
    return success


def run_tests(tests):
    success = True
    for test in tests:
        success = success and run_test(*test)
    if success:
        print(RED.format('All tests passed'))
    else:
        print(GREEN.format('Some tests failed'))
    return success
