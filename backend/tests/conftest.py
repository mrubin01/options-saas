import sys
from pathlib import Path

# Add backend/ to PYTHONPATH so "import app" works
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
