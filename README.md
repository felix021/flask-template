Flask 框架模板

## 初始化db

    python manage.py shell
    >> from app import db
    >> db.create_all()

## 启动服务

    python manage.py runserver -h 0.0.0.0 -p 8888

## 启动参数

    python manage.py runserver -?
