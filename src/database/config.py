import streamlit as st
from supabase import Client, create_client

SUPABASE_URL = st.secrets.get("SUPABASE_URL") or st.secrets.get("supabase_url")
SUPABASE_KEY = st.secrets.get("SUPABASE_KEY") or st.secrets.get("supabase_key")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError(
        "Supabase credentials are missing. Add SUPABASE_URL and SUPABASE_KEY to .streamlit/secrets.toml."
    )

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
