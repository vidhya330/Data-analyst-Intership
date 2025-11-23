SELECT * FROM newschema.online_sales;
use newschema;
select extract(year from order_date)as order_year,extract(month from order_date)as order_month,amount from online_sales;
select extract(year from order_date)as year,extract(month from order_date)as month, sum(amount)as total_amount from online_sales

group by year,month;
select extract(year from order_date)as year,extract(month from order_date)as month, sum(amount)as revenue from online_sales

group by year,month;
select extract(year from order_date)as year,extract(month from order_date)as month, count(distinct order_id)as total_volume from online_sales

group by year,month;
select extract(year from order_date)as year,extract(month from order_date)as month, sum(amount)as total_revenue,count(distinct order_id)as total_volume from online_sales

group by year,month
order by year,month;
select extract(year from order_date)as year,extract(month from order_date)as month, count(distinct order_id)as total_volume from online_sales
where order_date between '2024-01-01'and '2024-03-31'
group by year,month
order by year,month;


