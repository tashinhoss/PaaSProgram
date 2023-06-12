from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def find_nth_largest():
    if request.method == 'POST':
        numbers = request.form.get('numbers')
        n = int(request.form.get('n'))

        # Convert the input string of numbers to a list of integers
        numbers_list = list(map(int, numbers.split(',')))

        if len(numbers_list) < n:
            return render_template('index.html', error='Invalid input')

        # Sort the numbers in descending order
        numbers_list.sort(reverse=True)

        nth_largest = numbers_list[n - 1]

        return render_template('index.html', nth_largest=nth_largest)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
