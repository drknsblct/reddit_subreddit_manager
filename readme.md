## Requirements

- Download the corresponding version of [ChromeDriver](https://chromedriver.chromium.org/downloads) that matches the
  version of your Chrome browser and add it to this folder.


- Install requirements.txt (`pip install -r /path/to/requirements.txt`)

## Before running the program

- Log in to your Reddit account by using any desktop browser of your choice. Log in to the account from which you want to transfer the subreddits!


- Type or paste [reddit.com/subreddits](https://www.reddit.com/subreddits) on the address bar.


- Paste the following [snippet from Tim Visee](https://timvisee.com/blog/list-export-your-subreddits/) on the address bar and press `Enter`:
  ```javascript
  javascript:$('body').replaceWith('<body>'+$('.subscription-box').find('li').find('a.title').map((_, d) => $(d).text()).get().join("<br>")+'</body>');javascript.void()
  ``` 

- Copy all and paste it in a text file named `subs.txt`. Add the text file to the same folder as the program.


- Create file named `secrets.py` and add your username/password in variables with the same name. Use the Reddit account in which the subreddits will be transfered!

### Disclaimer

- Use this program with **caution**, meaning don't spam the Reddit server with too many requests. I'm not held responsible if your account gets banned.
