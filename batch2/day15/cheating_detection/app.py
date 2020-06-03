
from views.AuthView import AuthView
from views.DetectionView import DetectionView

class MyApp:

    def __init__(self):
        # av = AuthView()
        # av.load()
        dv = DetectionView()
        dv.load()

app = MyApp()
