from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

def get_connection(): 
    conn = mysql.connector.connect( 
        host=os.getenv("DB_HOST"), 
        user=os.getenv("DB_USER"), 
        password=os.getenv("DB_PASSWORD"), 
        database=os.getenv("DB_NAME") 
    ) 
    return conn


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"})


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!"})


@app.route("/authors", methods=["GET"])
def get_authors():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Author")
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify(rows), 200

    except Error as e:
        return jsonify({"error": str(e)}), 500


@app.route("/authors", methods=["POST"])
def create_author():
    try:
        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        specialities = data.get("specialities")
        company_name = data.get("company_name")

        if not name or not email:
            return jsonify({"error": "name and email are required"}), 400

        conn = get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO Author (Name, Email, Specialities, Company_Name)
            VALUES (%s, %s, %s, %s)
        """
        values = (name, email, specialities, company_name)

        cursor.execute(query, values)
        conn.commit()

        new_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return jsonify({
            "Author_id": new_id,
            "Name": name,
            "Email": email,
            "Specialities": specialities,
            "Company_Name": company_name
        }), 201

    except Error as e:
        return jsonify({"error": str(e)}), 500


@app.route("/authors/<int:author_id>", methods=["PUT"])
def update_author(author_id):
    try:
        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        specialities = data.get("specialities")
        company_name = data.get("company_name")

        if not name or not email:
            return jsonify({"error": "name and email are required"}), 400

        conn = get_connection()
        cursor = conn.cursor()

        query = """
            UPDATE Author
            SET Name = %s, Email = %s, Specialities = %s, Company_Name = %s
            WHERE Author_id = %s
        """
        values = (name, email, specialities, company_name, author_id)

        cursor.execute(query, values)
        conn.commit()

        updated = cursor.rowcount

        cursor.close()
        conn.close()

        if updated == 0:
            return jsonify({"error": "Author not found"}), 404

        return jsonify({
            "Author_id": author_id,
            "Name": name,
            "Email": email,
            "Specialities": specialities,
            "Company_Name": company_name
        }), 200

    except Error as e:
        return jsonify({"error": str(e)}), 500


@app.route("/authors/<int:author_id>", methods=["DELETE"])
def delete_author(author_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM Author WHERE Author_id = %s", (author_id,))
        conn.commit()

        deleted = cursor.rowcount

        cursor.close()
        conn.close()

        if deleted == 0:
            return jsonify({"error": "Author not found"}), 404

        return jsonify({"message": "Author deleted"}), 200

    except Error as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=4996, debug=True)
    
