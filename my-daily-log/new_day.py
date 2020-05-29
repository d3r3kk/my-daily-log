import datetime
import docopt
import logging
import os
import pathlib
import shutil
import sys


log = logging.getLogger(__name__)


def get_template(base_dir: pathlib.Path) -> pathlib.Path:
    """Return the absolute path to the raw template for daily logs."""

    log.debug("get_template")
    return base_dir.joinpath("daily_schedule-j.md")


def get_log_folder_for_month(
    log_folder_base: pathlib.Path, now: datetime
) -> pathlib.Path:
    """Get the folder to contain today's log."""

    log.debug("get_log_folder_for_month")

    log_epoch_foldername = "day-tracking-juniper"
    log_month_foldername = now.strftime("%m_%B_%y")
    log.debug(f"folder name = {log_epoch_foldername}/{log_month_foldername}.")
    return log_folder_base.joinpath(log_epoch_foldername, log_month_foldername)


def create_new_log(
    now: datetime,
    template_file: pathlib.Path,
    log_folder: pathlib.Path,
    force: bool = False,
):
    """Copy the template to the log folder and update any dynamic elements within the file."""

    log.debug("create_new_log")

    log_file_name = now.strftime("%b_%d_%y.md").lower()
    log_file_path = log_folder.joinpath(log_file_name)
    if not log_file_path.exists() or force:
        log.debug(f"Creating log file at {log_file_path}")
        log_folder.mkdir(parents=True, exist_ok=True)
        shutil.copy2(template_file, log_file_path)


def create_new_day(log_day: datetime, force: bool):
    log.debug("create_new_day")
    if log_day is None:
        log_day: datetime = datetime.date.today()
        log.debug(f'Default log day being used (today={log_day.strftime("%b_%d_%y")})')

    base_folder: pathlib.Path = pathlib.Path(__file__).resolve().parent
    template: pathlib.Path = get_template(base_folder)
    log_folder: pathlib.Path = get_log_folder_for_month(base_folder, log_day)
    create_new_log(log_day, template, log_folder, force)
