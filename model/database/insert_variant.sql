INSERT INTO aircraft_variants
	(variantname)
SELECT %s
WHERE
	NOT EXISTS (
		SELECT variantname FROM aircraft_variants WHERE variantname = %s
	);