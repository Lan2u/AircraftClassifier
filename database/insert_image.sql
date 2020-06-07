INSERT INTO aircraft_images (path, variantid) VALUES
	(%s, (SELECT variantid FROM aircraft_variants WHERE variantname=%s));