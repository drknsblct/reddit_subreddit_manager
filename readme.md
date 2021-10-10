## Requirements

- Download the corresponding version of [ChromeDriver](https://chromedriver.chromium.org/downloads) that matches the
  version of your Chrome browser and add it to this folder.


- Install requirements.txt (`pip install -r /path/to/requirements.txt`)

## Before running the program

- Log in to your reddit account by using any desktop browser of your choice.


- Type or paste [reddit.com/subreddits](reddit.com/subreddits) on the address bar.


- Paste the following snippet on the address bar and press `Enter`:
  ```javascript
  javascript:$('body').replaceWith('<body>'+$('.subscription-box').find('li').find('a.title').map((_, d) => $(d).text()).get().join("<br>")+'</body>');javascript.void()
  ``` 
  ##### Code snippet was from [here](https://timvisee.com/blog/list-export-your-subreddits/).

- Copy the list of all the subreddits and users and paste it in `generate_urls.py` on the subs list.

> #### Follow these steps to mass add elements to list:
>
> Click on the left of the first element and then press `Ctrl` + `Alt` and drag mouse from left to right and then down to the end of list to select all elements.
>
> Add quotes (`" "` or `' '`)
>
> Click &#8594; key on keyboard
>
> Add `,`
>
> Delete comma on the right of last element

- Create file named `secrets.py` and add your username/password in variables with the same name. Use the reddit account you want to tranfer the subreddits!

### Disclaimer

- Use this program with **caution!** I'm not held responsible if your account gets banned.
