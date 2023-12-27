import os
import sys
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', action='store_true', help='Force rebuild')
parser.add_argument('-c', '--coverage', action='store_true', help='Enable coverage')
parser.add_argument('--cov-fmt', default='coverage-html', choices=['coverage-html', 'coverage-xml', 'coverage-text'], help='Coverage format')

args = parser.parse_args()
SETUP_OPT = "--wipe" if args.force else "--reconfigure"

HOME_DIR = Path(__file__).parent.parent
BUILD_DIR = Path('build')
os.chdir(HOME_DIR)
os.system(f"meson setup -Db_coverage=true -Db_sanitize=address {BUILD_DIR} {SETUP_OPT}")
os.system(f"meson compile -C {BUILD_DIR}")
# os.system(f"meson test -C {BUILD_DIR}")
os.system(f"./{BUILD_DIR/'test_bin'}")
if args.coverage:
    os.system(f"ninja -C {BUILD_DIR} {args.cov_fmt}")
