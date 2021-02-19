# Write your MySQL query statement below

SELECT t.Id, 
    CASE
        WHEN t.p_id IS NULL THEN "Root"
        WHEN t.id NOT IN (SELECT DISTINCT p_id FROM tree WHERE p_id IS NOT NULL)  THEN "Leaf"
        ELSE "Inner"
    END 
    AS "Type"

FROM tree t
ORDER BY t.Id ASC; 
