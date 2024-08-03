# SteamStore
A web scraping project that scrapes the top 50 most selling games from the steam store website 
and displays it on the web in real time using Flask with Bootstrap and Scrapyrt (i.e. Client sends a request 
to ScrapyRT with spider name and URL, and in response, they get items collected by a spider visiting this URL).

## project setup

1. Install Anaconda from `https://www.anaconda.com/` and create a virtual environment.
2. Activate your virtual environment from the command line `conda activate {virtual env name}` or from the Anaconda GUI application.
3. Install scrapyrt: `pip install scrapyrt`
4. Install flask: `conda install flask -y`
5. `git clone` this project to your local machine and open it with your preferred IDE.
6. On your IDE, set up the python interpreter path to the `python.exe` file located in your anaconda virtual environment directory.
7. Change directory on the terminal to the web folder in this project `cd ./SteamStore/web`
8. Run `scrapyrt` on the terminal
9. Run `python .\app.py` on another instance of the terminal, then click on the link to the webpage

Note:
To run the spider locally without running the web app, after step 6, 
run `scrapy crawl bestsellers -o {file_name}.{json/csv}` on the terminal.





