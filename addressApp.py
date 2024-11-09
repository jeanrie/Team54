import requests

def get_ip_info(api_url):
    """Fetch data from the given API URL and return as JSON."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving IP information: {e}")
        return None

def display_ip_info(data):
    """Display the retrieved IP address information."""
    if data:
        print("\n=== Public IP Address Information ===")
        print(f"IP Address: {data.get('ip')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country_name', 'N/A')} ({data.get('country', 'N/A')})")
        print(f"Postal Code: {data.get('postal', 'N/A')}")
        print(f"Latitude: {data.get('latitude', 'N/A')}, Longitude: {data.get('longitude', 'N/A')}")
        print(f"ISP: {data.get('org', 'N/A')}")
        print(f"Autonomous System Number (ASN): {data.get('asn', 'N/A')}")
    else:
        print("No data to display.")

def main():
    
    user_input = input("Do you want to retrieve your IP address details? (yes/no): ").strip().lower()
    if user_input not in ['yes', 'y']:
        print("Exiting the application.")
        return
    
    print("\nFetching IPv4 Address...")
    ipv4_data = get_ip_info('https://api.ipify.org?format=json')
    if ipv4_data:
        ipv4_address = ipv4_data.get('ip')
        print(f"\nPublic IPv4 address: {ipv4_address}")

    print("\nFetching IPv6 Address...")
    ipv6_data = get_ip_info('https://api64.ipify.org?format=json')
    if ipv6_data:
        ipv6_address = ipv6_data.get('ip')
        print(f"\nPublic IPv6 address: {ipv6_address}")

    # Fetch additional details using ipapi.co for the IPv4 address
    if ipv4_data:
        ip_details = get_ip_info(f"https://ipapi.co/{ipv4_data['ip']}/json/")
        display_ip_info(ip_details)

if __name__ == "__main__":
    main()
