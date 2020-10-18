# Generated by Django 3.1.1 on 2020-10-17 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_code', models.CharField(db_index=True, default='', max_length=20, unique=True, verbose_name='基金代码')),
                ('fund_name', models.CharField(default='', max_length=200, verbose_name='基金名称')),
                ('fund_type', models.CharField(default='', max_length=200, verbose_name='基金类型')),
                ('fund_short_name', models.CharField(default='', max_length=200, verbose_name='基金简称')),
                ('pinyin_abbreviation_code', models.CharField(default='', max_length=200, verbose_name='基金首字母缩写')),
                ('establish_date', models.DateField(default='', null=True, verbose_name='基金创立日期')),
                ('handling_fee', models.FloatField(default=0, verbose_name='手续费率')),
                ('can_buy', models.BooleanField(default=False, verbose_name='可否购买')),
                ('initial_purchase_amount', models.FloatField(default=0, verbose_name='起购金额')),
                ('currency', models.CharField(blank=True, default='人民币', max_length=20, null=True, verbose_name='货币')),
                ('insert_time', models.DateTimeField(auto_now_add=True, verbose_name='爬取时间')),
                ('update_time', models.DateTimeField(null=True, verbose_name='更新时间')),
                ('is_deleted', models.IntegerField(default=0, verbose_name='是否删除')),
            ],
        ),
        migrations.CreateModel(
            name='FundCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(max_length=30, unique=True, verbose_name='基金公司 id')),
                ('company_name', models.CharField(default='', max_length=100, verbose_name='基金公司名')),
                ('company_short_name', models.CharField(default='', max_length=30, verbose_name='基金公司简称')),
                ('general_manager', models.CharField(default='', max_length=30, verbose_name='总经理')),
                ('establish_date', models.DateField(default='', verbose_name='基金公司创立日期')),
                ('total_manage_amount', models.FloatField(default=0, verbose_name='基金管理规模(亿元)')),
                ('total_fund_num', models.IntegerField(default=0, verbose_name='全部基金数')),
                ('total_manager_num', models.IntegerField(default=0, verbose_name='全部基金经理数')),
                ('tianxiang_star', models.PositiveIntegerField(default=0, verbose_name='天相评级(0星到五星)')),
                ('pinyin_abbreviation_code', models.CharField(default='', max_length=200, verbose_name='基金公司首字母缩写')),
                ('update_date', models.DateField(null=True, verbose_name='数据更新时间')),
                ('insert_time', models.DateTimeField(auto_now_add=True, verbose_name='爬取时间')),
                ('update_time', models.DateTimeField(null=True, verbose_name='更新时间')),
                ('is_deleted', models.IntegerField(default=0, verbose_name='是否删除')),
            ],
        ),
        migrations.CreateModel(
            name='FundLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='爬取名称')),
                ('total_fund', models.PositiveIntegerField(default=0, verbose_name='基金总数')),
                ('stock_fund_num', models.PositiveIntegerField(default=0, verbose_name='股票型基金总数')),
                ('hybrid_fund_num', models.PositiveIntegerField(default=0, verbose_name='混合型基金总数')),
                ('bond_fund_num', models.PositiveIntegerField(default=0, verbose_name='债券型基金总数')),
                ('index_fund_num', models.PositiveIntegerField(default=0, verbose_name='指数基金总数')),
                ('break_even_fund_num', models.PositiveIntegerField(default=0, verbose_name='保本型基金总数')),
                ('qdii_fund_num', models.PositiveIntegerField(default=0, verbose_name='QDII 型基金总数')),
                ('etf_fund_num', models.PositiveIntegerField(default=0, verbose_name='ETF 型基金总数')),
                ('lof_fund_num', models.PositiveIntegerField(default=0, verbose_name='LOF型基金总数')),
                ('fof_fund_num', models.PositiveIntegerField(default=0, verbose_name='FOF型基金总数')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
            ],
        ),
        migrations.CreateModel(
            name='FundManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='基金经理')),
                ('manager_id', models.CharField(max_length=20, unique=True, verbose_name='基金经理 id')),
                ('company_id', models.CharField(default='', max_length=20, verbose_name='所属公司 id')),
                ('working_time', models.IntegerField(default=0, verbose_name='从业时间(天)')),
                ('total_asset_manage_amount', models.FloatField(default=0, verbose_name='基金资产管理总规模(亿元)')),
                ('current_fund_best_profit', models.FloatField(default=0, verbose_name='现任基金最佳回报')),
                ('insert_time', models.DateTimeField(auto_now_add=True, verbose_name='爬取时间')),
                ('update_time', models.DateTimeField(null=True, verbose_name='更新时间')),
                ('is_deleted', models.IntegerField(default=0, verbose_name='是否删除')),
            ],
        ),
        migrations.CreateModel(
            name='FundTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='任务名')),
                ('func', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='执行函数名')),
                ('status', models.CharField(default='', max_length=100, verbose_name='任务状态')),
                ('insert_time', models.DateTimeField(auto_now_add=True, verbose_name='爬取时间')),
                ('update_time', models.DateTimeField(null=True, verbose_name='更新时间')),
                ('is_deleted', models.IntegerField(default=0, verbose_name='是否删除')),
            ],
        ),
        migrations.CreateModel(
            name='FundRanking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_code', models.CharField(db_index=True, default='', max_length=20, verbose_name='基金代码')),
                ('start_unit_net_worth', models.FloatField(default=0, verbose_name='起始单位净值')),
                ('start_cumulative_net_worth', models.FloatField(default=0, verbose_name='起始累计净值')),
                ('current_unit_net_worth', models.FloatField(default=0, verbose_name='当前单位净值')),
                ('current_cumulative_net_worth', models.FloatField(default=0, verbose_name='当前累计净值')),
                ('daily', models.FloatField(default=0, verbose_name='日涨跌幅')),
                ('last_week', models.FloatField(default=0, verbose_name='周涨跌')),
                ('last_month', models.FloatField(default=0, verbose_name='最近一个月涨跌')),
                ('last_three_month', models.FloatField(default=0, verbose_name='最近三个月涨跌')),
                ('last_six_month', models.FloatField(default=0, verbose_name='最近六个月涨跌')),
                ('last_year', models.FloatField(default=0, verbose_name='最近一年涨跌')),
                ('last_two_year', models.FloatField(default=0, verbose_name='最近两年涨跌')),
                ('last_three_year', models.FloatField(default=0, verbose_name='最近三年涨跌')),
                ('last_five_year', models.FloatField(default=0, verbose_name='最近五年涨跌')),
                ('ten_thousand_income', models.FloatField(default=0, verbose_name='万份收益')),
                ('annualized_income_7day', models.FloatField(default=0, verbose_name='7天年化收益率')),
                ('annualized_income_14day', models.FloatField(default=0, verbose_name='14天年化收益率')),
                ('annualized_income_28day', models.FloatField(default=0, verbose_name='28天年化收益率')),
                ('this_year', models.FloatField(default=0, verbose_name='今年以来涨跌')),
                ('since_founded', models.FloatField(default=0, verbose_name='成立以来涨跌')),
                ('since_founded_bonus', models.FloatField(default=0, verbose_name='成立以来分红')),
                ('since_founded_bonus_num', models.IntegerField(default=0, verbose_name='成立以来分红次数')),
                ('handling_fee', models.FloatField(default=0, verbose_name='手续费率')),
                ('current_date', models.DateField(default='', verbose_name='当前日期')),
                ('insert_time', models.DateTimeField(auto_now_add=True, verbose_name='爬取时间')),
                ('update_time', models.DateTimeField(null=True, verbose_name='更新时间')),
                ('is_deleted', models.IntegerField(default=0, verbose_name='是否删除')),
            ],
            options={
                'unique_together': {('fund_code', 'current_date')},
            },
        ),
        migrations.CreateModel(
            name='FundManagerRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_code', models.CharField(default='', max_length=20, verbose_name='基金代码')),
                ('manager_id', models.CharField(max_length=20, verbose_name='基金经理 id')),
                ('insert_time', models.DateTimeField(auto_now_add=True, verbose_name='爬取时间')),
                ('update_time', models.DateTimeField(null=True, verbose_name='更新时间')),
                ('is_deleted', models.IntegerField(default=0, verbose_name='是否删除')),
            ],
            options={
                'unique_together': {('fund_code', 'manager_id')},
            },
        ),
        migrations.CreateModel(
            name='FundHistoricalNetWorth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_code', models.CharField(db_index=True, default='', max_length=20, verbose_name='基金代码')),
                ('current_unit_net_worth', models.FloatField(default=0, verbose_name='当前单位净值')),
                ('current_cumulative_net_worth', models.FloatField(default=0, verbose_name='当前累计净值')),
                ('daily', models.FloatField(default=0, verbose_name='日涨跌幅')),
                ('subscription_status', models.CharField(default='', max_length=20, null=True, verbose_name='申购状态')),
                ('redemption_status', models.CharField(default='', max_length=20, null=True, verbose_name='赎回状态')),
                ('dividend_distribution', models.CharField(default='', max_length=200, null=True, verbose_name='分红送配')),
                ('current_date', models.DateField(default='', verbose_name='当前日期')),
                ('insert_time', models.DateTimeField(auto_now_add=True, verbose_name='爬取时间')),
                ('update_time', models.DateTimeField(null=True, verbose_name='更新时间')),
                ('is_deleted', models.IntegerField(default=0, verbose_name='是否删除')),
            ],
            options={
                'unique_together': {('fund_code', 'current_date')},
            },
        ),
    ]