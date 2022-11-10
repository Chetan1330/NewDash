from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
# from pymongo import MongoClient


# from binance.client import Client
# import configparser

# # Loading keys from config file
# config = configparser.ConfigParser()
# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(THIS_FOLDER, 'secret.cfg')
# config.read_file(open('secret.cfg'))
# test_api_key = config.get('BINANCE', 'TEST_API_KEY')
# test_secret_key = config.get('BINANCE', 'TEST_SECRET_KEY')

# client = Client(test_api_key, test_secret_key)

# client.API_URL = 'https://testnet.binance.vision/api'  # To change endpoint URL for test account

# # info = client.get_account()  # Getting account info
# # print(info)

# BTC = client.get_asset_balance(asset='BTC')
# print(BTC['free'])

# ETH = client.get_asset_balance(asset='ETH')
# print(ETH['free'])

# BNB = client.get_asset_balance(asset='BNB')
# print(BNB['free'])

# USDT = client.get_asset_balance(asset='USDT')
# print(USDT['free'])

# btc_val = [45525.0, 37650.0, 31793.4, 19926.6, 23303.4, 21707.1]
# months = ['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']

# # Making Connection
# myclient = MongoClient("mongodb://localhost:27017/")

# # database
# db = myclient["GFG"]

# # Created or Switched to collection
# Collection = db["data"]

# # Create Lists of Data
# start_year = []
# Year = []
# intensity = []
# Relevance = []

# y2016 = []
# y2017 = []
# y2018 = []
# y2019 = []
# y2020 = []
# y2021 = []
# y2022 = []
# y2025 = []
# y2028 = []
# y2030 = []
# y2035 = []
# y2040 = []
# y2050 = []
# trialintensity = []

# ## For Getting All Data:

# # allintensity = []
# # allLikelihood = []
# # allRelevance = []
# # startYear = []
# # endYear = []
# allcountry = []
# allTopics = []
# allRegion = []
# alldata = []
# i = 1
# for y in Collection.find():
#     if y['start_year'] != '' and y['intensity'] != '':
#         # intensity.append(y['intensity'])
#         start_year.append([y['start_year'], y['intensity'], y['relevance']])
#     if y['country'] != '' and y['topic'] != '':
#         allcountry.append(y['country'])
#         allTopics.append(y['topic'])
#         allRegion.append(y['region'])
#         alldata.append([i, y['country'], y['topic'], y['region'], y['intensity'],y['likelihood'], y['relevance']])
#         i += 1

#     ## For getting All Data:
#     # allintensity.append(y['intensity'])
#     # allLikelihood.append(y['likelihood'])
#     # allRelevance.append(y['relevance'])
#     # startYear.append(y['start_year'])
#     # endYear.append(y['end_year'])
#     # allcountry.append(y['country'])
#     # allTopics.append(y['topic'])
#     # allRegion.append(y['region'])

# for data in sorted(start_year):
#     # print(data[1])
#     Year.append(data[0])
#     intensity.append(data[1])
#     Relevance.append(data[2])

# for y in Collection.find():
#     if y['start_year'] == 2016 and y['intensity'] != '' and y['relevance'] != '':
#         y2016.append([y['intensity'], y['relevance'], y['likelihood']])
#     if y['start_year'] == 2017 and y['intensity'] != '' and y['relevance'] != '':
#         y2017.append([y['intensity'], y['relevance'], y['likelihood']])
#     if y['start_year'] == 2018 and y['intensity'] != '' and y['relevance'] != '':
#         y2018.append([y['intensity'], y['relevance'], y['likelihood']])
#     if y['start_year'] == 2019 and y['intensity'] != '' and y['relevance'] != '':
#         y2019.append([y['intensity'], y['relevance'], y['likelihood']])
#     if y['start_year'] == 2020 and y['intensity'] != '' and y['relevance'] != '':
#         y2020.append([y['intensity'], y['relevance'], y['likelihood']])
#     if y['start_year'] == 2021 and y['intensity'] != '' and y['relevance'] != '':
#         y2021.append([y['intensity'], y['relevance'], y['likelihood']])
#     if y['start_year'] == 2022 and y['intensity'] != '' and y['relevance'] != '':
#         y2022.append([y['intensity'], y['relevance'], y['likelihood']])
#     if y['start_year'] == 2025 and y['intensity'] != '' and y['relevance'] != '':
#         y2025.append([y['intensity'], y['relevance'], y['likelihood']])
#     if y['start_year'] == 2028 and y['intensity'] != '' and y['relevance'] != '':
#         y2028.append([y['intensity'], y['relevance'], y['likelihood']])
#     if y['start_year'] == 2030 and y['intensity'] != '' and y['relevance'] != '':
#         y2030.append([y['intensity'], y['relevance'], y['likelihood']])
#     if y['start_year'] == 2035 and y['intensity'] != '' and y['relevance'] != '':
#         y2035.append([y['intensity'], y['relevance'], y['likelihood']])
#     if y['start_year'] == 2040 and y['intensity'] != '' and y['relevance'] != '':
#         y2040.append([y['intensity'], y['relevance'], y['likelihood']])
#     if y['start_year'] == 2050 and y['intensity'] != '' and y['relevance'] != '':
#         y2050.append([y['intensity'], y['relevance'], y['likelihood']])

# # print(len(start_year))
# # print(len(Year))
# # print(len(intensity))
# # print(len(Relevance))
# #print(sorted(set(Year))) #Sorted Year list
# # print(max(y2016), max(y2017), max(y2018), max(y2019), max(y2020), max(y2021), max(y2022),
# #       max(y2025), max(y2028), max(y2030), max(y2035), max(y2040), max(y2050))
# l_inten = [max(y2016), max(y2017), max(y2018), max(y2019), max(y2020), max(y2021), max(y2022),
#       max(y2025), max(y2028), max(y2030), max(y2035), max(y2040), max(y2050)]
# # print(l_inten)
# inten = []
# rele = []
# likehood = []
# for i in range(len(l_inten)):
#     inten.append(l_inten[i][0])
#     rele.append(l_inten[i][1])
#     likehood.append(l_inten[i][2])
# # print(inten)
# # print(rele)
# # print(likehood)
# # print(set(allcountry))
# # print(allcountry)

# # print(len(allTopics))
# # print(len(allRegion))
# # print(len(allcountry))

@login_required(login_url="/login/")
def index(request):
    # context = {'segment': 'index'}
    # 'ETH': ETH['free']
    context = {'segment': 'index'}
    # 'allintensity': allintensity

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
