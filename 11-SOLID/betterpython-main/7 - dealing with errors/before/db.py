import sqlite3


def blog_lst_to_json(item):
    return { 
        'id': item[0],
        'published': item[1],
        'title': item[2],
        'content': item[3],
        'public': bool(item[4])
         }

def fetch_blogs():
    #connect to database
    con=sqlite3.connect('application.db')
    cur=con.cursor()
    
    #execute query and fetch data
    cur.execute(f"SELECT * FROM blogs where public=1")
    result=list(map(blog_lst_to_json, cur.fetchall()))
    
    #close database
    con.close()
    
    return result

def fetch_blog(id: str):
    #connect to database
    con=sqlite3.connect('application.db')
    cur=con.cursor()
    
    #execute query and fetch data
    cur.execute(f"SELECT * FROM blogs where id='{id}'")
    result=cur.fetchone()
    
    data=blog_lst_to_json(result)
    
    #close database
    con.close()
    
    return data
