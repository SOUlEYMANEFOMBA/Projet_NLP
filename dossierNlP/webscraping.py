import requests
from bs4 import BeautifulSoup
class WebScraping():

    def __init__(self,url):
        self.url= url
    
    def jobsearch(self):
        # URL de la recherche d'emploi Indeed pour les offres de data science
        url =self.url

        # Envoyer une requête GET à la page

        #creation d'un dictionnaire pour stocker les resultat
        result={}

        params = {
        'publisher': 'YOUR_PUBLISHER_ID',  # Remplacez par votre Publisher ID
        'q': 'data science',
        'l': 'San Francisco, CA',
        'sort': 'date',
        'radius': '25',
        'st': 'employer',
        'jt': 'fulltime',
        'start': '0',
        'limit': '10',
        'fromage': '7',
        'filter': '1',
        'latlong': '1',
        'co': 'us',
        'format': 'json',
        'v': '2'
    }

    # Envoyer une requête GET à l'API Indeed
        response = requests.get(url, params=params)
        print(response)
    # Vérifier si la requête a réussi
        if response.status_code == 200:
           data = response.json()
           for job in data.get('results', []):
                    title = job.get('jobtitle')
                    company = job.get('company')
                    location = job.get('formattedLocation')
                    summary = job.get('snippet')
                    # Afficher les informations extraites
                    result['Title']=title
                    result['Company']=company
                    result['Location']=location
                    result['Summary']=summary
                    result['Title']=title
                    print(f"Title: {title}")
                    print(f"Company: {company}")
                    print(f"Location: {location}")
                    print(f"Summary: {summary}")
                    print('-' * 40)
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
                  
        return result