import sys
import pkg_resources
import pandas as pd
import numpy as np
import seaborn as sns
import plotly
import soccerdata

matplotlib_version = pkg_resources.get_distribution("matplotlib").version
soccerdata_version = pkg_resources.get_distribution("soccerdata").version

print(f"Python version: {sys.version}")
print(f"Matplotlib version: {matplotlib_version}")
print(f"Pandas version: {pd.__version__}")
print(f"NumPy version: {np.__version__}")
print(f"Seaborn version: {sns.__version__}")
print(f"Plotly version: {plotly.__version__}")
print(f"Soccerdata version: {soccerdata_version}")
