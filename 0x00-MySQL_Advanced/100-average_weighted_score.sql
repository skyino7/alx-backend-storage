-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score DECIMAL(10, 2);
    DECLARE total_weight DECIMAL(10, 2);
    DECLARE average_score DECIMAL(10, 2);

    -- Calculate the total score and total weight for the user
    SELECT SUM(score * weight) INTO total_score, SUM(weight) INTO total_weight
    FROM scores
    WHERE user_id = user_id;

    -- Calculate the average weighted score
    IF total_weight > 0 THEN
        SET average_score = total_score / total_weight;
    ELSE
        SET average_score = 0;
    END IF;

    -- Store the average weighted score for the user
    UPDATE users
    SET average_weighted_score = average_score
    WHERE id = user_id;
END $$

DELIMITER ;