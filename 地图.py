import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
# from pyecharts.globals import CurrentConfig, NotebookType
# CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

io = r'D:\案例\海底捞\海底捞门店.xls'
df = pd.read_excel(io=io,engine='xlrd')
df['province'] = df['province'].apply(lambda x: x[:3] if x.startswith('黑龙江') else x[:3] if x.startswith('内蒙古') else x[:2])
# df['city'] = df['city'].apply(lambda x: x[:2])
# df['district'] = df['district'].apply(lambda x: x[:2])

xxx = []
b = df.query("city=='广州市'")['district'].value_counts()
for i in zip(b.index,b.values):
    xxx.append(list(i))
print(xxx)

data_pair_province = [['广东', 163], ['江苏', 142], ['浙江', 108], ['山东', 75], ['北京', 73], ['上海', 72], ['河南', 69],['陕西', 69],['湖北', 65], ['福建', 58], ['安徽', 50], ['四川', 45], ['湖南', 42], ['河北', 39], ['天津', 31], ['江西', 24], ['辽宁', 22], ['广西', 22], ['山西', 18], ['云南', 17], ['台湾', 14], ['重庆', 13], ['甘肃', 13], ['黑龙江', 12], ['贵州', 12], ['吉林', 12], ['海南', 11], ['内蒙古', 9], ['宁夏', 8], ['香港', 5], ['青海', 2], ['澳门', 2]]
data_pair_guangdong = [['深圳市', 42], ['广州市', 41], ['佛山市', 17], ['东莞市', 14], ['惠州市', 7], ['中山市', 6], ['汕头市', 5], ['江门市', 5], ['湛江市', 5], ['珠海市', 4], ['揭阳市', 3], ['梅州市', 3], ['清远市', 2], ['阳江市', 2], ['茂名市', 2], ['肇庆市', 2], ['河源市', 1], ['云浮市', 1], ['汕尾市', 1]]
data_pair_guangzhou = [['天河区', 7], ['白云区', 7], ['番禺区', 6], ['海珠区', 6], ['黄埔区', 4], ['增城区', 3], ['荔湾区', 2], ['花都区', 2], ['越秀区', 2], ['南沙区', 1], ['从化区', 1]]
map_province = (
    Map()
    .add(series_name='海底捞店铺数',data_pair=data_pair_province,maptype='china')
    .set_global_opts(title_opts=opts.TitleOpts(title='海底捞全国各省店铺数分布'),visualmap_opts=opts.VisualMapOpts(max_=170,is_piecewise=True))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
)
# map_province.render('海底捞全国各省店铺数分布.html')

map_guangdong = (
    Map()
    .add(series_name='海底捞店铺数',data_pair=data_pair_guangdong,maptype='广东')
    .set_global_opts(title_opts=opts.TitleOpts(title='海底捞广东省各市分布'),visualmap_opts=opts.VisualMapOpts(max_=45,is_piecewise=True))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
)
# map_guangdong.render('海底捞广东省各市分布.html')

map_guangzhou = (
    Map()
    .add(series_name='海底捞店铺数',data_pair=data_pair_guangzhou,maptype='广州')
    .set_global_opts(title_opts=opts.TitleOpts(title='海底捞广州市各区分布'),visualmap_opts=opts.VisualMapOpts(max_=8,is_piecewise=True))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
)
map_guangzhou.render('海底捞广州市各区分布.html')