from scrapy.http import HtmlResponse
import os, csv, re, json



class DetailsData:
    allowed_domains = []
    start_urls = ['https://www.example.com']
    data = HtmlResponse("")
    output = "booktopia.csv"
    jobid = ""

    def __init__(self, file_name):

        self.path = 'D:\\pythonProject\\book_topia'
        self.output = self.path + f"\\{file_name}.csv"

        if not os.path.exists(self.output):
            with open(self.output, "w", newline="") as wd:
                wr = csv.writer(wd)
                wr.writerow(
                    ["Title of the Book","Author","Book type","Original Price","Discounted price","ISBN-10","Published Date","Publisher","No. of Pages"])




    def extract_data(self, response):
        # response = HtmlResponse(url="my HTML string", body=html_page, encoding='utf-8')
        #
        # raw_dict = {}
        # remarks_dict = {}
        # JOBID = self.jobid
        # ST_COUNTY = st_county
        dic_date = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
                    'September': 9, 'October': 10, 'November': 11, 'December': 12}

        title =response.xpath(f'//*[@id="ProductDetails_d-product-info__rehyy"]/div[3]/h1/text()|//*[@id="ProductDetails_d-product-info__rehyy"]/div[2]/h1/text()').get(default='').strip()
        if title=='':
            title='book not found'
        author = response.xpath(f'//*[@id="ProductDetails_d-product-info__rehyy"]/div[3]/p[1]/a/span/text()|//*[@id="ProductDetails_d-product-info__rehyy"]/div[2]/p[1]/a/span/text()').get(default='').strip()
        book_ype = response.xpath(f'//*[@id="BuyBox_product-version__uw1et"]/h3/text()').get(default='').strip()
        if book_ype=='':
            try:
                book_ype=response.xpath(f'//*[@id="ProductDetails_d-product-info__rehyy"]/div[3]/p[2]/text()|//*[@id="ProductDetails_d-product-info__rehyy"]/div[2]/p[2]/text()').get(
                    default='').strip().split()[0]
            except:
                book_ype=''
        rrp = response.xpath(f'//*[@id="BuyBox_product-version__uw1et"]/div[1]/div/div/div/p/span/text()').get(default='').strip()
        discount_price = response.xpath(f'//*[@id="BuyBox_product-version__uw1et"]/div[1]/div/div/p/text()|//*[@id="ProductDetails_d-product-info__rehyy"]/div[2]/button[2]/a/p[2]/text()').get(default='').strip()
        ISBN = response.xpath(f'//*[contains(text(),"ISBN-10")]/../text()').get(default='').strip()
        try:
            pub_date = response.xpath(f'//span[contains(text(),"Published")]/../text()').get(default='').strip().replace('th','')
            publisher=pub_date.split(' ')
            month=dic_date[publisher[1]]
            year=publisher[2]
            date=publisher[0].replace('st','').replace('nd','').replace('rd')
            published_date=year+'/'+str(month)+'/'+date
        except:
            published_date=''

        publisher = response.xpath(f'//span[contains(text(),"Publisher")]/../text()').get(default='').strip()
        Pages = response.xpath(f'//*[contains(text(),"Number of Pages")]/../text()').get(default='').strip()


        alldata = [title,author,book_ype,rrp,discount_price,ISBN,published_date,publisher,Pages]
        with open(self.output, "a", newline="") as wd:
            wr = csv.writer(wd)
            print(alldata)
            wr.writerow(alldata)



