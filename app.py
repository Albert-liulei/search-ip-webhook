from flask import Flask, jsonify, render_template, request  # 导入Flask类
import logging
import geoip2.database  # ip

app = Flask(__name__)  # 实例化并命名为app实例

# 返回中文
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    ip = request.remote_addr
    logging.debug(ip)
    with geoip2.database.Reader('GeoLite2-City.mmdb') as reader:
        try:
            response = reader.city(ip)
        except Exception as e:
            print(f'数据库中没该IP有地址: {ip} !!!')
            country = 'None'
            city = 'None'
        else:
            country = response.country.names['zh-CN']
            city = response.city.name

    res = {
        'ip地址': ip,
        'country': country,
        'city': city
    }

    print(country, city)
    return jsonify(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
