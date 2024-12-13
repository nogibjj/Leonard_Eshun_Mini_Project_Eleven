"""
Extract data from a url and save as a file
"""

import requests


def extract(
    url: str,
    file_name: str,
):
    """ "Extract a url to a file path"""
    file_path = "data/" + file_name
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return "Extract Successful"


def do_extract():
    # log_tests("Extraction Test", header=True, new_log_file=True)
    # log_tests("Removing existing CSV file exists")
    if os.path.exists("data/air_quality.csv"):
        os.remove("data/air_quality.csv")

    # log_tests("Confirming that CSV file doesn't exists...")
    assert not os.path.exists("population_bar.png")
    # log_tests("Test Successful")

    # log_tests("Extracting data and saving...")
    extract(
        "https://data.cityofnewyork.us/resource/c3uy-2p5r.csv?$limit=200000",
        "air_quality.csv",
    )

    # log_tests("Testing if CSV file exists...")
    assert os.path.exists("data/air_quality.csv")
    # log_tests("Extraction Test Successful", last_in_group=True)
    print("Extraction Test Successful")
