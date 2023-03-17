# from flask import Flask, render_template, request, redirect, url_for, session
# from app import app
# from dbconn import *


# @app.route('/pointmanage')
# def pointmanage():
#     with getcursor() as cur:
#         sql="select code,name_1,unit_cost,balance_qty::int from ic_inventory where balance_qty>0 order by code limit 20"
#         cur.execute(sql)
#         stockall = cur.fetchall()

#     return render_template('manage/index.html',title="stock",subtitle="stockbalance",stockall=stockall)