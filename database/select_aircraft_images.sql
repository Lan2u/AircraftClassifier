SELECT aircraft_images.path, aircraft_variants.variantid
FROM aircraft_images 
INNER JOIN aircraft_variants 
ON aircraft_images.variantid = aircraft_variants.variantid
ORDER BY random()