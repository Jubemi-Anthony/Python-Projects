import urllib.request as urllib


print("This is a site connectivity checker program.")
url = input("Input the url of the site you want to check: ")

def main(url):
    print("Checking connectivity...")

    response = urllib.urlopen(url)
    print(f"Connected to {url} successfully")

    myfile = open('site.txt', 'w')
    myfile.write(f'{response.read()}')
    myfile.close()
    print(f"The response code was {response.getcode()}")
    print('DONE...')

main(url)


"""

headers = response.info()
print("Headers:")
print(headers)
response.geturl(): Returns the URL of the resource retrieved, which might be different from the original URL if there were redirects.

final_url = response.geturl()
print("Final URL:")
print(final_url)
response.getheaders(): Returns a list of (header, value) tuples.

all_headers = response.getheaders()
print("All Headers:")
print(all_headers)
response.read(): Reads and returns the content of the response.

content = response.read()
print("Content:")
print(content)
response.getheader(header): Returns the value of a specific header.

content_type = response.getheader("Content-Type")
print("Content-Type:")
print(content_type)
"""