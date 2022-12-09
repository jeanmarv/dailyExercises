def domain_name(url):
    # words = ""
    # if "//" in url and "www." not in url:
    #     words = url.split('//')
    #     words = words[1].split('.')
    #     return words[0]
    # if "//" in url and "www." in url:
    #     words = url.split('//')
    #     words = words[1].split('.')
    #     return words[1]
    # else: 
    #     words = url.split('.')
    #     return words[1]
    return url.split("//")[-1].split("www.")[-1].split('.')[0]

print(domain_name("http://www.github.com/carbonfive/raygun"))