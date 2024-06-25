from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")

def hello_world():

    return "<p>Hello, World!</p>"



@app.route("/formulario",methods=["GET","POST"])

def formulario():

    if request.method == "POST":

        A = request.form["datoA"]

        B = request.form["datoB"]
        
        C = request.form["datoC"]

        #print(int(A)+int(B))

        a=int(A)
        b=int(B)
        c=int(C)

        coe1= ((-b)+(((b**2)-(4*a*c))**(1/2)))/(2*a)
        coe2 = ((-b)-(((b**2)-(4*a*c))**(1/2)))/(2*a)
        

        return render_template("formulario.html",C=C,A=A,B=B,coe1=coe1,coe2=coe2)

        

    return render_template("formulario.html")



if __name__=="__main__":

    app.run(debug=True)


