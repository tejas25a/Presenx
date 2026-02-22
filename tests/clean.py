def cl():
    from pathlib import Path
    import shutil

    #Presenx dir 
    BASE_DIR = Path(__file__).resolve().parents[1]

    #Data dir
    DATA_DIR = BASE_DIR / "data"

    #src dir
    SRC_DIR = BASE_DIR / "src/__pycache__"

    #test dir
    TEST_DIR = BASE_DIR / "tests/__pycache__"

    if DATA_DIR.exists() and DATA_DIR.is_dir():
        shutil.rmtree(DATA_DIR)
    if SRC_DIR.exists() and SRC_DIR.is_dir():
        shutil.rmtree(SRC_DIR)
    if TEST_DIR.exists() and TEST_DIR.is_dir():
        shutil.rmtree(TEST_DIR)

if __name__ == "__main__":
    cl()
