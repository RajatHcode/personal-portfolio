"""module ProvidingFunction to parse the argumets"""
import argparse
import logging
import sys

from pylint.lint import Run

logging.getLogger().setLevel(logging.INFO)

parser = argparse.ArgumentParser(prog="LINT")

parser.add_argument(
    "-p",
    "--path",
    help="path to directory you want to run pylint | " "Default: %(default)s | " "Type: %(type)s ",
    default="./src",
    type=str,
)

parser.add_argument(
    "-t",
    "--threshold",
    help="score threshold to fail pylint runner | " "Default: %(default)s | " "Type: %(type)s ",
    default=7,
    type=float,
)

args = parser.parse_args()
PATH = str(args.path)
threshold = float(args.threshold)

logging.info("PyLint Starting | " "Path: {%s} | " "Threshold: {%s} ", PATH, threshold)

results = Run([PATH], do_exit=False)
final_score = results.linter.stats.global_note

if final_score < threshold:

    message = "PyLint Failed | " "Score: {%s} | " "Threshold: {%s} ", final_score, threshold

    logging.error(message)
    raise Exception(message)

else:
    message = "PyLint Passed | " "Score: {%s} | " "Threshold: {%s} ", final_score, threshold
    logging.info(message)

sys.exit(0)
