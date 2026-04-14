from flask import Flask, request
import math
import os

app = Flask(__name__)

def lcm(x, y):
    return abs(x * y) // math.gcd(x, y) if x and y else 0

@app.route("/southroman_mail_ru", methods=["GET"])
def get_lcm():
    try:
        x = int(request.args.get("x", ""))
        y = int(request.args.get("y", ""))
        if x < 0 or y < 0:
            return "NaN"
    except ValueError:
        return "NaN"

    return str(lcm(x, y))

if __name__ == "__main__":
    # запускаем локально на порту 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)