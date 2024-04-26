-- SQL script that lists all bands with Glam rock as their main style,
-- ordered by their lifespan (years).

SELECT band_name, (IFNULL(split, 2023) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
