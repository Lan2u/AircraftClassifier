SELECT aircraft_images.path, aircraft_variants.variantname 
FROM aircraft_images 
INNER JOIN aircraft_variants 
ON aircraft_images.variantid = aircraft_variants.variantid
AND (aircraft_variants.variantname = '737-800'
OR aircraft_variants.variantname = 'c-130'
OR aircraft_variants.variantname = 'cessna 172')
ORDER BY random()