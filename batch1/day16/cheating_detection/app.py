
# import sys
# print(sys.executable)

from views.AuthView import AuthView
from views.DetectionView import DetectionView
from views.BarView import BarView

class MyApp:

    def run(self):
        av = AuthView()
        av.transfer_control = self.detection
        av.load()


    def detection(self):
        dv = DetectionView()
        dv.load()

    def Bar(self):
        b = BarView()
        b.load()


app = MyApp()
app.run()

#  To try barcode invoke Bar function
#  app.Bar()