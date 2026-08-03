import unittest


def test_lib():
    loader = unittest.TestLoader()
    suite = loader.discover("lib/tests", pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def test_server():
    loader = unittest.TestLoader()
    suite = loader.discover("tests", pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def main():
    test_lib()
    test_server()


if __name__ == "__main__":
    main()
