
from views.AuthView import AuthView
from views.DetectionView import DetectionView
from views.BarView import BarView

class MyApp:

    def run(self):
        av = AuthView()
        av.transfer_control = self.detector
        av.load()

    def detector(self):
        dv = DetectionView()
        dv.load()

    def Barcode(self):
        bv = BarView()
        bv.load()




app = MyApp()
app.run()
# app.Barcode()
