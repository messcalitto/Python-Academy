from flask import Blueprint, request
import math

math_bp = Blueprint("math", __name__)


@math_bp.route("/factorial/<n>", methods=["GET"])
def factorial(n):
    res = math.factorial(int(n))
    return {
        "result": res,
    }


def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case

@math_bp.route("/fibonacci/", methods=["POST"])
def fibonacci():
    n = request.form.get("n")
    res = fibonacci_of(int(n))
    return  {
        "result": res,
    }


@math_bp.route("/power/", methods=["POST"])
def power():
    n = request.headers.get("n")
    res = int(n) ** 2
    return  {
        "result": res,
    }

