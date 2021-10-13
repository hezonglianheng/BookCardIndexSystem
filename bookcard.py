# coding:utf-8

import sqlite3
# import getSummarization(这是团队中另一位学长提供的文本摘要生成模块)
# import snownlp


def database_build():
    con = sqlite3.connect('book_card.db')
    cur = con.cursor()
    cur.execute('''create table if not exists book_card
                (id integer primary key autoincrement,
                card_text text not null,
                author text,
                name text,
                publish_info text,
                ways_to_get text,
                collect integer not null,
                tag1 text,
                tag2 text,
                tag3 text,
                tag4 text,
                tag5 text,
                summary text,
                thoughts text);''')
    con.commit()
    con.close()


def add(card_text, author=None, book_name=None,
        publish_info=None, ways_to_get=None, collect=0,
        tag1=None, tag2=None, tag3=None, tag4=None, tag5=None,
        thoughts=None):
    summarization = summary(card_text)
    con = sqlite3.connect('book_card.db')
    cur = con.cursor()
    cur.execute('''insert into book_card (card_text,author,name,
    publish_info,ways_to_get,collect,tag1,tag2,tag3,tag4,tag5,summary,
    thoughts) values (?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                (card_text, author, book_name, publish_info,
                 ways_to_get, collect, tag1, tag2, tag3, tag4,
                 tag5, summarization, thoughts))
    row_id = cur.lastrowid
    con.commit()
    con.close()
    return row_id


def delete(del_id):
    con = sqlite3.connect('book_card.db')
    cur = con.cursor()
    cur.execute('delete from book_card where id = ?', (del_id,))
    con.commit()
    con.close()


def update(update_id, **updates):
    con = sqlite3.connect('book_card.db')
    cur = con.cursor()
    for key in updates:
        cur.execute('update book_card set ' + key +
                    '= ? where id = ?', (updates[key], update_id))
    con.commit()
    con.close()


def search_all():
    con = sqlite3.connect('book_card.db')
    cur = con.cursor()
    cur.execute('select * from book_card')
    rows = cur.fetchall()
    con.close()
    return rows


def collect_search():
    con = sqlite3.connect('book_card.db')
    cur = con.cursor()
    cur.execute('select * from book_card where collect=1')
    rows = cur.fetchall()
    con.close()
    return rows


def id_search(row_id):
    con = sqlite3.connect('book_card.db')
    cur = con.cursor()
    cur.execute('select * from book_card where id=?', (row_id,))
    row = cur.fetchall()
    con.close()
    return row


def tag_search(tag):
    con = sqlite3.connect('book_card.db')
    cur = con.cursor()
    tag = tag
    cur.execute('''select * from book_card where tag1=? or tag2=?
    or tag3=? or tag4=? or tag5=?''', (tag, tag, tag, tag, tag))
    rows = cur.fetchall()
    con.close()
    return rows


def text_search(string):
    con = sqlite3.connect('book_card.db')
    cur = con.cursor()
    format_string = '%' + string + '%'
    cur.execute('''select * from book_card where card_text like ?''',
                (format_string,))
    row = cur.fetchall()
    con.close()
    return row


def book_name_search(name):
    con = sqlite3.connect('book_card.db')
    cur = con.cursor()
    format_string = '%' + name + '%'
    cur.execute('''select * from book_card where name like ?''',
                (format_string,))
    row = cur.fetchall()
    con.close()
    return row


def author_search(author):
    con = sqlite3.connect('book_card.db')
    cur = con.cursor()
    format_string = '%' + author + '%'
    cur.execute('''select * from book_card where author like ?''',
                (format_string,))
    row = cur.fetchall()
    con.close()
    return row


def string_search(string):
    result = []
    text_row = text_search(string)
    author_row = author_search(string)
    name_row = book_name_search(string)
    tag_row = tag_search(string)
    for i in text_row:
        if i not in result:
            result.append(i)
    for j in author_row:
        if j not in result:
            result.append(j)
    for k in name_row:
        if k not in result:
            result.append(k)
    for m in tag_row:
        if m not in result:
            result.append(m)
    return result


def summary(text):
    # s = getSummarization.getSummarization(text)
    # t = snownlp.SnowNLP(text)
    # s = t.summary()
    # print(s)
    return None


def drop_table():
    con = sqlite3.connect('book_card.db')
    cur = con.cursor()
    cur.execute('drop table book_card')
    con.commit()
    con.close()


def rebuild():
    drop_table()
    database_build()


if __name__ == '__main__':
    print(summary('''在《老子》那里，“无为”“守雌”是积极的政治哲学，即君主统治方术。但这种积极的政治层含义又恰恰是以其消极的社会层含义为基础和根源的。
在现实生活特别是古代农业社会中，除军事斗争的特殊情况外，并非任何矛盾都必须激化或转化。贴别是从一些生命有机体来看，以维持机体系统的和谐稳定为目的，强调对立项的依存渗透，中和互补，避免激剧的动荡、否定、毁灭、转化，在许多对象和许多情况下，有其重要的合理性。正由于中国辩证法主要源出于和应用于社会秩序、政治统治和人事经验，它之所以具有这种特性，便有其不可忽视的现实根据和生活依据。'''))