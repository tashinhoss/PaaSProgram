from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def find_nth_largest():
    if request.method == 'POST':
        numbers = request.form.get('numbers')
        n = int(request.form.get('n'))

        numbers_list = list(map(int, numbers.split()))
        numbers_list.sort(reverse=True)

        if 1 <= n <= len(numbers_list):
            nth_largest = numbers_list[n-1]
        else:
            nth_largest = 'Invalid input'

        return render_template('index.html', nth_largest=nth_largest, numbers=numbers, n=n)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
