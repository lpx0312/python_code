

import  sys
import  os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_PATH)
# 或 sys.path.append(BASE_PATH)
from main import main

if __name__ == '__main__':
    main.start()
