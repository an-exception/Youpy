# Made by Shrey
import os, platform, pytube

(os.system('cls') if platform.system() == 'Windows' else os.system('clear'))
try: os.system('color E')
except: pass

print('#   #   #####   #   #   #####   #   #')
print(' # #    #   #   #   #   #   #    # # ')
print('  #     #   #   #   #   #####     #  ')
print('  #     #   #   #   #   #         #  ')
print('  #     #####   #####   #         #  ')
print('\n' + 'Youpy is a super useful tool which allows you to download youtube video. Any one of them, to make your life so much easier. We all had the times when we want to download a music video but youtube asks for the damn premium, or we just want to download a simple clip or meme, but no worries now we have Youpy! \n\n')

while True:
    urls = input('Enter the url(s) of the video you want to install (Saperate more then one url with a space):-\n').strip()
    urls = urls.split(' ')

    print('\n' + 'Download Queue:-')

    queue = []
    for i in urls:
        if i.startswith('https://www.youtube.com/') or i.startswith('https://youtube.com/'):
            print(f'- {i}')
            queue.append(i)
        else:
            print(f'- {i} [URL must start with https://youtube.com/...] [Removed]')
    
    print('\n' + 'Processing Tasks:-')
    for i, url in enumerate(queue):
        print('\n' + f'[{i + 1}] {url}')

        try: 
            yt = pytube.YouTube(url)
        except:
            print('Failed to connect with current URL!')
            continue

        print(f'{pytube.Channel(yt.channel_url).channel_name} - {yt.title}')
        print(f'Uploaded On - {yt.publish_date}')
        print(f'View Count - {yt.views}')
        print(f'Rating - {yt.rating}')
        print(f'Thumbnail - {yt.thumbnail_url}' + '\n')

        print('Attempting to download video in highest resolution (Might take some time)...')
        try:
            yt.streams.get_highest_resolution().download('./')
            print(f'Video successfully downloaded in the current working directory! (In {os.getcwd()}) \n')
        except:
            print('Unable to download video, trying in normal resolution...')
            try:
                yt.streams.first().download('./')
                print(f'Video successfully downloaded in normal resolution! (In {os.getcwd()}) \n')
            except:
                print('Unable to download video, trying in lowest resolution...')
                try:
                    yt.streams.get_lowest_resolution().download('./')
                    print(f'Video successfully downloaded in lowest resolution! (In {os.getcwd()}) \n')
                except:
                    print('We just cant download this, the vid is kinda sus. \n')
