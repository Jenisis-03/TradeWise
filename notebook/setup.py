import os
import sys
import pathlib

THIS_FILE_PATH = pathlib.Path(__file__).resolve()
NBS_DIR = THIS_FILE_PATH.parent
REPO_DIR = NBS_DIR.parent
DJANGO_BASE_DIR = REPO_DIR / "src"

def init_django(project_name='home.main'):
    """Run administrative tasks."""
    os.chdir(DJANGO_BASE_DIR)
    sys.path.insert(0, str(DJANGO_BASE_DIR))
    
    # Set the DJANGO_SETTINGS_MODULE to point to the correct settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", project_name + ".settings")
    
    os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = "true"
    
    import django
    django.setup()