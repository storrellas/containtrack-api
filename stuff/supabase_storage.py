import os
from supabase import create_client, Client


if __name__ == "__main__":
  try:
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    response = supabase.storage.list_buckets()
    print("repsonse", response)

    with open("./doc/sample.png", "rb") as f:
        supabase.storage.from_("pictures").upload(
            "sample.png",
            f.read(),
            file_options={"content-type": "image/png"}
        )

    print("response", response)
  except Exception as e:
    print("error", e)

