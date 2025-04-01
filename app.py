from flask import Flask,request, render_template,url_for,redirect
from qrcode import QRCode
import io,base64

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        data=request.form['data']
        qr=QRCode()
        qr.add_data(data)
        qr.make(fit=True)
        img=qr.make_image()
        buffered=io.BytesIO()
        img.save(buffered,format="PNG")
        img_str=base64.b64encode(buffered.getvalue()).decode('utf-8')


        return redirect(url_for('qrgen',img_str=img_str))
    return render_template('index.html')

@app.route('/qrgen')
def qrgen():
    img_str=request.args.get('img_str')
    return render_template('qr.html',img_str=img_str)
app.run(host="0.0.0.0", post="80" ,debug=True)    
