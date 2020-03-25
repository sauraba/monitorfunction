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

    def __init__(self, inputs_items, output_item):

        self.inputs_items = inputs_items
        self.output_item = output_item
        super().__init__()
    def execute(self, df):
        df=pd.dataframe(columns=[self.inputs_items[0],self.inputs_items[1],self.inputs_items[2]])
        #df=pd.dataframe(output_items)
        df[self.output_item[0]] = df.groupby(['siteId', pd.to_datetime(df['Intervaldttm'].str[:16])])['HouseAir'].mean()
        return df

    @classmethod
    def build_ui(cls):
        #define arguments that behave as function inputs
        inputs = []
        inputs.append(ui.UIMultiItem(
                name = 'input_items',
                datatype=float,
                description = "Data items adjust",
                output_item = 'output_item',
                is_output_datatype_derived = True)
                      )

        outputs = []
        return (inputs,outputs)
