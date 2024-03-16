from urllib.error import URLError

import pandas as pd
import pydeck as pdk
from sqlalchemy import create_engine

import streamlit as st
from streamlit.hello.utils import show_code

engine = create_engine('postgresql://rds_psql:Drb3*rbd77@dwh-warehouse-staging.cp0ehit8u4cb.us-east-1.rds.amazonaws.com:5432/OperationManager')

d = pd.read_sql_query("""
select 
    r."ProviderName" as "Provider Name",
    r."ProviderId" as "Provider ID",
    r."Currency" as "Currency",
    SUM(CASE 
        WHEN o."Type" = 2000 /*WIN*/ THEN o."Amount" 
        ELSE 0 
        END) as "Win Sum Amount",
    SUM(CASE
            WHEN o."Type" = 1000 /*BET*/ THEN o."Amount"
            ELSE 0
        END) as "Bet Sum Amount",
    '0' as "GGR",
    SUM(CASE
            WHEN o."Type" = 1001 /*BONUS BET*/ THEN o."Amount"
            ELSE 0
        END) as "Bonus Bet Sum Amount",
    SUM(CASE
            WHEN o."Type" = 2001 /*BONUS WIN*/ THEN o."Amount"
            ELSE 0
        END) as "Bonus Win Sum Amount"
from "Operations" o
left join "Rounds" r ON o."RoundId"=r."Id"
group by 
    r."ProviderName",
    r."ProviderId",
    r."Currency"
                      """, con=engine)
st.dataframe(d)