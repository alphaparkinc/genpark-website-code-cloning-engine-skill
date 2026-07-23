from client import WebsiteCodeCloningEngineClient

def main():
    client = WebsiteCodeCloningEngineClient()
    res = client.clone_site_structure("https://example.com/landing", "react")
    print("Generated Code:")
    print(res["generated_code"])
    print(f"Assets: {res['asset_links']}")

if __name__ == "__main__":
    main()
