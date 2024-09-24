# Write your MySQL query statement below

select product_name , year, price 
from Sales inner join Product
on sales.product_id = product.product_id ;