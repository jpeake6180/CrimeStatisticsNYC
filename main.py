import bottle
import json
import data

@bottle.route("/")
def serve_html():
  return bottle.static_file("index.html",root=".")

@bottle.route("/ajax.js")
def serve_ajax():
  return bottle.static_file("ajax.js",root=".")

@bottle.route("/arrest.js")
def serve_arrest():
    return bottle.static_file("arrest.js",root=".")

@bottle.get("/lineGraphData")
def serve_line_data():
  line_graph_data = data.line_data_gen()
  return json.dumps(line_graph_data)

@bottle.get("/pieChartData")
def serve_pie_data():
  pie_chart_data = data.pie_data_gen()
  return json.dumps(pie_chart_data)

@bottle.post("/barChartData")
def serve_bar_data():
  content = bottle.request.body.read().decode()
  content = json.loads(content)
  #content is a name of a borough
  bar_chart_data = data.bar_data_gen(content)
  return json.dumps(bar_chart_data)

import os.path
def load_data( ):
  csv_file = 'cache.csv'
  if not os.path.isfile(csv_file):
    url = 'https://data.cityofnewyork.us/resource/uip8-fykc.json?$limit=50000&$select=arrest_date,pd_desc,ofns_desc,arrest_boro,arrest_precinct,law_cat_cd,age_group,perp_sex,perp_race'
    info = data.retrieve_json(url)
    needed_keys = ['arrest_date','age_group','arrest_boro','pd_desc','law_cat_cd']
    for k in needed_keys:
    	info = data.clean_list(k, info)
    data.cache_writer(info, csv_file)

load_data()
bottle.run(host="0.0.0.0", port=8080)