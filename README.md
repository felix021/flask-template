Flask 框架模板

## 初始化db

    python manage.py shell
    >> from app import db
    >> db.create_all()

## 启动服务

    python manage.py runserver -h 0.0.0.0 -p 8888
    #其他参数
    python manage.py runserver -?

## uwsgi

### 1. nginx配置
    
将 uwsgi/nginx.conf 链到 nginx 的 site-enabled 目录下，并按需修改

### 2. 启动uwsgi

    ./uwsgi/manage.sh start

### 3. 维护
    
    $ ./uwsgi/manage.sh
    Usage: %s <start|reload|stop|status|help>
