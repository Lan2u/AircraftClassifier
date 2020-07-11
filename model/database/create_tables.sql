CREATE TABLE IF NOT EXISTS public.aircraft_variants
(
    variantid integer NOT NULL DEFAULT nextval('aircraft_variants_variantid_seq'::regclass),
    variantname character varying(500) COLLATE pg_catalog."default",
    CONSTRAINT aircraft_variants_pkey PRIMARY KEY (variantid)
)

TABLESPACE pg_default;

ALTER TABLE public.aircraft_variants
    OWNER to postgres;
	
CREATE INDEX variant_name
    ON public.aircraft_variants USING btree
    (variantname COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;

CREATE TABLE IF NOT EXISTS public.aircraft_images
(
    imageid integer NOT NULL DEFAULT nextval('aircraft_images_imageid_seq'::regclass),
    path character varying(512) COLLATE pg_catalog."default",
    variantid integer,
    CONSTRAINT aircraft_images_pkey PRIMARY KEY (imageid),
    CONSTRAINT aircraft_images_variantid_fkey FOREIGN KEY (variantid)
        REFERENCES public.aircraft_variants (variantid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.aircraft_images
    OWNER to postgres;
