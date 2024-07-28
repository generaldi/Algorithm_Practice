from pyecharts.charts import Line
from pyecharts.faker import Faker
line = Line()
line.add_xaxis(Faker.choose())
line.add_yaxis("商家A", Faker.values())
line.add_yaxis("商家B", Faker.values())
line.add_yaxis("商家C", Faker.values())
line.render()