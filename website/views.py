from string import printable
from flask import Blueprint, flash, render_template, request, jsonify, redirect, url_for
from .spellChecker import spellChecker

views = Blueprint('views', __name__)

@views.route('/spellChecker', methods=["GET", "POST"])
def spellChecker_page():

    sentence_dic = {}

    if request.method == "GET":
        return render_template("spellChecker.html", spelling_form_data = sentence_dic, )

    elif request.method == "POST":
        sentence = request.form.get("sentence")
        sentence_dic = spellChecker(sentence)
        return render_template("spellChecker.html", spelling_form_data = sentence_dic )



@views.route("/", methods=["GET"])
def home():

    return render_template("home.html")

