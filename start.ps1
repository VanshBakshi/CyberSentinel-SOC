$ErrorActionPreference = "Stop"
if (!(Test-Path ".venv\Scripts\python.exe")) {
  py -m venv .venv
}
$py = ".\.venv\Scripts\python.exe"
& $py -m pip install --upgrade pip
& $py -m pip install -r requirements.txt
& $py scripts\seed_demo.py
& $py -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
