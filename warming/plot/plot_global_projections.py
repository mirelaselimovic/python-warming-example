import matplotlib.pyplot as plt
import geopandas as gpd

class global_pro:

    def __init__(self):
        self._dataC02 = sum_global_projections.co2()
        self._dataCH4 = sum_global_projections.ch4()
        self._dataN20 = sum_global_projections.n2o()
        self.xaxis = sum_global_projections.xscale()
        )

    def show(self):
        """Opens a world map plot.

        The map shows the specified data, which also needs to be
        set with the `column` parameter.

        :param data: The data that will be shown on the world map.
        :type data: pandas.core.series.Series
        :param column: The index of the data to show.
        :type column: str
        """

        plt.plot(_xaxis, _dataC02)
        plt.plot(_xaxis, _dataCH4)
        plt.plot(_xaxis, _dataN20)
        plt.show()