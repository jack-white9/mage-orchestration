import pandas as pd
import numpy as np

if "transformer" not in globals():
    from mage_ai.data_preparation.decorators import transformer
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print("Replacing strings with bools in 'Tested' column")
    data['Tested'] = data['Tested'].replace({'Yes': True, 'No': False, None: False})
    return data


@test
def test_output(output, *args) -> None:
    assert 'Yes' not in output['Tested'], "There are non-boolean 'Yes' values in the 'Tested' column."
    assert 'No' not in output['Tested'], "There are non-boolean 'No' values in the 'Tested' column."
    assert None not in output['Tested'], "There are non-boolean None values in the 'Tested' column."
