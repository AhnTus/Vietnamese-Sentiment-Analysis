from flask import Flask, render_template, request, redirect, url_for, session, flash
from function.datapreprocessing import DataPreprocessing
from function.User_file import User
from function.Phone_file import Phone
from function.UserDao_file import UserDao
from function.Comment_file import Comment
from function.CommentDao_File import CommentDao
from function.PhoneDao_file import PhoneDao
import tensorflow as tf
from tensorflow import keras 
# from tensorflow.keras.models import load_model 
import numpy as np
import csv

app = Flask(__name__)
app.secret_key = 'sentiment'

dp = DataPreprocessing("./data/data_processed/trainprocessed.csv", "./data/data_processed/generate.csv")

# Function to generate text
def generate_text(comment):
    model_generate = tf.keras.models.load_model("./model/model_lstm_generate_text.h5")
    temp = ""
    for _ in range(3):
        comment_processed = dp.fit_transform_generate(comment)
        predicted_probs = model_generate.predict(comment_processed)
        word = dp.generate.index_word[np.argmax(predicted_probs)]
        comment += " " + word
        temp += " " + word
    return temp

# Function to predict sentiment
def predict_sentiment(comment):
    model_sentiment = tf.keras.models.load_model("./model/model_sentiment_lstm.h5")
    result = model_sentiment.predict(comment)
    label_index = np.argmax(result, axis=1)
    predicted_label = dp.labelEn.inverse_transform(label_index)
    return predicted_label[0]

@app.route('/sentiment_analysis', methods=['GET', 'POST'])
def sentiment_analysis():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    userDao = UserDao()
    commentDao = CommentDao()
    phoneDao = PhoneDao()
    user = User(userid=session['user_id'], username=session['username'])
    if user.getUserId == 1:
        if request.method == 'POST' and 'predict' in request.form:
            comment_of_user = commentDao.get_comment_by_user()
            results = []
            for comment_user in comment_of_user:
                comment = Comment(comment_id=comment_user[0], comment=comment_user[1])
                if comment is not None:
                    processed_comment = dp.fit_transform(comment.getComment)
                    full_name = userDao.get_full_name(User(comment=comment.getComment))
                    prediction = predict_sentiment(processed_comment)
                    prediction_s = dp.Standardization(prediction)
                    user_result = User(userid=user.getUserId, username=full_name, comment=comment.getComment, predict=prediction_s)
                    comment_result = Comment(comment_id=comment.getId, predict=prediction)
                    commentDao.update_comment(comment_result)
                    results.append(user_result)

            # Call the statistical function
            statistics = commentDao.statistical()

            # Export statistics to CSV
            with open('statistics.csv', 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Phone Name', 'Number of Positives', 'Number of Negatives', 'Number of Neutrals']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in statistics:
                    writer.writerow({
                        'Phone Name': row[0],
                        'Number of Positives': row[1],
                        'Number of Negatives': row[2],
                        'Number of Neutrals': row[3]
                    })

            return render_template('sentiment_analysis.html', user_id=user.getUserId, results=results)
    else:
        if request.method == 'POST':
            comment_input = request.form.get('comment_input')
            user = User(userid=session['user_id'], username=session['username'], comment=comment_input)
            phone = Phone(id=session['phone_id'])
            comment = Comment(comment=comment_input)
            commentDao.insert_comment(user, comment)
            comment_id = commentDao.get_comment_id_by_user()
            comment_idp = Comment(comment_id=comment_id)
            phoneDao.insert_comment_phone(phone, comment_idp)
            flash('Comment posted successfully!', 'success')
            return redirect(url_for('phone_detail', phone_id=phone.getId))
    return render_template('sentiment_analysis.html', user_id=user.getUserId, username=user.getUserName)

@app.route('/phone', methods=['GET', 'POST'])
def phone():
    phoneDao = PhoneDao()
    phone_of_db = phoneDao.get_list_phone()
    results = []
    for phone in phone_of_db[:30]:
        if phone[0] is not None:
            phone_result = Phone(id=phone[0], phone_name=phone[1], specifications=phone[2], photo=phone[3])
            results.append(phone_result)
    return render_template('phone.html', results=results)

@app.route('/phone/<int:phone_id>', methods=['GET', 'POST'])
def phone_detail(phone_id):
    phoneDao = PhoneDao()
    phone_of_db = phoneDao.get_phone(phone_id)
    phone = Phone(id=phone_of_db[0], phone_name=phone_of_db[1], specifications=phone_of_db[2], photo=phone_of_db[3])
    session['phone_id'] = phone_id
    user = User(username=session['username'], userid=session['user_id'])
    return render_template('sentiment_analysis.html', user_id=user.getUserId, user_name=user.getUserName,phone=phone)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username, password)
        userDao = UserDao()

        if userDao.check_login(user):
            user_id = userDao.get_user_id(user)
            session['username'] = username
            session['user_id'] = user_id
            if session['user_id'] == 1:
                return redirect(url_for('sentiment_analysis'))
            else:
                return redirect(url_for('phone'))
        else:
            flash('Invalid username or password.', 'error')

    return render_template('login.html')

@app.route('/generate_text', methods=['POST'])
def generate_text_route():
    comment = request.form.get('comment')
    if comment:
        generated_text = generate_text(comment)
        return {'generated_text': generated_text}
    return {'error': 'No comment provided'}, 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
