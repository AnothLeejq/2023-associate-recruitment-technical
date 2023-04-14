Select owner_id, owner_name, Count(distinct(category_id)) as different_category_count
FROM
(
Select a.owner_id, a.owner_name,b.category_id FROM
(
(Select owner_id, owner_name FROM owner)a
JOIN
(Select c.owner_id, d.category_id FROM
(Select owner_id FROM article)c
JOIN
(Select category_id FROM category_article_mapping)d
on c.article_id = d.article_id
)b
on a.owner_id = b.owner_id
)
)
GROUP BY owner_id, owner_name
ORDER BY Count(distinct(category_id)) DESC