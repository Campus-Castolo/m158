from flask import Blueprint, render_template
import psutil
import matplotlib.pyplot as plt
from io import BytesIO
import base64

networkinfo_blueprint = Blueprint('networkinfo', __name__)

@networkinfo_blueprint.route('/')
def network_info():
    # Get network statistics
    net_info = psutil.net_io_counters(pernic=True)

    # Extract the top 10 protocols by bytes sent
    top_protocols = sorted(net_info.items(), key=lambda x: x[1].bytes_sent, reverse=True)[:10]

    # Create bar charts for the top 10 protocols
    fig, ax = plt.subplots()
    protocols = [protocol[0] for protocol in top_protocols]
    bytes_sent = [protocol[1].bytes_sent for protocol in top_protocols]

    ax.bar(protocols, bytes_sent)
    ax.set_ylabel('Bytes Sent')
    ax.set_title('Top 10 Network Protocols by Bytes Sent')

    # Save the chart to a BytesIO object
    img_buf = BytesIO()
    fig.savefig(img_buf, format='png')
    img_buf.seek(0)
    img_data = base64.b64encode(img_buf.read()).decode('utf-8')

    # Pass the network information and chart image data to the template
    return render_template('network_info.html', net_info=net_info, top_protocols=top_protocols, img_data=img_data)
