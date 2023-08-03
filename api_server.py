import _creckle_pop_flow

from flask import flash, Flask, render_template, request

app = Flask(__name__)
app.secret_key = "b26el&$uGX_ZUhnbLk6RiVI3EgGP9k@eYD"


@app.get("/creckle_pop")
def creckle_pop():
    start_number = request.args.get("start_number", "").strip()
    end_number = request.args.get("end_number", "").strip()
    if not start_number and not end_number:
        return render_template(
            "creckle-pop.html",
            start_number=start_number,
            end_number=end_number,
        )

    if not start_number.isdigit() or not end_number.isdigit():
        flash("Inserted ID is not a valid integer number.")
        return render_template(
            "creckle-pop.html",
            start_number=start_number,
            end_number=end_number,
        )

    try:
        result = _creckle_pop_flow.get_result(start_number, end_number)
    except ValueError:
        flash("Sorry, something didnt work correctly.")
        return render_template(
            "creckle-pop.html",
            start_number=start_number,
            end_number=end_number,
        )

    return render_template(
        "creckle-pop.html",
        start_number=start_number,
        end_number=end_number,
        result=result,
    )


if __name__ == "__main__":
    app.run(debug=True)
