-- What customers are from the UK
SELECT customername FROM customers WHERE country='UK';

-- What is the name of the customer who has the most orders?
SELECT customername, COUNT(orderid) FROM orders
LEFT JOIN customers ON orders.customerid = customers.customerid
GROUP BY customers.customername
ORDER BY COUNT(orderid) DESC
LIMIT 1;

-- What supplier has the highest average product price?
SELECT suppliername, AVG(price) AS avg_price FROM products
LEFT JOIN suppliers ON products.supplierid = suppliers.supplierid
GROUP BY suppliername
ORDER BY avg_price DESC
LIMIT 1;

-- What category has the most orders?
SELECT categoryname, COUNT(orderid) FROM orderdetails
LEFT JOIN products ON products.productid = orderdetails.productid
LEFT JOIN categories ON products.categoryid = categories.categoryid
GROUP BY categoryname
ORDER BY COUNT(orderid) DESC
LIMIT 1;

-- What employee made the most sales (by number of sales)?
SELECT employeeid, firstname, lastname, SUM(quantity) AS sales FROM orders
LEFT JOIN employees ON orders.employeeid = employees.employeeid
LEFT JOIN orderdetails ON orders.orderid = orderdetails.orderid
GROUP BY employeeid
ORDER BY sales DESC
LIMIT 1;

-- What employee made the most sales (by value of sales)?
SELECT firstname, lastname, SUM(quantity * price) AS sales FROM orders
LEFT JOIN employees ON orders.employeeid = employees.employeeid
LEFT JOIN orderdetails ON orders.orderid = orderdetails.orderid
LEFT JOIN products ON orderdetails.productid = products.productid
GROUP BY employees.employeeid
ORDER BY sales DESC
LIMIT 1;

-- What employees have BS degrees? (Hint: Look at LIKE operator)
SELECT employeeid, firstname, lastname from employees
WHERE notes LIKE '%BS%';

-- What supplier has the highest average product price assuming they have at least 2 products (Hint: Look at the HAVING operator)
SELECT suppliername, AVG(price) AS avg_price FROM products
LEFT JOIN suppliers ON products.supplierid = suppliers.supplierid
GROUP BY suppliername
HAVING count(productid) > 1
ORDER BY avg_price DESC
LIMIT 1;
