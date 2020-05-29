"""new_day.py

Program to create a new daily log file in the WDIDT format.

Usage:
  my-daily-log (-h | --help | --version)
  my-daily-log [-a DAYS] [-b FLDR] [-t TPLT] [--force] [--verbose]

Options:
  -h, --help                   Show this help and exit.
  --version                    Show the version of this script and exit.
  -a DAYS, --ago=DAYS          Create a log file for num_days ago.
  -b FLDR, --base-folder=FLDR  The base folder to create log files within. [default: .]
  -t TPLT, --template=TPLT     Template file to use in creating the new daily log. [default: my-daily-log.md]
  -f, --force                  Always create the log file, even if it exists.
  --verbose                    Show verbose logs during processing.
"""

import datetime
import logging

import docopt

from . import config
from . import new_day

logging.basicConfig(
    format="[%(asctime)s]%(name)s.%(levelname)s: %(message)s", level=logging.INFO
)


if __name__ == "__main__":
    opts = docopt.docopt(doc=__doc__, help=True, version="0.1")
    print(opts)

    log_level = logging.INFO
    if opts.get("--verbose", False):
        log_level = logging.DEBUG

    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

    log.debug("Arguments given:")
    log.debug(opts)

    log_day = datetime.date.today()

    if opts.get("--ago", None):
        log_day = datetime.date.today() - datetime.timedelta(
            days=int(opts.get("--ago", 0))
        )
        log.debug(f"Log file day is being set to {log_day}.")

    new_day.create_new_day(log_day, opts.get("--force", False))
