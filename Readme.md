# Google Trends Analysis

This Python script fetches and plots Google Trends data for a given keyword over a specified timeframe.

## Prerequisites

- Python 3
- pytrends
- matplotlib
- pandas

## Installation

Before running the script, you need to install the required Python packages. You can do this using pip:

bash
pip install pytrends matplotlib pandas


## Usage

To run the script, use the following command:


bash
python main.py



When prompted, enter the keyword and the number of days for the timeframe.

The script will then fetch the Google Trends data for the keyword over the past specified number of days and plot two charts:

1. Interest over time for the keyword: This chart shows how the interest in the keyword has changed over time. The x-axis is the date, and the y-axis is the interest.

2. Related queries for the keyword: This chart shows the top related queries for the keyword. The y-axis is the related queries, and the x-axis is their values.

Both charts are plotted for Vietnam.

## Reading the Charts

- Interest over time: A higher value means higher interest in the keyword. If there are peaks in the chart, that means there were times when the interest in the keyword was particularly high.

- Related queries: The related queries are the queries that people also search for when they search for the keyword. A higher value means a higher correlation with the keyword.


# Phân Tích Google Trends

Script Python này lấy và vẽ biểu đồ dữ liệu Google Trends cho một từ khóa nhất định trong một khoảng thời gian đã chỉ định.

## Yêu cầu

- Python 3
- pytrends
- matplotlib
- pandas

## Cài đặt

Trước khi chạy script, bạn cần cài đặt các gói Python cần thiết. Bạn có thể làm điều này bằng pip:

bash
pip install pytrends matplotlib pandas



## Sử dụng

Để chạy script, sử dụng lệnh sau:


python main.py



Khi được nhắc, nhập từ khóa và số ngày cho khoảng thời gian.

Script sau đó sẽ lấy dữ liệu Google Trends cho từ khóa trong số ngày đã chỉ định và vẽ hai biểu đồ:

1. Sự quan tâm theo thời gian đối với từ khóa: Biểu đồ này cho thấy sự thay đổi của sự quan tâm đối với từ khóa theo thời gian. Trục x là ngày, và trục y là sự quan tâm.

2. Các truy vấn liên quan đến từ khóa: Biểu đồ này cho thấy các truy vấn hàng đầu liên quan đến từ khóa. Trục y là các truy vấn liên quan, và trục x là giá trị của chúng.

Cả hai biểu đồ đều được vẽ cho Việt Nam.

## Đọc Biểu Đồ

- Sự quan tâm theo thời gian: Một giá trị cao hơn có nghĩa là sự quan tâm đối với từ khóa cao hơn. Nếu có các đỉnh trong biểu đồ, điều đó có nghĩa là có những thời điểm mà sự quan tâm đối với từ khóa đặc biệt cao.

- Các truy vấn liên quan: Các truy vấn liên quan là những truy vấn mà mọi người cũng tìm kiếm khi họ tìm kiếm từ khóa. Một giá trị cao hơn có nghĩa là mối tương quan cao hơn với từ khóa.



