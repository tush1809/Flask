from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)

@app.route('/')
def welcome ():
    return render_template('index.html')

@app.route('/Success/<int:score>')
def Success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',result=res)


@app.route('/Fail/<int:score>')
def Fail(score):
    return "The Person has fail and the marks is"+ str(score)

@app.route('/result/<int:marks>')
def fail(marks):
    result=""
    if marks<50:
        result='Fail'
    else:
        result='Success'
    return redirect(url_for(result,score=marks))

@app.route('/submit',methods=['POST','GET'])
def Submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        english=float(request.form['english'])
        history=float(request.form['history'])
        total_score=(science+maths+english+history)/4
    res=""
    if total_score>=50:
        res="Success"
    else:
        res="Fail"
    return redirect(url_for(res,score=total_score))











if __name__=='__main__':
    app.run(debug=True)