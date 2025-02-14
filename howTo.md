create a .env file with the following:
GEMINI_KEY=

Create a virtual environment

```bash
python -m venv nameOfFolderWithVenv
cd nameOfFolderWithVenv/bin
source activate
cd ../..
pip install -r requirements.txt
playwright install
```

then run the following command:

```bash
python test_practice_auto.py
```

```bash
or
python test_any_test_as_long_as_it_starts_with_test*.py
```
