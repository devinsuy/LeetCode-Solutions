-- Write a SQL query to rank scores. 
-- If there is a tie between two scores, 
-- both should have the same ranking. Note that after a tie, 
-- the next ranking number should be the next consecutive integer value. 
-- In other words, there should be no "holes" between ranks.

-- Tie should have same rank -> Use Rank() or Dense_Rank()
--   After tie rank should be next value -> Dense_rank()

SELECT Score, DENSE_RANK() OVER(PARTITION BY score DESC) AS `Rank`
FROM Scores