#!/usr/bin/python3
import psycopg2, cgi
import login


form = cgi.FieldStorage()
#getvalue uses the names from the form in previous page
ean = form.getvalue('ean')
designation = form.getvalue('designation')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Change Designation</title>')
print('</head>')
print('<body>')

connection = None

try:
    # Creating connection
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    # Making query

    

    sql = 'UPDATE product SET descr = %s WHERE ean = %s;'
    data = (designation, ean)
    
    # The string has the {}, the variables inside format() will replace the {}
    print('<p>{}</p>'.format(sql % data))
    # Feed the data to the SQL query as follows to avoid SQL injection
    cursor.execute(sql, data)
    # Commit the update (without this step the database will not change)
    connection.commit()
    # Closing connection
    cursor.close()

except Exception as e:
    # Print errors on the webpage if they occur
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))
finally:
    if connection is not None:
        connection.close()
print('</body>')
print('</html>')

