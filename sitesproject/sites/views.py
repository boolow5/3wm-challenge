from django.shortcuts import render
from django.db import connection
from sites.models import *

# Create your views here.
def index(request):
    '''
    index is the / page and /sites page view
    '''
    sites = Site.objects.all()
    context = {
      "sites": sites,
    }
    return render(request, "sites/index.html", context)

def site_detail(request, pk=None):
    '''
    site_detail is /site/pk page view
    '''
    site = Site.objects.get(pk=pk)
    items = Item.objects.filter(site__pk=pk)
    context = {
      "site": site,
      "items": items,
    }
    return render(request, "sites/details.html", context)

def summary(request):
    '''
    summary is the /summary page view
    '''
    site = Site.objects.raw('SELECT * FROM sites_site')
    cursor = connection.cursor()
    cursor.execute('''
    SELECT site.id, site.name, SUM(item.a_value) as a_value, SUM(item.b_value) as b_value
    FROM sites_item as item 
    INNER JOIN sites_site as site ON site.id = item.site_id
    GROUP BY item.site_id
    ORDER BY item.site_id DESC
    ''')
    items = []
    error = None
    for row in cursor.fetchall():
        if len(row) == 4:
          items.append({"site_id": row[0], "name": row[1] + " Site", "a_value": row[2], "b_value": row[3]})
        else:
          error = "{} found columns, expected 4 columns".format(len(row))
          print(error)
    context = {
      "site": site,
      "items": items,
    }
    return render(request, "sites/summary.html", context)

def summary_average(request):
    '''
    summary_average is the /summary-average page view
    '''
    site = Site.objects.raw('SELECT * FROM sites_site')
    cursor = connection.cursor()
    cursor.execute('''
    SELECT site.id, site.name, AVG(item.a_value) as a_value, AVG(item.b_value) as b_value
    FROM sites_item as item 
    INNER JOIN sites_site as site ON site.id = item.site_id
    GROUP BY item.site_id
    ORDER BY item.site_id DESC
    ''')
    items = []
    error = None
    for row in cursor.fetchall():
        if len(row) == 4:
          items.append({"site_id": row[0], "name": row[1] + " Site", "a_value": row[2], "b_value": row[3]})
        else:
          error = "{} found columns, expected 4 columns".format(len(row))
          print(error)
    context = {
      "site": site,
      "items": items,
    }
    return render(request, "sites/summary.html", context)