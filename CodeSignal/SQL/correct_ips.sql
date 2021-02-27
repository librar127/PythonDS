CREATE PROCEDURE correctIPs()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    select
        id, 
        ip
    from
        ips
    where
        IS_IPV4(ip)
    and
        ip regexp "(\\d{2}.\\d+)$|(\\d+.\\d{2})$"
    order by id;
END