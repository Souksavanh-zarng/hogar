from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from app import app
# from dbconn import *


@app.route('/')
def index():
    return render_template('home/homepage.html')

@app.route('/about')
def about():
    return render_template('about/home_about.html',head_content='The most variety,')

@app.route('/product_bedroom')
def product_bedroom():
    return render_template('product/product_bedroom.html')

@app.route('/inspiration')
def inspiration():
    return render_template('inspiration/home_inspiration.html')

@app.route('/join_membership')
def join_membership():
    return render_template('membership/home_membership.html')

@app.route('/help')
def help():
    return render_template('help/home_help.html',head_content='Helping Centre')

@app.route('/mycart')
def mycart():
    return render_template('shopping_cart/home_cart.html',head_content='')



