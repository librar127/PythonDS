-- Write your MySQL query statement below
SELECT
    A.invoice_id,
    B.customer_name,
    A.price
    ,COALESCE(COUNT(C.contact_name), 0) contacts_cnt
    ,SUM(CASE WHEN C.contact_email in (SELECT DISTINCT email FROM Customers) THEN 1 ELSE 0 END) trusted_contacts_cnt
FROM
    Invoices A
LEFT JOIN
    Customers B
ON
    A.user_id = B.customer_id
LEFT JOIN
    Contacts C
ON
    B.customer_id = C.user_id
GROUp BY
    A.invoice_id,
    B.customer_name,
    A.price
ORDER BY
    invoice_id
    