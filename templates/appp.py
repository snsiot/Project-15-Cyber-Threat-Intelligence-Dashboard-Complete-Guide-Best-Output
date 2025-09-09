from datetime import datetime
@app.template_filter('datetimeformat')
def datetimeformat(value):
    if value:
        return datetime.utcfromtimestamp(value).strftime('%Y-%m-%d %H:%M:%S UTC')
    return "N/A"
