"""Fixes for CanESM5 model."""
from ..fix import Fix
import numpy as np


class Co2(Fix):
    """Fixes for co2."""
    def fix_metadata(self, cubes):
        """Correctly sets lat boundary to that of the other variables and corrects units.

        Parameters
        ----------
        cube : iris.cube.CubeList

        Returns
        -------
        iris.cube.Cube

        """
        cube = self.get_cube_from_list(cubes)
        metadata = cube.metadata
        cube *= 1.e-6
        cube.metadata = metadata
        cube.coord('latitude').bounds = [[-90.        , -86.57774751],
       [-86.57774751, -83.75702878],
       [-83.75702878, -80.95502019],
       [-80.95502019, -78.15834785],
       [-78.15834785, -75.36393858],
       [-75.36393858, -72.5707002 ],
       [-72.5707002 , -69.77814617],
       [-69.77814617, -66.98602671],
       [-66.98602671, -64.19420036],
       [-64.19420036, -61.40258094],
       [-61.40258094, -58.61111296],
       [-58.61111296, -55.81975904],
       [-55.81975904, -53.02849308],
       [-53.02849308, -50.23729628],
       [-50.23729628, -47.44615476],
       [-47.44615476, -44.65505801],
       [-44.65505801, -41.86399795],
       [-41.86399795, -39.07296823],
       [-39.07296823, -36.28196381],
       [-36.28196381, -33.49098058],
       [-33.49098058, -30.70001521],
       [-30.70001521, -27.9090649 ],
       [-27.9090649 , -25.11812731],
       [-25.11812731, -22.32720044],
       [-22.32720044, -19.53628258],
       [-19.53628258, -16.7453722 ],
       [-16.7453722 , -13.95446797],
       [-13.95446797, -11.16356869],
       [-11.16356869,  -8.37267325],
       [ -8.37267325,  -5.58178063],
       [ -5.58178063,  -2.79088986],
       [ -2.79088986,   0.        ],
       [  0.        ,   2.79088986],
       [  2.79088986,   5.58178063],
       [  5.58178063,   8.37267325],
       [  8.37267325,  11.16356869],
       [ 11.16356869,  13.95446797],
       [ 13.95446797,  16.7453722 ],
       [ 16.7453722 ,  19.53628258],
       [ 19.53628258,  22.32720044],
       [ 22.32720044,  25.11812731],
       [ 25.11812731,  27.9090649 ],
       [ 27.9090649 ,  30.70001521],
       [ 30.70001521,  33.49098058],
       [ 33.49098058,  36.28196381],
       [ 36.28196381,  39.07296823],
       [ 39.07296823,  41.86399795],
       [ 41.86399795,  44.65505801],
       [ 44.65505801,  47.44615476],
       [ 47.44615476,  50.23729628],
       [ 50.23729628,  53.02849308],
       [ 53.02849308,  55.81975904],
       [ 55.81975904,  58.61111296],
       [ 58.61111296,  61.40258094],
       [ 61.40258094,  64.19420036],
       [ 64.19420036,  66.98602671],
       [ 66.98602671,  69.77814617],
       [ 69.77814617,  72.5707002 ],
       [ 72.5707002 ,  75.36393858],
       [ 75.36393858,  78.15834785],
       [ 78.15834785,  80.95502019],
       [ 80.95502019,  83.75702878],
       [ 83.75702878,  86.57774751],
       [ 86.57774751,  90.        ]]
        return cubes

class Gpp(Fix):
    """Fixes for fgco2, land values set to 0 instead of masked."""

    def fix_data(self, cube):
        """
        Fix data.

        Parameters
        ----------
        cube: iris.cube.Cube

        Returns
        -------
        iris.cube.Cube

        """
        cube.data = np.ma.masked_where(cube.data==0, cube.data)
        return cube
