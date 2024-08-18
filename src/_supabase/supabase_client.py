from supabase import create_client, Client
from src.core.config import settings

url: str = settings.supabase_url
key: str = settings.supabase_key
supabase_client: Client = create_client(url, key)
