from flask import Flask, request, render_template
from employee_info import *
app = Flask(__name__)


@app.route('/')
@app.route('/employee')
@app.route('/employee/save', methods=['POST', 'GET'])
def employee_crud_landing_page():
    message = ""
    if request.method == 'POST':
        formdata = request.form
        emp = Employee(**formdata)
        print(emp)
        file_types = formdata.getlist('fileType')
        if file_types:
            for type in file_types:
                funref = FILE_TYPES_FUN_REF.get(type)
                funref(emp)
            message = f"Data written successfully in {file_types}.."
        else:
            message = "You should select at least one file type.."

    return render_template('employee.html', message=message)


@app.route('/file/read', methods=['POST'])
def show_data():
    emplist = []
    if request.method == 'POST':
        fileType = request.form.get('fileType')
        if fileType == "J":
            emplist = read_from_json_file()
    return render_template('employee.html', emplist=emplist)


if __name__ == '__main__':
    app.run(debug=True)