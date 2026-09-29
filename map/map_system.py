import urllib.parse
import webbrowser

print("=========================================")
print("  🚀 MAP INTERACTIVE SYSTEM BOOTING...  ")
print("=========================================")

# Get starting and ending locations
start = input("Type Starting City (e.g. Bengaluru) and hit Enter: ").strip()
end = input("Type Ending City (e.g. Mumbai) and hit Enter: ").strip()

if start and end:
    src_clean = urllib.parse.quote(start)
    dst_clean = urllib.parse.quote(end)

    # Create Google Maps directions URL
    url = f"https://www.google.com/maps/dir/?api=1&origin={src_clean}&destination={dst_clean}"

    print("\n🔗 Attempting to open Google Maps...")
    print(f"🌍 Generated Target: {url}")

    # Open the URL in the default browser
    webbrowser.open(url)

    print("\n✅ Google Maps opened in your browser!")

else:
    print("❌ Values cannot be blank.")