import io
import pandas as pd
import requests
from io import BytesIO
import zipfile

if "data_loader" not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    url = "https://openpowerlifting.gitlab.io/opl-csv/files/openpowerlifting-latest.zip"
    response = requests.get(url)
    # define data types to reduce pandas memory consumption
    dtypes = {
        "Name": "object",
        "Sex": "object",
        "Event": "object",
        "Equipment": "object",
        "Age": "float64",
        "AgeClass": "object",
        "BirthYearClass": "object",
        "Division": "object",
        "BodyweightKg": "float64",
        "WeightClassKg": "object",
        "Squat1Kg": "float64",
        "Squat2Kg": "float64",
        "Squat3Kg": "float64",
        "Squat4Kg": "float64",
        "Best3SquatKg": "float64",
        "Bench1Kg": "float64",
        "Bench2Kg": "float64",
        "Bench3Kg": "float64",
        "Bench4Kg": "float64",
        "Best3BenchKg": "float64",
        "Deadlift1Kg": "float64",
        "Deadlift2Kg": "float64",
        "Deadlift3Kg": "float64",
        "Deadlift4Kg": "float64",
        "Best3DeadliftKg": "float64",
        "TotalKg": "float64",
        "Place": "object",
        "Dots": "float64",
        "Wilks": "float64",
        "Glossbrenner": "float64",
        "Goodlift": "float64",
        "Tested": "object",
        "Country": "object",
        "State": "object",
        "Federation": "object",
        "ParentFederation": "object",
        "Date": "object",
        "MeetCountry": "object",
        "MeetState": "object",
        "MeetTown": "object",
        "MeetName": "object"
    }

    if response.status_code == 200:
        zip_content = BytesIO(response.content)
        with zipfile.ZipFile(zip_content, "r") as zip_file:
            csv_file = [
                file for file in zip_file.namelist() if file.lower().endswith(".csv")
            ][0]
            df = pd.read_csv(zip_file.open(csv_file), dtype=dtypes)
            print(df.dtypes)
            print(df)
            return df
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


@test
def test_output(output, *args) -> None:
    assert output is not None, "The output is undefined"
