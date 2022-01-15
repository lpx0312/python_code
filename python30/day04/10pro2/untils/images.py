import  sys
import  os

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)
print(sys.path)
print("images>>main")
def images():
    print("images")