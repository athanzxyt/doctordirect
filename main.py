from flask import Flask, render_template, request
import doctorOutput, doctorReturn
import os
print(os.path.abspath(os.getcwd()))
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
   input = request.form.to_dict()
   # print(input['symptoms'])
   illness, doctor = doctorOutput.outputDisease(input['symptoms'])
   doctorString = doctorReturn.getDoctor('va', 'vienna', doctor)
   # illness += '\n'
   print(doctorString)
   return render_template('result.html', disease = illness, type = doctor, name = doctorString)

@app.route('/hello')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()