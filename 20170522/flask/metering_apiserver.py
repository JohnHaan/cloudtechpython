from flask import Flask, request
from sqlalchemy import create_engine, MetaData
import json
import datetime
from oslo_config import cfg

app = Flask(__name__)

DB_OPTS = [
    cfg.StrOpt('connection',default='mysql://id:password@controller:3306/dbname?charset=utf8', help=('connection path')),
    ]

def dateconverter(d):
    if type(d) is datetime.date:
        return d.__str__()

@app.route("/v1/billing/days", methods=["GET"])
def query_few_days_data():
    CONF = cfg.CONF
    # cfg.CONF.register_opts(DB_OPTS, "db")
    # cfg.CONF(default_config_files= ['/usr/local/etc/billing/billing-agent.ini'])
    result = []
    totaljson = []
    # engine = create_engine(CONF.db.connection, convert_unicode=True)
    engine = create_engine('mysql://billing:wmfrjdna!dufwjd10@10.90.20.11:3306/billing?charset=utf8', convert_unicode=True)
    metadata = MetaData(bind=engine)
    con = engine.connect()

    table_type = None
    tenant_id = None
    tenant_name = None
    start_date = None
    end_date = None
    pagenum = None
    limit = None

    # check essential key is exist
    if (request.args.get('type') is not None) and (request.args.get('start_date') is not None) and \
        (request.args.get('end_date') is not None) and (request.args.get('pagenum') is not None) and  \
            (request.args.get('limit') is not None):
        table_type = request.args['type']
        tenant_id = None
        start_date = request.args['start_date']
        end_date = request.args['end_date']
        pagenum = int(request.args['pagenum'])
        limit = int(request.args['limit'])
    else:
        print('invalid request')
        return json.dumps([]), 400

    if (request.args.get('tenant_id') is not None):
        tenant_id = request.args['tenant_id']
    elif (request.args.get('tenant_name') is not None):
        tenant_name = request.args.get('tenant_name')

    querystr = "select * from "
    if table_type == 'compute':
        querystr += "compute where date>='%s' and date <= '%s'  " % (start_date, end_date)
    elif table_type == 'volume':
        querystr += "volume where date>='%s' and date <= '%s'  " % (start_date, end_date)
    else:
        return json.dumps([]), 400

    if tenant_id is not None:
        querystr += "and projectid='%s' " % tenant_id
    elif tenant_name is not None :
        querystr += "and projectname='%s' " % tenant_name

    pagevalue = (pagenum-1) * limit
    querystr += "limit %d, %d" % (pagevalue, limit)
    # tenant_id CheckPoint is not exist in this method
    querydata = con.execute(querystr)
    columns = tuple([d[0] for d in querydata.cursor.description])
    for d in querydata.cursor:
        result.append(dict(zip(columns, d)))

    print(request.method)

    return json.dumps(result, default=dateconverter), 200
def main():
    app.run(debug=True, host='0.0.0.0', port=5009)

if __name__ == "__main__":
    main()