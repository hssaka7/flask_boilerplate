from flask import Flask, render_template, request, Response
import random
test_app = Flask(__name__)

@test_app.route('/')
def getRandomData():
   context = {"title": "Data table test"}
   data = [{ 'id': i,
             'name': "test_name_{0}".format(random.randint(0,1000)),
             'phone': random.randint(2308,903234),
             'status': random.choice([True, False])
           } for i in range(0,10000)]

   context['data'] = data
   return render_template('table_example.html', **context)

if __name__ == "__main__":
    test_app.run(host ="localhost")