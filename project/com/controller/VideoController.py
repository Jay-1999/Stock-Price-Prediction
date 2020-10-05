from flask import request, render_template, session, redirect, url_for
from project import app
from werkzeug.utils import secure_filename
from project.com.vo.VideoVO import VideoVO
from project.com.dao.VideoDAO import VideoDAO
from datetime import datetime
import os


@app.route('/loadVideo')
def loadVideo():
    try:
        if session['loginRole'] == 'admin':
            return render_template('admin/addVideos.html')
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')

@app.route('/insertVideo', methods=['POST'])
def insertVideo():
    try:
        if session['loginRole'] == 'admin':
            videoVO = VideoVO()
            videoDAO = VideoDAO()
            UPLOAD_FOLDER = 'C:/project/admin/project/static/adminResources/video'

            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

            file = request.files['videoFile']

            filename = secure_filename(file.filename)

            filepath = os.path.join(app.config['UPLOAD_FOLDER'])

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            videoVO.videoFilename = filename
            print videoVO.videoFilename
            videoVO.videoFilepath = filepath
            videoVO.videoTitle = request.form['videoTitle']
            videoVO.videoDescription = request.form['videoDescription']
            videoVO.videoDate, videoVO.videoTime = str(datetime.now()).split(' ')
            videoVO.videoActiveStatus = 'active'
            videoDAO.insertVideo(videoVO)
            return render_template('admin/addVideos.html')
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')

@app.route('/viewVideo')
def viewVideo():
    try:
        if session['loginRole'] == 'admin':
            videoDAO = VideoDAO()
            videoDict = videoDAO.searchVideo()
            return render_template('admin/viewVideo.html', videoDict=videoDict)
        else:
            videoDAO = VideoDAO()
            videoDict = videoDAO.searchVideo()
            return render_template('user/viewVideos.html', videoDict=videoDict)
    except:
        return render_template('admin/login.html')

@app.route('/deleteVideo',methods=['GET'])
def deleteVideo():

    try:
        if session['loginRole'] == 'admin':
            videoVO = VideoVO()
            videoDAO = VideoDAO()
            videoVO.videoId=request.args.get('videoId')
            videoVO.videoActiveStatus='deactive'
            videoDAO.deleteVideo(videoVO)
            return redirect(url_for('viewVideo'))
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')

@app.route('/livetv')
def livetv():
    return render_template('user/livetv.html')
