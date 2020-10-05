from flask import request, render_template, session, redirect, url_for
from project import app
from datetime import datetime
from werkzeug.utils import secure_filename
from project.com.vo.BlogVO import BlogVO
from project.com.dao.BlogDAO import BlogDAO
import os


@app.route('/loadBlog')
def loadBlog():
    try:
        if session['loginRole'] == 'admin':
            return render_template('admin/addBlog.html')
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')


@app.route('/insertBlog', methods=['POST'])
def insertBlog():
    # try:
        if session['loginRole'] == 'admin':
            blogVO = BlogVO()
            blogDAO = BlogDAO()
            UPLOAD_FOLDER = 'C:/project/admin/project/static/adminResources/blog'

            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

            file = request.files['blogFile']

            filename = secure_filename(file.filename)

            filepath = os.path.join(app.config['UPLOAD_FOLDER'])

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            blogVO.blogFilename = filename
            blogVO.blogFilepath = filepath
            blogVO.blogTitle = request.form['blogTitle']
            blogVO.blogDescription = request.form['blogDescription']
            blogVO.blogDate, blogVO.blogTime = str(datetime.now()).split(' ')
            blogVO.blogActiveStatus = 'active'

            blogDAO.insertBlog(blogVO)
            return render_template('admin/addBlog.html')
        else:
            return render_template('admin/login.html')
    # except:
    #      return render_template('admin/login.html')


@app.route('/viewBlog')
def viewBlog():

    if session['loginRole'] == 'admin':
        blogDAO = BlogDAO()
        blogDict = blogDAO.searchBlog()
        return render_template('admin/viewBlog.html', blogDict=blogDict)
    else:
        blogDAO = BlogDAO()
        blogDict = blogDAO.searchBlog()
        return render_template('user/viewBlog.html', blogDict=blogDict)

@app.route('/deleteBlog', methods=['GET'])
def deleteBlog():
    try:
        if session['loginRole'] == 'admin':
            blogVO = BlogVO()
            blogDAO = BlogDAO()
            blogVO.blogId = request.args.get('blogId')
            blogVO.blogActiveStatus = 'deactive'
            blogDAO.deleteBlog(blogVO)
            return viewBlog()
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')


@app.route('/editBlog', methods=['GET'])
def editBlog():
    try:
        if session['loginRole'] == 'admin':
            blogVO = BlogVO()
            blogDAO = BlogDAO()
            blogVO.blogId = request.args.get('blogId')
            blogDict = blogDAO.searchBlogbyId(blogVO)
            return render_template('admin/editBlog.html', blogDict=blogDict)
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')


@app.route('/updateBlog', methods=['POST'])
def updateBlog():
    try:
        if session['loginRole'] == 'admin':
            blogVO = BlogVO()
            blogDAO = BlogDAO()
            UPLOAD_FOLDER = 'C:/project/admin/project/static/adminResources/blog'

            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

            file = request.files['uploadBlogFile']

            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'])

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            blogVO.blogFilename = filename
            blogVO.blogFilepath = filepath
            blogVO.blogTitle = request.form['uploadBlogTitle']
            blogVO.blogDescription = request.form['uploadBlogDescription']
            blogVO.blogActiveStatus = 'active'
            blogVO.blogId = request.form['blogId']
            blogDAO.updateBlog(blogVO)
            return redirect(url_for('viewBlog'))
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')
