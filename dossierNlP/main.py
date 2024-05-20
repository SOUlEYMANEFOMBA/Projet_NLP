import typer
from webscraping import WebScraping
app=typer.Typer()
@app.command()

def main():
    url = "https://api.indeed.com/ads/apisearch"
    result=WebScraping(url).jobsearch()
    print(result)

if __name__=="__main__":
    main()