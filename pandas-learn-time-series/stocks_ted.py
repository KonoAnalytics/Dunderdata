''' Create a simple stocks correlation dashboard.
Choose stocks to compare in the drop down widgets, and make selections
on the plots to update the summary and histograms accordingly.
.. note::
    Running this example requires downloading sample data. See
    the included `README`_ for more information.
Use the ``bokeh serve`` command to run the example by executing:
    bokeh serve stocks
at your command prompt. Then navigate to the URL
    http://localhost:5006/stocks
.. _README: https://github.com/bokeh/bokeh/blob/master/examples/app/stocks/README.md
'''
from functools import lru_cache
from os.path import dirname, join

import pandas as pd
from pandas_datareader.data import DataReader
import numpy as np

from bokeh.io import curdoc
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import PreText, Select,TextInput 
from bokeh.plotting import figure
from bokeh.charts import Histogram

DATA_DIR = join(dirname(__file__), 'daily')

@lru_cache()
def get_web_prices(ticker):
    return DataReader(ticker, 'google')

# set up widgets

stats = PreText(text='', width=500)
text_ticker = TextInput()

# set up plots

source = ColumnDataSource(data=dict(Date=[], Close=[]))
source_gain = ColumnDataSource(data=dict(Date=[], Gain=[]))
source_stock = ColumnDataSource(data=dict(hist=[], bottom=[], left=[], right=[]))
tools = 'pan,wheel_zoom,xbox_select,reset'

ts1 = figure(plot_width=900, plot_height=200, tools=tools, x_axis_type='datetime', active_drag="xbox_select")
ts1.line('Date', 'Close', source=source)

ts2 = figure(plot_width=900, plot_height=200, tools=tools, x_axis_type='datetime', active_drag="xbox_select")
ts2.line('Date', 'Gain', source=source_gain)

hist = figure(plot_width=300, plot_height=200, tools=tools, active_drag="xbox_select")
hist.quad(top='hist', bottom=0, left='left', right='right', 
        fill_color="#036564", line_color="#033649", source=source_stock)

# set up callbacks

def text_ticker_change(attrname, old, new):
    df = get_web_prices(new)
    hist, edges = np.histogram(df.Close, density=True, bins=20)
    df_new = pd.DataFrame({'hist':hist, 'left':edges[:-1], 'right':edges[1:]})
    source_stock.data = source_stock.from_df(df_new)
    df_prices = df['Close'].reset_index()
    source.data = source.from_df(df_prices)
    df_gain = one_week_predict(df['Close'])
    df_gain_final = df_gain.rename('Gain').reset_index()
    source_gain.data = source_gain.from_df(df_gain_final)
    
def one_week_predict(stock):
    model = stock.resample('W-FRI').agg(lambda x: 1 if x[-1] - x[0] > 0 else -1)
    model = model.tshift(1)[:-1]
    actual = stock.resample('W-FRI').agg(lambda x: (x[-1] - x[0]) / x[-1])
    actual = actual[1:]
    df = pd.DataFrame({'actual':actual, 'model':model})
    df_gain = df.apply(lambda x: 1 + x['actual'] if x['model'] == 1 else 1 / (1 + x['actual']), axis=1)
    df_gain = df_gain.cumprod()
    return df_gain


text_ticker.on_change('value', text_ticker_change)

# def selection_change(attrname, old, new):
#     t1, t2 = ticker1.value, ticker2.value
#     data = get_data(t1, t2)
#     selected = source.selected['1d']['indices']
#     if selected:
#         data = data.iloc[selected, :]
#     update_stats(data, t1, t2)

# source.on_change('selected', selection_change)

# set up layout
widgets = column(text_ticker, stats)
main_row = row(hist, widgets)
series = column(ts1, ts2)
layout = column(main_row, series)

curdoc().add_root(layout)
curdoc().title = "Stocks"