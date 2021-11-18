import json
import requests  # pip install requests
import mimetypes

# authorization token in request header message (xhr type)
token = ''


def retrieve_msg(channelid):
    headers = {
        'authorization': token
    }
    r = requests.get(
        f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers
    )
    data = json.loads(r.text)
    for value in data:
        if len(value['attachments']) > 0:
            print(value['attachments'][0]['url'])
            print(
                f"Author: {value['author']['username']}#{value['author']['discriminator']}")
            download(value['attachments'][0]['url'],
                     value['attachments'][0]['filename'])
        elif len(value['embeds']) > 0:
            if "image" in value['embeds'][0]:
                print(
                    f"Author: {value['author']['username']}#{value['author']['discriminator']}")
                download(value['embeds'][0]['image']['url'],
                         Get_Name(value['embeds'][0]['image']['url']))
        elif len(value['embeds']) > 0:
            print(
                f"Author: {value['author']['username']}#{value['author']['discriminator']}")
            download(value['embeds'][0]['url'], Get_Name(
                value['embeds'][0]['url']))
        else:
            continue


def download(url, name):
    response = requests.get(url)
    file = open(name, "wb")
    file.write(response.content)
    file.close()


def Get_Name(url):
    response = requests.get(url)
    content_type = response.headers['content-type']
    extension = mimetypes.guess_extension(content_type)
    final_name = response.headers['Content-Length'] + extension
    return final_name


retrieve_msg('channel_ID')
