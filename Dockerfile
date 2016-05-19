FROM slave4.wizeye.com.cn:5000/ubuntu-python
COPY quick_sort.py /home/quick_sort.py
CMD python /home/quick_sort.py