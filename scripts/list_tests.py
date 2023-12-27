import os
from pathlib import Path

TESTD = Path(__file__).parent.parent / 'tests'
tests = [f for f in os.listdir(TESTD) if f.startswith('test_') and f.endswith('.cpp')]
tests.sort()
for t in tests:
    print(str(TESTD / t))