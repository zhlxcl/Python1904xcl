# migrations是应用的迁移文件夹

'''
由一个python类生成一个MySQL数据表：
1.生成迁移文件（根据模型类生成相应的sql语句）
    python manage.py makemigrations
2.执行迁移（将迁移文件同步到数据库，执行相应的sql语句生成数据表）
    python manage.py migrate
'''