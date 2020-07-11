-- Table: public.aircraft_variants

-- DROP TABLE public.aircraft_variants;

CREATE TABLE IF NOT EXISTS public.aircraft_variants
(
    variantid integer NOT NULL DEFAULT nextval('aircraft_variants_variantid_seq'::regclass),
    variantname character varying(500) COLLATE pg_catalog."default",
    CONSTRAINT aircraft_variants_pkey PRIMARY KEY (variantid)
)

TABLESPACE pg_default;

ALTER TABLE public.aircraft_variants
    OWNER to postgres;
-- Index: variant_name

-- DROP INDEX public.variant_name;

CREATE INDEX variant_name
    ON public.aircraft_variants USING btree
    (variantname COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;