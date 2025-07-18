import requests
url = input("Enter the webpage URL: ")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url, headers=headers)
print(response.text[:500])
import re
match = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE)
if match:
    title = match.group(1)
    with open("webpage_title.txt", "w", encoding='utf-8') as f:
        f.write("Title: " + title)
    print("✅ Title saved successfully!")
    print("Extracted Title:", title)
else:
    print("❌ Could not find the <title> tag.")
