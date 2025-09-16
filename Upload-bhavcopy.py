import requests
import zipfile
import io
import pandas as pd
import datetime as dt
import os

# ----------------------------
# Step 1: Get today's date
# ----------------------------
today = dt.date.today()
day = today.strftime("%d")
month = today.strftime("%b").upper()   # e.g. SEP
year = today.strftime("%Y")

# ----------------------------
# Step 2: URLs for Equity & FO bhavcopy (ZIP)
# ----------------------------
eq_url = f"https://www.nseindia.com/content/historical/EQUITIES/{year}/{month}/cm{day}{month}{year}bhav.csv.zip"
fo_url = f"https://www.nseindia.com/content/historical/DERIVATIVES/{year}/{month}/fo{day}{month}{year}bhav.csv.zip"

headers = {"User-Agent": "Mozilla/
