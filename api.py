from flask import Flask, request, jsonify



def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Home"

    # пример post запроса
    @app.route("/get-user/<user_id>")
    def get_user(user_id):
        user_data = {
            "user_id": user_id,
            "name": "John Doe",
            "email": "john.doe@example.com"
        }

        # чтобы взять аргументы через вопрос
        # (например, /get-user/123?extra='default')
        # можно использовать request.args.get(<название аргумента>)
        extra = request.args.get("extra")
        if extra:
            user_data['extra'] = extra

        # вернуть словарь как json объект со статусом 200
        return jsonify(user_data), 200

    # пример POST запроса
    @app.route("/create-user", methods=["POST"])
    def create_user():
        # если одна функция используется для нескольких методов
        # то необходимо предварительно проверять какой тип запроса используется
        if request.method == 'POST':
            # чтобы получить поступающий в запросе json
            # используем request.json
            data = request.get_json()
            return jsonify(data), 201  # статус 201 - запись создана

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
