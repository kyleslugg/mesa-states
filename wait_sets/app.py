from model import BasicModel
import datetime as dt

start = dt.datetime(2020, 1, 1)
end = dt.datetime(2020, 1, 10)
delta = dt.timedelta(hours=1)

model = BasicModel(start, end, delta)
model.run_model()
