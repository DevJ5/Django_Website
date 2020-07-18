## Activate virtual env
source django_env/Scripts/activate

## Create file with all dependencies
pip freeze --local > requirements.txt

## Deactivate the virutal env
deactivate
