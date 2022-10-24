-- Build a Celestial Bodies Database
-- This is one of the required projects to earn your certification. 
-- For this project, you will build a database of celestial bodies 
-- using PostgreSQL.

--
-- PostgreSQL database dump
--

-- Dumped from database version 12.9 (Ubuntu 12.9-2.pgdg20.04+1)
-- Dumped by pg_dump version 12.9 (Ubuntu 12.9-2.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE universe;
--
-- Name: universe; Type: DATABASE; Schema: -; Owner: freecodecamp
--

CREATE DATABASE universe WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8';


ALTER DATABASE universe OWNER TO freecodecamp;

\connect universe

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: galaxy; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.galaxy (
    galaxy_id integer NOT NULL,
    name character varying(50) NOT NULL,
    constellation character varying(50) NOT NULL,
    has_redshift boolean NOT NULL,
    distance integer NOT NULL,
    apparent_magnitude numeric(6,2) NOT NULL
);


ALTER TABLE public.galaxy OWNER TO freecodecamp;

--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.galaxy_galaxy_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.galaxy_galaxy_id_seq OWNER TO freecodecamp;

--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.galaxy_galaxy_id_seq OWNED BY public.galaxy.galaxy_id;


--
-- Name: moon; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.moon (
    moon_id integer NOT NULL,
    name character varying(50) NOT NULL,
    description character varying(50) NOT NULL,
    orbital_speed numeric(9,4) NOT NULL,
    temperature integer NOT NULL,
    is_synchron boolean NOT NULL,
    planet_id integer
);


ALTER TABLE public.moon OWNER TO freecodecamp;

--
-- Name: moon_moon_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.moon_moon_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.moon_moon_id_seq OWNER TO freecodecamp;

--
-- Name: moon_moon_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.moon_moon_id_seq OWNED BY public.moon.moon_id;


--
-- Name: planet; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.planet (
    planet_id integer NOT NULL,
    name character varying(50) NOT NULL,
    description text NOT NULL,
    distance integer NOT NULL,
    has_life boolean NOT NULL,
    orbital_period numeric(9,2) NOT NULL,
    star_id integer
);


ALTER TABLE public.planet OWNER TO freecodecamp;

--
-- Name: planet_details; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.planet_details (
    planet_details_id integer NOT NULL,
    name character varying(50) NOT NULL,
    description character varying(50) NOT NULL
);


ALTER TABLE public.planet_details OWNER TO freecodecamp;

--
-- Name: planet_details_planet_detail_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.planet_details_planet_detail_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.planet_details_planet_detail_id_seq OWNER TO freecodecamp;

--
-- Name: planet_details_planet_detail_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.planet_details_planet_detail_id_seq OWNED BY public.planet_details.planet_details_id;


--
-- Name: planet_planet_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.planet_planet_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.planet_planet_id_seq OWNER TO freecodecamp;

--
-- Name: planet_planet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.planet_planet_id_seq OWNED BY public.planet.planet_id;


--
-- Name: star; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.star (
    star_id integer NOT NULL,
    galaxy_id integer,
    name character varying(50) NOT NULL,
    star_type character varying(50) NOT NULL,
    magnitude numeric(6,2) NOT NULL,
    mass numeric(6,3) NOT NULL,
    distance integer NOT NULL
);


ALTER TABLE public.star OWNER TO freecodecamp;

--
-- Name: star_star_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.star_star_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.star_star_id_seq OWNER TO freecodecamp;

--
-- Name: star_star_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.star_star_id_seq OWNED BY public.star.star_id;


--
-- Name: galaxy galaxy_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy ALTER COLUMN galaxy_id SET DEFAULT nextval('public.galaxy_galaxy_id_seq'::regclass);


--
-- Name: moon moon_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon ALTER COLUMN moon_id SET DEFAULT nextval('public.moon_moon_id_seq'::regclass);


--
-- Name: planet planet_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet ALTER COLUMN planet_id SET DEFAULT nextval('public.planet_planet_id_seq'::regclass);


--
-- Name: planet_details planet_details_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet_details ALTER COLUMN planet_details_id SET DEFAULT nextval('public.planet_details_planet_detail_id_seq'::regclass);


--
-- Name: star star_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star ALTER COLUMN star_id SET DEFAULT nextval('public.star_star_id_seq'::regclass);


--
-- Data for Name: galaxy; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.galaxy VALUES (3, 'Milky Way', 'Sagittarius', false, 25881, 4.00);
INSERT INTO public.galaxy VALUES (4, 'Andromeda', 'Andromeda', false, 2, 3.44);
INSERT INTO public.galaxy VALUES (5, 'Antennae', 'Corvus', true, 45, 11.20);
INSERT INTO public.galaxy VALUES (6, 'Backward', 'Centaurus', true, 200, 12.60);
INSERT INTO public.galaxy VALUES (7, 'Black Eye', 'Coma Berenices', true, 17, 8.52);
INSERT INTO public.galaxy VALUES (8, 'Butterfly', 'Virgo', false, 59, 10.90);


--
-- Data for Name: moon; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.moon VALUES (1, 'Moon', 'Earth', 1.0220, 26, false, 1);
INSERT INTO public.moon VALUES (2, 'Phobos', 'Mars', 2.1380, 233, true, 4);
INSERT INTO public.moon VALUES (3, 'Deimos', 'Mars', 1.3513, 233, true, 4);
INSERT INTO public.moon VALUES (4, 'Ganymede', 'Jupiter', 10.8800, 110, true, 5);
INSERT INTO public.moon VALUES (5, 'Callisto', 'Jupiter', 8.2040, 134, true, 5);
INSERT INTO public.moon VALUES (6, 'Io', 'Jupiter', 17.3340, 110, true, 5);
INSERT INTO public.moon VALUES (7, 'Europa', 'Jupiter', 13.7430, 102, true, 5);
INSERT INTO public.moon VALUES (8, 'Titan', 'Saturn', 5.5700, 93, true, 6);
INSERT INTO public.moon VALUES (9, 'Rhea', 'Saturn', 8.4800, 76, true, 6);
INSERT INTO public.moon VALUES (10, 'Iapetus', 'Saturn', 3.2600, 110, true, 6);
INSERT INTO public.moon VALUES (11, 'Dione', 'Saturn', 0.5100, 87, true, 6);
INSERT INTO public.moon VALUES (12, 'Tethys', 'Saturn', 11.3500, 86, true, 6);
INSERT INTO public.moon VALUES (13, 'Enceladus', 'Saturn', 860.4000, 75, true, 6);
INSERT INTO public.moon VALUES (14, 'Mimas', 'Saturn', 14.2800, 64, true, 6);
INSERT INTO public.moon VALUES (16, 'Oberon', 'Uranus', 3.1500, 75, true, 7);
INSERT INTO public.moon VALUES (15, 'Titania', 'Uranus', 3.6400, 70, true, 7);
INSERT INTO public.moon VALUES (17, 'Umbriel', 'Uranus', 4.6700, 75, true, 7);
INSERT INTO public.moon VALUES (18, 'Ariel', 'Uranus', 5.5100, 60, true, 7);
INSERT INTO public.moon VALUES (19, 'Miranda', 'Uranus', 6.6600, 60, true, 7);
INSERT INTO public.moon VALUES (20, 'Triton', 'Neptune', 4.3900, 38, true, 8);


--
-- Data for Name: planet; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.planet VALUES (1, 'Earth', 'The Earth', 150, true, 365.25, 4);
INSERT INTO public.planet VALUES (2, 'Mercury', 'The Mercury', 46, false, 115.88, 4);
INSERT INTO public.planet VALUES (3, 'Venus', 'The Venus', 108, false, 583.92, 4);
INSERT INTO public.planet VALUES (4, 'Mars', 'The Mars', 230, false, 686.98, 4);
INSERT INTO public.planet VALUES (5, 'Jupiter', 'The Jupiter', 520, false, 4332.59, 4);
INSERT INTO public.planet VALUES (6, 'Saturn', 'The Saturn', 1400, false, 10759.22, 4);
INSERT INTO public.planet VALUES (7, 'Uranus', 'The Uranus', 3000, false, 30688.50, 4);
INSERT INTO public.planet VALUES (8, 'Neptune', 'The Neptune', 4500, false, 60195.00, 4);
INSERT INTO public.planet VALUES (9, 'Eris', 'The Eris', 14410, false, 204199.00, 4);
INSERT INTO public.planet VALUES (10, 'Pluto', 'The Pluto', 5910, false, 90560.00, 4);
INSERT INTO public.planet VALUES (11, 'Sedna', 'The Sedna', 14962, false, 1139000.00, 4);
INSERT INTO public.planet VALUES (12, 'Quaoar', 'The Quaoar', 6540, false, 105495.00, 4);


--
-- Data for Name: planet_details; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.planet_details VALUES (1, 'Sol', 'Sun - a star at center of Solar System');
INSERT INTO public.planet_details VALUES (2, 'Earth', '3rd planet from the Sun');
INSERT INTO public.planet_details VALUES (3, 'Venus', '2nd planet from the Sun');


--
-- Data for Name: star; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.star VALUES (1, 6, 'Proxima Centauri', 'star', 15.53, 0.122, 4);
INSERT INTO public.star VALUES (2, 6, 'Rigil Kentaurus', 'bright star', 4.38, 1.079, 4);
INSERT INTO public.star VALUES (4, 3, 'Sol', 'bright star', 4.85, 1.000, 0);
INSERT INTO public.star VALUES (5, 6, 'Taliman', 'bright star', 5.71, 0.909, 4);
INSERT INTO public.star VALUES (6, 4, 'Ross 248', 'star', 14.79, 0.136, 10);
INSERT INTO public.star VALUES (7, 8, 'Ross 128', 'star', 13.51, 0.168, 11);


--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.galaxy_galaxy_id_seq', 8, true);


--
-- Name: moon_moon_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.moon_moon_id_seq', 20, true);


--
-- Name: planet_details_planet_detail_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.planet_details_planet_detail_id_seq', 3, true);


--
-- Name: planet_planet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.planet_planet_id_seq', 12, true);


--
-- Name: star_star_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.star_star_id_seq', 7, true);


--
-- Name: galaxy galaxy_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_name_key UNIQUE (name);


--
-- Name: galaxy galaxy_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_pkey PRIMARY KEY (galaxy_id);


--
-- Name: moon moon_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_name_key UNIQUE (name);


--
-- Name: moon moon_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_pkey PRIMARY KEY (moon_id);


--
-- Name: planet_details planet_details_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet_details
    ADD CONSTRAINT planet_details_name_key UNIQUE (name);


--
-- Name: planet_details planet_details_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet_details
    ADD CONSTRAINT planet_details_pkey PRIMARY KEY (planet_details_id);


--
-- Name: planet planet_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_name_key UNIQUE (name);


--
-- Name: planet planet_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_pkey PRIMARY KEY (planet_id);


--
-- Name: star star_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_name_key UNIQUE (name);


--
-- Name: star star_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_pkey PRIMARY KEY (star_id);


--
-- Name: moon moon_planet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_planet_id_fkey FOREIGN KEY (planet_id) REFERENCES public.planet(planet_id);


--
-- Name: planet planet_star_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_star_id_fkey FOREIGN KEY (star_id) REFERENCES public.star(star_id);


--
-- Name: star star_galaxy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_galaxy_id_fkey FOREIGN KEY (galaxy_id) REFERENCES public.galaxy(galaxy_id);


--
-- PostgreSQL database dump complete
--

