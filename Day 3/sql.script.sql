SELECT * FROM ecommerce.customers; 
select * from customers where city='chennai';
select * from customers where gender='male' and age>25;
select city,COUNT(*) AS total_customers from customers group by city;
select * from customers where city='chennai' order by customer_name;
select c.customer_name,p.product_name,i.quantity,i.order_date from items i inner join
customers c on i.customer_id=c.customer_id inner join products p on i.product_id=p.product_id;
select c.customer_name,c.city from customers c left join items i on c.customer_id=i.customer_id where
i.product_id is null;
select p.product_name,i.quantity,i.order_date from items i
right join products p on i.product_id=p.product_id;
select sum(i.quantity * p.price)as total_revenue from items i join 
products p on i.product_id=p.product_id;
select avg(age)as avg_age from customers where customer_id in(select customer_id from items);
select c.city,count(i.product_id) as orders_count from customers c join items i on c.customer_id=
i.customer_id group by c.city order by orders_count desc;
select customer_name from customers where customer_id in (select customer_id from items where 
product_id=(select product_id FROM  products order by price desc limit 1));
select product_name from products where product_id in (select product_id from items 
group by product_id having avg(quantity)>(select avg(quantity) from items));
CREATE VIEW p_summary as select c.customer_id, c.customer_name,count(i.product_id) as 
orders_count,sum(i.quantity*p.price)as total_spent from customers c left join items i on 
c.customer_id left join products p on i.product_id=p.product_id group by c.customer_id;
 create view m_sales as select date_format(order_date,'%y-%m')as month, sum(i.quantity *p.price)
 as revenue,count(i.product_id)as total_items from items i join products p on i.product_id=p.product_id
 group by month
 order by month;
 create index idx_city on customers(city); create index idx_order_date on items(order_date);
 create index idx_category on products(category);