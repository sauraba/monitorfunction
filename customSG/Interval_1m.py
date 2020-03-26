import inspect
import logging
import datetime as dt
import math
from sqlalchemy.sql.sqltypes import TIMESTAMP,VARCHAR
import numpy as np
import pandas as pd

from iotfunctions.base import BaseTransformer
from iotfunctions import ui

logger = logging.getLogger(__name__)

# Specify the URL to your package here.
# This URL must be accessible via pip install

PACKAGE_URL = 'git+https://github.com/sauraba/monitorfunction.git@master'

class Interval_1min (BaseTransformer):

    def __init__(self, input_item, input_items_str,output_items):

        self.input_items = input_item
        self.input_items_str=input_items_str
        self.output_items = output_items
    def execute(self, df):
        df=df.copy()
        #df=pd.DataFrame(columns=[self.input_items[0],self.input_items_str[0],self.input_items_str[1]],dtype=np.dtype([('float','str','str')]))

        #=pd.DataFrame(columns=[self.input_items[0],self.input_items_str[0],self.input_items_str[1]])
        print (self.input_items_str)
        df[self.output_items[0]] = df.groupby([self.input_items_str[1], pd.to_datetime(df[self.input_items_str[0]].str[:16])])[self.input_item].mean()
        print (df)
        return df

    @classmethod
    def build_ui(cls):
        #define arguments that behave as function inputs
        inputs = []
        inputs.append(ui.UIMultiItem(
                name = 'input_items_str',
                datatype=str,
                description = "Data items adjust",
                output_item = 'output_items',
                is_output_datatype_derived = True)
                      )
        inputs.append(ui.UISingle(
                name = 'input_item',
                datatype=float)
                      )
        outputs = []
        return (inputs,outputs)
