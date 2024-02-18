from mysql import mysql_connect_users, mysql_close
from mysql2 import mysql_connect_csdb, mysql2_close

from page.page_login import Login

if __name__ == '__main__':
    mysql_connect_users()
    mysql_connect_csdb()

    win = Login()
    win.mainloop()

    mysql_close()
    mysql2_close()