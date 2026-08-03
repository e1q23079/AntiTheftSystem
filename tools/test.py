import unittest


def main():
    loader = unittest.TestLoader()
    suite = loader.discover("lib/tests", pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == "__main__":
    main()
