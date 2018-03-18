from flask import Flask, Response
import subprocess


app = Flask(__name__)


@app.route('/yield')
def run_code():
    def run_command(command):
        process = subprocess.Popen(['python3', '-u', 'hello.py'], stdout=subprocess.PIPE)

        while True:
            output = process.stdout.readline()
            if output == b'' and process.poll() is not None:
                break
            if output:
                yield str(output.strip(), 'utf-8') + '<br/>\n'

        rc = process.poll()
        return rc

    return Response(run_command('echo'), mimetype='text/html')  # text/html is required for most browsers to show th$


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
