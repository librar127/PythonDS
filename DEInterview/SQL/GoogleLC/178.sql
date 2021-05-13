SELECT
    score,
    dense_rank() over(order by Score desc) `Rank`
FROM
    scores
order by `Rank`