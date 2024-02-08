from flask import Blueprint, render_template
import psutil
import matplotlib.pyplot as plt
from io import BytesIO
import base64

pcinfo_blueprint = Blueprint('pcinfo', __name__)

@pcinfo_blueprint.route('/')
def pc_info():
    # Get CPU and memory information
    cpu_info = psutil.cpu_percent()
    mem_info = psutil.virtual_memory()

    # Create a bar chart for CPU usage
    fig_cpu, ax_cpu = plt.subplots()
    ax_cpu.bar(['CPU Usage'], [cpu_info])
    ax_cpu.set_ylabel('Percentage')
    ax_cpu.set_title('CPU Usage')

    # Save the CPU chart to a BytesIO object
    img_buf_cpu = BytesIO()
    fig_cpu.savefig(img_buf_cpu, format='png')
    img_buf_cpu.seek(0)
    img_data_cpu = base64.b64encode(img_buf_cpu.read()).decode('utf-8')

    # Create a bar chart for memory usage
    fig_mem, ax_mem = plt.subplots()
    ax_mem.bar(['Memory Usage'], [mem_info.percent])
    ax_mem.set_ylabel('Percentage')
    ax_mem.set_title('Memory Usage')

    # Save the memory chart to a BytesIO object
    img_buf_mem = BytesIO()
    fig_mem.savefig(img_buf_mem, format='png')
    img_buf_mem.seek(0)
    img_data_mem = base64.b64encode(img_buf_mem.read()).decode('utf-8')

    # Pass the CPU and memory information along with the image data to the template
    return render_template('pc_info.html', cpu_info=cpu_info, mem_info=mem_info, img_data_cpu=img_data_cpu, img_data_mem=img_data_mem)
