def save_abstracts(year):
    '''
    I used the E-utililities https://www.ncbi.nlm.nih.gov/books/NBK25499/
    In the first part it makes a query and then gets the count of the results and 
    the 'MCID' for that query. '&retmax' is the max results to return 
    In the second part the MCID is used to access the query results, but only 10,000
    at a time, so '&retstart' is used to change the start from 0 to 10,000 to 20,000 ect.
    Each 10,000 from each year are saved as a seperate file.
    '''
    year = str(year)
    base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
    query = '"Cell Physiological Phenomena"[Mesh]+AND+english[Filt]+\
AND+human[Mesh]+AND+"has abstract"[Filt]+AND+'+year+'[pdat]+AND+(signaling+OR+pathway)'
    url = base + 'esearch.fcgi?db=pubmed&term=' + query +'&retmax=100000'+'&usehistory=y'
    output = requests.get(url, headers = user_agent)
    page = output.text
    soup = BeautifulSoup(page, "lxml")
    count = soup.find('count').text
    MCID = soup.find('webenv').text
    
    for i in range(0,int(count),10000):
        print(i)
        url = base + "efetch.fcgi?db=pubmed&query_key=1&WebEnv=" + MCID
        url = url + "&rettype=abstract&retmode=text&retmax=100000&retstart="+str(i)
        output = requests.get(url, headers = user_agent)
        page = output.text
        soup = BeautifulSoup(page, "lxml")
        file_num = str(i)[0]
        with open('proj4_pubmed_'+year+'_'+file_num+'.pickle', 'wb') as write_file:
            pickle.dump(soup, write_file)

for i in range(1985,2020):
    year = str(i)
    print(year)
    save_abstracts(year)    