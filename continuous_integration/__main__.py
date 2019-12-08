import argparse
import sys

from continuous_integration.run_tests import run_tests
from continuous_integration.run_pylint import run_pylint
from continuous_integration.install_or_skip_dependencies import install_or_skip_dependencies

def parse_argurments():
    parser = argparse.ArgumentParser("Continous Integration Tools")
    parser.add_argument("--tests", action='store_true')
    parser.add_argument("--pylint", action='store_true')
    parser.add_argument("--install_or_skip_dependencies", action='store_true')
    return parser.parse_args()

def main():
    arguments = parse_argurments()
    if arguments.tests:
        returncode = run_tests()
    elif arguments.pylint:
        returncode = run_pylint()
    elif arguments.install_or_skip_dependencies:
        returncode = install_or_skip_dependencies()
    print("Return code is ", returncode)
    sys.exit(returncode)

if __name__ == "__main__":
    main()
