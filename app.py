from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys
app = Flask(__name__)



@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception ("We are generating custom exception")

    except Exception as ex:
        housing = HousingException(ex,sys)
        logging.info(housing.error_message)
        logging.info("Pasing logging module")
    return "First Heroku Deplyomnet"

if __name__ == "__main__":
    app.run(debug = True)