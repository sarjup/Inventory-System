@app.route('/api/login', methods = ['POST'])
def login():
    admin = AdminApi.login_admin(request)
    # print '=='*50
    # print admin
    if admin:
        session['username'] = request.form['uname']
        # print session.get('username')
        session['logged_in'] = True

    else:
        flash('Username or Password is incorrect')
    return redirect(url_for('index'))

@app.route('/api/logout', methods = ['GET'])
def logout():
    if session.get('logged_in'):
        session.pop('username',None)
        session['logged_in'] = False
    return redirect(url_for('index'))

