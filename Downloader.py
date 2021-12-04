import json
import math
import random
import requests  # pip3 install requests
import mimetypes

# authorization token in request header message (xhr type)
token = ''
channelID = '854214724169236483'

def retrieve_msg(channelid):
    headers = {
        'authorization': token
    }
    r = requests.get(
        f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers
    )
    data = json.loads(r.text)
    for value in data:
        #print(json.dumps(value, indent=4))
        try:
            if len(value['attachments']) == 1:
                print(value['attachments'][0]['url'])
                print(
                    f"Author: {value['author']['username']}#{value['author']['discriminator']} MEDIA")
                print(
                    f"File size: {convert_size(int(value['attachments'][0]['size']))}")
                var_name = random.randint(0, 500000)
                download(value['attachments'][0]['url'], str(
                    var_name)+value['attachments'][0]['filename'])
            elif len(value['attachments']) >= 2:
                for index in range(len(value['attachments'])):
                    print(value['attachments'][index]['url'])
                    print(
                        f"Author: {value['author']['username']}#{value['author']['discriminator']} MEDIA+")
                    print(
                        f"File size: {convert_size(int(value['attachments'][index]['size']))}")
                    var_name = random.randint(0, 500000)
                    download(value['attachments'][index]['url'], str(
                        var_name)+value['attachments'][index]['filename'])
            elif len(value['embeds']) == 1:
                if "image" in value['embeds'][0]:
                    print(value['embeds'][0]['image']['url'])
                    print(
                        f"Author: {value['author']['username']}#{value['author']['discriminator']} EMBEDS image")
                    var_name = random.randint(0, 500000)
                    download(value['embeds'][0]['image']['url'], str(
                        var_name)+Get_Name(value['embeds'][0]['image']['url']))
                elif "thumbnail" in value['embeds'][0]:
                    print(value['embeds'][0]['thumbnail']['url'])
                    print(
                        f"Author: {value['author']['username']}#{value['author']['discriminator']} EMBEDS thumbnail url")
                    var_name = random.randint(0, 500000)
                    download(value['embeds'][0]['thumbnail']['url'], str(
                        var_name)+Get_Name(value['embeds'][0]['thumbnail']['url']))
                elif "thumbnail" in value['embeds'][0]:
                    print(value['embeds'][0]['thumbnail']['proxy_url'])
                    print(
                        f"Author: {value['author']['username']}#{value['author']['discriminator']} EMBEDS thumbnail proxy_url")
                    var_name = random.randint(0, 500000)
                    download(value['embeds'][0]['thumbnail']['proxy_url'], str(
                        var_name)+Get_Name(value['embeds'][0]['thumbnail']['proxy_url']))
                else:
                    pass
            elif len(value['embeds']) == 1:
                print(value['embeds'][0]['url'])
                print(
                    f"Author: {value['author']['username']}#{value['author']['discriminator']} EMBEDS")
                var_name = random.randint(0, 500000)
                download(value['embeds'][0]['url'], str(var_name) +
                         Get_Name(value['embeds'][0]['url']))
            elif len(value['embeds']) >= 2:
                for blap in range(len(value['embeds'])):
                    print(value['embeds'][blap]['url'])
                    print(
                        f"Author: {value['author']['username']}#{value['author']['discriminator']} EMBEDS+")
                    var_name = random.randint(0, 500000)
                    download(value['embeds'][blap]['url'], str(
                        var_name)+Get_Name(value['embeds'][blap]['url']))
            else:
                pass
        except:
            pass


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def download(url, name):
    response = requests.get(url)
    file = open(name, "wb")
    file.write(response.content)
    file.close()


def Get_Name(url):
    try:
        response = requests.get(url)
        content_type = response.headers['content-type']
        extension = mimetypes.guess_extension(content_type)
        final_name = response.headers['Content-Length'] + extension
        return final_name
    except:
        pass


retrieve_msg(channelID)
