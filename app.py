from flask import Flask, render_template, request, flash
from send_mail import send_mail
app = Flask(__name__) 
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
def topsis(dataFile, weights, impacts, resFile = 'result.csv') :
  import pandas as pd
  import numpy as np
  import sys
  w = list(int(i) for i in weights.split(','))
  im = list(i for i in impacts.split(','))
  if(len(w) != len(im)) :
    raise Exception('Number of elements in Weights and Impacts should be same')
  try:
    data = pd.read_csv(dataFile)
  except FileNotFoundError:
    raise Exception('File not Found')
  else :
    df = data.iloc[:, 1 :].values
    m = len(data)
    n = len(data.columns) - 1
    if(n < 3):
      raise Exception('Less than 3 Columns')
    rss = []
    for j in range(0, n):
      s = 0
      for i in range(0, m):
        s += np.square(df[i, j])
      rss.append(np.sqrt(s))
    for j in range(0, n):
      df[:, j] /= rss[j]
      df[:, j] *= w[j]
    best = []
    worst = []
    for j in range(0, n):
      if(im[j] == '+'): 
        best.append(max(df[:, j]))
        worst.append(min(df[:, j]))
      elif(im[j] == '-'):
        best.append(min(df[:, j]))
        worst.append(max(df[:, j]))
      else:
        print('Signs in Impact can be either + or - only')
        sys.exit(0)
    ebest = []
    eworst = []
    for i in range(0, m):
      ssdb = 0
      ssdw = 0
      for j in range(0, n):
        ssdb += np.square(df[i, j] - best[j])
        ssdw += np.square(df[i, j] - worst[j])
      rssdb = np.sqrt(ssdb)
      rssdw = np.sqrt(ssdw)
      ebest.append(rssdb)
      eworst.append(rssdw)
    p = []
    for i in range(0, m):
      measure = eworst[i] / (eworst[i] + ebest[i])
      p.append(measure * 100)
    data['Topsis Score'] = p
    data['Rank'] = data['Topsis Score'].rank(ascending = False)
    # print(data)
    # data.to_csv(resFile)
    return(data)
@app.route("/", methods = ('GET', 'POST'))
def hello_world():
    if request.method  == "POST":
        file = request.files['file']
        weights = request.form['weights']
        impacts = request.form['impacts']
        email_id = request.form['email_id']
        file_name = 'data.csv'
        file.save(file_name)
        try:
            data = topsis(file_name, weights, impacts)
        except Exception as e:
            flash(e)
            return render_template('index.html')
        send_mail(email_id, data.to_html())
        return data.to_html()
    return render_template('index.html')