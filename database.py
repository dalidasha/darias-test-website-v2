from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://n2gzsh3fkwe2h4q8i1yf:pscale_pw_17LgU0AYA09ihjwuhLXBsBgZp86HvaC6RAXA4eJkqcw@aws.connect.psdb.cloud/dariaswebsite?charset=utf8mb4"


engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem",
        }
    }
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))
        return jobs

#    print(result_dicts)

#    print("type(result:", type(result))
#    result_all = result.all()
#    print("type(result.all()):", type(result_all))
#    print(type(result_all[0]))
#    first_result_dict = result_all[0]._asdict()
#    print("type(first_result_dict:", type(first_result_dict))
#    print(first_result_dict)
