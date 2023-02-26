import pandas as pd
import geopandas as gpd
import plotly.express.colors as colors
import plotly.express as px
import os

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
FILES = "files"

#ALL_DF_PATH = os.path.join(CURRENT_PATH, FILES, "Bobs_dash_df.csv")
PRODUCT_SALES_12_PATH = os.path.join(CURRENT_PATH, FILES, "sales_12.csv")
PRODUCT_SALES_6_PATH = os.path.join(CURRENT_PATH, FILES, "sales_6.csv")
PRODUCT_SALES_3_PATH = os.path.join(CURRENT_PATH, FILES, "sales_3.csv")
SALES_REGION_PATH = os.path.join(CURRENT_PATH, FILES, "all_sales_region.csv")
ACTIVE_PER_REGION_PATH = os.path.join(CURRENT_PATH, FILES, "active_per_region.csv")
GDF_PATH = os.path.join(CURRENT_PATH, FILES, "Spain_regions.geojson")

apr = pd.read_csv(ACTIVE_PER_REGION_PATH)
gdf = gpd.read_file(GDF_PATH)
#df_bob = pd.read_csv(ALL_DF_PATH)
asr = pd.read_csv(SALES_REGION_PATH)
prod_sales_12 = pd.read_csv(PRODUCT_SALES_12_PATH)
prod_sales_6 = pd.read_csv(PRODUCT_SALES_6_PATH)
prod_sales_3 = pd.read_csv(PRODUCT_SALES_3_PATH)
df_bob = pd.read_csv("https://storage.googleapis.com/easymoneybobsdata/Bobs_dash_df.csv")

#apr = pd.read_csv("https://github.com/shogoBCN/pub_data/blob/main/active_per_region.csv?raw=true")
#gdf = gpd.read_file("https://github.com/shogoBCN/pub_data/blob/main/Spain_regions.geojson?raw=true")
#asr = pd.read_csv("https://github.com/shogoBCN/pub_data/blob/main/all_sales_region.csv?raw=true")
#prod_sales_12 = pd.read_csv("https://github.com/shogoBCN/pub_data/blob/main/sales_12.csv?raw=true")
#prod_sales_6 = pd.read_csv("https://github.com/shogoBCN/pub_data/blob/main/sales_6.csv?raw=true")
#prod_sales_3 = pd.read_csv("https://github.com/shogoBCN/pub_data/blob/main/sales_3.csv?raw=true")

table_dist_dict = [ {"label": item, "value": item} for item in ["All Users", "New Users", "Stock Users"] ]
region_dict = [{"label": region, 'value': region} for region in asr["region"].unique()]
products = ["short_term_deposit", "loans", "mortgage", "funds","securities", "long_term_deposit", "credit_card", "pension_plan", "payroll_account", "emc_account", "debit_card", "em_acount"]


gdf_fig = px.choropleth_mapbox(
    gdf, 
    geojson = gdf.geometry, 
    locations = gdf.index,
    color_continuous_scale = colors.sequential.Greens,
    color = "total_customers",
    mapbox_style = "carto-positron",
    zoom = 4, 
    center = {"lat": 40.416775, "lon": -3.7037},
    opacity = 0.45,
    labels = {'value':'Value'},
    height = 250)

layout = dict(
    margin = dict(l = 0, r = 0, t = 0, b = 0))

gdf_fig.update_layout(layout)



