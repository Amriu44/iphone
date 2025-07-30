import psycopg2
import DataBase
from GettinPhoneDetail import data as phones

conn = psycopg2.connect(
    dbname=DataBase.dbname,
    user=DataBase.user,
    password=DataBase.password,
    host=DataBase.host,
    port=DataBase.port
)
conn.set_client_encoding('UTF8')
cur = conn.cursor()

def parse_price(price_str):
    if not price_str: return None
    try:
        return int(price_str.replace('تومان', '').replace('،', '').strip())
    except:
        return None

def parse_gb(text):
    if not text: return None
    try:
        return int(text.replace('گیگابایت', '').strip())
    except:
        return None

def parse_sim_number(text):
    if not text: return None
    try:
        return int(text.replace('عدد', '').strip())
    except:
        return None

def parse_battery(text):
    if not text: return None
    try:
        return int(text.replace('٪', '').replace('%', '').strip())
    except:
        return None

def fa_bool(text):
    if not text: return False
    return text.strip() == 'هستم'

def is_empty_record(phone):
    important_fields = ['برند و مدل', 'وضعیت', 'اصالت برند', 'تعداد سیم‌کارت', 'حافظهٔ داخلی', 'مقدار رم', 'قیمت']
    for f in important_fields:
        val = phone.get(f)
        if val and str(val).strip() != '':
            return False
    return True


for phone in phones:
    if is_empty_record(phone):
        continue

    brand = phone.get('برند و مدل')
    status = phone.get('وضعیت')
    original = phone.get('اصالت برند') == 'اصل'
    sim_number = parse_sim_number(phone.get('تعداد سیم‌کارت'))
    storage = parse_gb(phone.get('حافظهٔ داخلی'))
    ram = parse_gb(phone.get('مقدار رم'))
    color = phone.get('رنگ')
    tradeable = fa_bool(phone.get('مایل به معاوضه'))
    battery_health = parse_battery(phone.get('میزان سلامت باتری'))
    price = parse_price(phone.get('قیمت'))

    cur.execute("""
        INSERT INTO iphone (brand, status, original, sim_number, storage, ram, color, tradeable, battery_health, price)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        brand,
        status,
        original,
        sim_number,
        storage,
        ram,
        color,
        tradeable,
        battery_health,
        price
    ))

conn.commit()
cur.close()
conn.close()
