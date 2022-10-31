-- Build a Number Guessing Game
-- This is one of the required projects to earn your certification. For this project, 
-- you will use Bash scripting, PostgreSQL, and Git to create a number guessing game 
-- that runs in the terminal and saves user information.


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

DROP DATABASE number_guess;
--
-- Name: number_guess; Type: DATABASE; Schema: -; Owner: freecodecamp
--

CREATE DATABASE number_guess WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8';


ALTER DATABASE number_guess OWNER TO freecodecamp;

\connect number_guess

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
-- Name: user_games; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.user_games (
    user_game_id integer NOT NULL,
    user_id integer NOT NULL,
    guesses integer NOT NULL,
    secret_number integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.user_games OWNER TO freecodecamp;

--
-- Name: user_games_user_game_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.user_games_user_game_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_games_user_game_id_seq OWNER TO freecodecamp;

--
-- Name: user_games_user_game_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.user_games_user_game_id_seq OWNED BY public.user_games.user_game_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    username character varying(30) NOT NULL
);


ALTER TABLE public.users OWNER TO freecodecamp;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO freecodecamp;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: user_games user_game_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.user_games ALTER COLUMN user_game_id SET DEFAULT nextval('public.user_games_user_game_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: user_games; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.user_games VALUES (1, 1, 3, 268);
INSERT INTO public.user_games VALUES (3, 1, 3, 572);
INSERT INTO public.user_games VALUES (2, 1, 5, 162);
INSERT INTO public.user_games VALUES (4, 2, 352, 351);
INSERT INTO public.user_games VALUES (5, 2, 332, 331);
INSERT INTO public.user_games VALUES (6, 3, 991, 990);
INSERT INTO public.user_games VALUES (7, 3, 419, 418);
INSERT INTO public.user_games VALUES (8, 2, 112, 109);
INSERT INTO public.user_games VALUES (9, 2, 189, 187);
INSERT INTO public.user_games VALUES (10, 2, 804, 803);
INSERT INTO public.user_games VALUES (11, 4, 612, 611);
INSERT INTO public.user_games VALUES (12, 4, 899, 898);
INSERT INTO public.user_games VALUES (13, 5, 703, 702);
INSERT INTO public.user_games VALUES (14, 5, 424, 423);
INSERT INTO public.user_games VALUES (15, 4, 195, 192);
INSERT INTO public.user_games VALUES (16, 4, 29, 27);
INSERT INTO public.user_games VALUES (17, 4, 445, 444);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.users VALUES (1, 'LenSys');
INSERT INTO public.users VALUES (2, 'user_1667205958954');
INSERT INTO public.users VALUES (3, 'user_1667205958953');
INSERT INTO public.users VALUES (4, 'user_1667206041375');
INSERT INTO public.users VALUES (5, 'user_1667206041374');


--
-- Name: user_games_user_game_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.user_games_user_game_id_seq', 17, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.users_user_id_seq', 5, true);


--
-- Name: user_games user_games_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.user_games
    ADD CONSTRAINT user_games_pkey PRIMARY KEY (user_game_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: user_games user_games_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.user_games
    ADD CONSTRAINT user_games_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

