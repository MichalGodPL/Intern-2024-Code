import json  # Importujemy moduł json. / We import the json module.

# Określamy ścieżkę do pliku JSON. / We specify the path to the JSON file.
json_file_path = 'C:/Users/Admin/Desktop/PythonIntern/Dokument.json'

# Otwieramy plik JSON i wczytujemy jego zawartość. / We open the JSON file and load its contents.
with open(json_file_path, 'r') as json_file:
    dane = json.load(json_file)

# Definiujemy funkcję, która sprawdza, czy dane JSON są zgodne z formatem AWS::IAM::Role Policy.
# We define a function that verifies if the JSON data is in the AWS::IAM::Role Policy format.
def verify_aws_iam_role_policy(data):
    # Wymagane klucze w danych. / Required keys in the data.
    required_keys = ['Version', 'Statement']

    # Sprawdzamy, czy wszystkie wymagane klucze są obecne w danych. / We check if all required keys are present in the data.
    if not all(key in data for key in required_keys):
        return False

    # Przechodzimy przez każde oświadczenie w danych. / We go through each statement in the data.
    for statement in data['Statement']:
        # Sprawdzamy, czy wszystkie wymagane klucze są obecne w oświadczeniu. / We check if all required keys are present in the statement.
        if not all(key in statement for key in ['Effect', 'Action', 'Resource']):
            return False

        # Sprawdzamy, czy pole 'Resource' zawiera pojedynczy znak gwiazdki. / We check if the 'Resource' field contains a single asterisk.
        if statement['Resource'] == "*":
            return False

    # Jeśli wszystkie sprawdzenia przeszły pomyślnie, zwracamy True. / If all checks passed, we return True.
    return True

# Wywołujemy funkcję z wczytanymi danymi. / We call the function with the loaded data.
result = verify_aws_iam_role_policy(dane)

# Drukujemy wynik. / We print the result.
print(result)
