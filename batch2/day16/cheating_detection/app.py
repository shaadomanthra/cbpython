
from views.AuthView import AuthView
from views.DetectionView import DetectionView

class MyApp:

    def run(self):
        av = AuthView()
        av.transfer_control = self.detector
        av.load()

    def detector(self):
        dv = DetectionView()
        dv.load()



app = MyApp()
app.run()
