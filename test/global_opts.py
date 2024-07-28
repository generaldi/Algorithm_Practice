from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
test_examle=(
    Bar(
        init_opts=opts.InitOpts
        (
            page_title="Bar-基本示例",
            theme=ThemeType.ROMANTIC,
            bg_color="#fff",
            ),
        )
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Bar-基本示例",
                subtitle='副标题',
                pos_left="center",
                item_gap=20,),
            #缩放条配置
            datazoom_opts=opts.DataZoomOpts(
                is_show=True,#是否显示组件
                type_="inside",#组件类型:slider,inside,both
                is_realtime=True,#是否实时显示
                range_start=0,#数据范围开始
                range_end=100,#数据范围结束
                orient="vertical",#垂直显示
                is_zoom_lock=True,#是否锁定缩放
            ),
            legend_opts=opts.LegendOpts(
                type_='plain',#图例类型：plain,scroll,vertical
                is_show=True,#是否显示图例
                pos_top="10",#图例位置
                pos_left="center",#图例位置
                orient="vertical",#图例方向
                selected_mode='multiple',#选择模式：single(单选),multiple
                align="left",#图例文字和图标的位置对齐方式
                legend_icon='circle',#图例图标形状
                ),
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,#是否显示组件
                type_="color",#组件类型:size,color,both
                min_=0,#最小值
                max_=100,#最大值
                range_text=["High", "Low"],#数据范围文字
                orient="horizontal",#水平显示
                pos_top="5%",#组件位置
                pos_right="10",#组件位置
                is_piecewise=False,#是否为分段型
                is_inverse=True,#是否反向显示
                ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,#是否显示提示框to
                trigger="item",#触发类型：item,axis 
                #{a}: 系列名称
                #{b}: 数据项名称
                #{c}: 数据值
                #{d}: 数据百分比
                formatter="{a} <br/>{b} : {c} ({d}%)",#提示框内容格式
                background_color='white',
                )
            )
        
        .render("bar_base.html")
)