from flask import render_template,session,redirect,url_for,request
from project import app
from datetime import datetime
from project.com.dao.RegisterDAO import RegisterDAO
from project.com.dao.ForumAnswerDAO import ForumAnswerDAO
from project.com.vo.ForumAnswerVO import ForumAnswerVO
from project.com.vo.ForumQuestionVO import ForumQuestionVO
from project.com.dao.ForumQuestionDAO import ForumQuestionDAO

@app.route('/loadForum')
def loadForum():
    try:
        if session['loginRole'] == 'admin':
            return render_template('admin/index.html')
        else:
            forumQuestionDAO = ForumQuestionDAO()
            forumQuestionDict = forumQuestionDAO.searchForumQuestion()

            forumAnswerDAO = ForumAnswerDAO()
            forumAnswerDict = forumAnswerDAO.searchForumAnswer()

            registerDAO = RegisterDAO()
            registerDict = registerDAO.searchRegister()

            return render_template('user/forum.html', forumQuestionDict=forumQuestionDict,forumAnswerDict=forumAnswerDict, registerDict=registerDict ,session=session)
    except:
        return render_template('admin/login.html')


@app.route('/insertForumQuestion',methods=['POST'])
def insertForumQuestion():
    if session['loginRole'] != 'user':
        return redirect(url_for('login'))

    else:
        forumQuestionDAO = ForumQuestionDAO()
        forumQuestionVO = ForumQuestionVO()

        forumQuestionVO.forumQuestion = request.form['forumquestion']
        forumQuestionVO.forumQuestionDate, forumQuestionVO.forumQuestionTime = str(datetime.now()).split(' ')
        forumQuestionVO.forumQuestionActiveStatus = 'active'
        forumQuestionVO.forumQuestionDiscussion = 1

        forumQuestionVO.forumQuestion_LoginId = session['loginId']

        forumQuestionDAO.insertForumQuestion(forumQuestionVO)
        # print forumQuestionVO.forumQuestion_LoginId

        return redirect(url_for('loadForum'))

@app.route('/insertForumAnswer',methods=['POST'])
def insertForumAnswer():
    if session['loginRole'] != 'user':
        return redirect(url_for('login'))

    else:
        forumAnswerDAO = ForumAnswerDAO()
        forumAnswerVO = ForumAnswerVO()

        forumAnswerVO.forumAnswer_ForumQuestionId = request.form['forumQuestionId']
        forumAnswerVO.forumAnswer = request.form['forumAnswer']
        forumAnswerVO.forumAnswerDate, forumAnswerVO.forumAnswerTime = str(datetime.now()).split(' ')
        forumAnswerVO.forumAnswerActiveStatus = 'active'

        forumAnswerVO.forumAnswer_LoginId = session['loginId']

        forumAnswerDAO.insertForumAnswer(forumAnswerVO)

        return redirect(url_for('loadForum'))


@app.route('/replyQuestion', methods=['GET'])
def replyQuestion():
    try:
        if session['loginRole'] != 'admin':
            forumQuestionDAO = ForumQuestionDAO()
            forumQuestionVO = ForumQuestionVO()
            forumQuestionVO.forumQuestionId = request.args.get('QuestionId')
            forumQuestionDict = forumQuestionDAO.searchForumQuestionById(forumQuestionVO)
            return render_template('user/replyForum.html', forumQuestionDict=forumQuestionDict)
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')

@app.route('/deleteQuestion',methods=['GET'])
def deleteQuestion():

    if session['loginRole']== 'admin':
        return redirect(url_for('login'))
    else:
        forumQuestionVO = ForumQuestionVO()
        forumQuestionDAO = ForumQuestionDAO()
        forumQuestionVO.forumQuestionId = request.args.get('QuestionId')
        forumQuestionVO.forumQuestionActiveStatus = 'deactive'
        forumQuestionDAO.deleteQuestion(forumQuestionVO)
        return redirect(url_for('loadForum'))

@app.route('/deleteAnswer',methods=['GET'])
def deleteAnswer():
    if session['loginRole']== 'admin':
        return redirect(url_for('login'))
    else:
        forumAnswerVO = ForumAnswerVO()
        forumAnswerDAO = ForumAnswerDAO()
        forumAnswerVO.forumAnswerId = request.args.get('AnswerId')
        # print forumAnswerVO.forumAnswerId
        forumAnswerVO.forumAnswerActiveStatus = 'deactive'
        forumAnswerDAO.deleteAnswer(forumAnswerVO)
        return redirect(url_for('loadForum'))


@app.route('/discussQuestion',methods=['GET'])
def discussQuestion():

    if session['loginRole']== 'admin':
        return redirect(url_for('login'))
    else:
        forumQuestionVO = ForumQuestionVO()
        forumQuestionDAO = ForumQuestionDAO()
        forumQuestionVO.forumQuestionId = request.args.get('QuestionId')
        forumQuestionVO.forumQuestionDiscussion = '0'
        forumQuestionDAO.discussQuestion(forumQuestionVO)
        return redirect(url_for('loadForum'))