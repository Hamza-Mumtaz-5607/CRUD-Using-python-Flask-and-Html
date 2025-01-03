from flask import Flask, render_template, request, redirect, abort

main = Flask(__name__)

# Store submitted data
data = []  # List of dictionaries to store the entries

@main.route('/')
def index():
    return render_template('index.html', data=data, enumerate=enumerate)

@main.route('/save', methods=['POST'])
def save_data():
    # Get form data
    name = request.form.get('name')
    date = request.form.get('date')
    invoice_number = request.form.get('invoice_number')

    # Add the new entry to the data list
    data.append({'name': name, 'date': date, 'invoice_number': invoice_number})

    # Redirect back to the home page
    return redirect('/')

@main.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_data(index):
    # Check if the index is valid
    if index < 0 or index >= len(data):
        abort(404)  # Return 404 if index is out of range

    if request.method == 'POST':
        # Update the specific entry
        data[index]['name'] = request.form.get('name')
        data[index]['date'] = request.form.get('date')
        data[index]['invoice_number'] = request.form.get('invoice_number')
        return redirect('/')  # Redirect back to the home page after edit

    # If it's a GET request, render the form to edit the specific entry
    return render_template('edit.html', entry=data[index], index=index)

@main.route('/delete/<int:index>', methods=['GET'])
def delete_data(index):
    # Check if the index is valid
    if index < 0 or index >= len(data):
        abort(404)  # Return 404 if index is out of range

    # Remove the entry from the data list
    data.pop(index)

    # Redirect back to the home page after deletion
    return redirect('/')

if __name__ == '__main__':
    main.run(debug=True)




   -------------Html-------------
   index.html

   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD Learning</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #333;
        }
        form {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: 0 auto;
        }
        label {
            display: block;
            margin: 10px 0 5px;
            color: #333;
        }
        input {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        table {
            width: 100%;
            margin-top: 30px;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            text-align: left;
            border: 1px solid #ddd;
        }
        th {
            background-color: #f2f2f2;
            color: #333;
        }
        td {
            background-color: #fff;
        }
        a {
            color: #007BFF;
            text-decoration: none;
            margin-right: 10px;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <h1>Enter Data</h1>
    <form action="/save" method="POST">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" required>

        <label for="date">Date:</label>
        <input type="date" name="date" id="date" required>

        <label for="invoice_number">Invoice Number:</label>
        <input type="number" name="invoice_number" id="invoice_number" required>

        <button type="submit">Save Data</button>
    </form>

    <h2>Saved Data:</h2>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Date</th>
                <th>Invoice Number</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for index, entry in enumerate(data) %}
                <tr>
                    <td>{{ entry.name }}</td>
                    <td>{{ entry.date }}</td>
                    <td>{{ entry.invoice_number }}</td>
                    <td>
                        <a href="/edit/{{ index }}">Edit</a>
                        <a href="/delete/{{ index }}">Delete</a>
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>

</body>
</html>



Edit.html -----------------

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Entry</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f9f9f9;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        form {
            margin: 20px auto;
            padding: 20px;
            max-width: 500px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }
        input {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <h1>Edit Entry</h1>
    <form action="/edit/{{ index }}" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="{{ entry.name }}" required>

        <label for="date">Date:</label>
        <input type="date" id="date" name="date" value="{{ entry.date }}" required>

        <label for="invoice_number">Invoice Number:</label>
        <input type="number" id="invoice_number" name="invoice_number" value="{{ entry.invoice_number }}" required>

        <button type="submit">Update</button>
    </form>
</body>
</html>
