--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Ubuntu 14.5-1ubuntu1)
-- Dumped by pg_dump version 14.5 (Ubuntu 14.5-1ubuntu1)

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
-- Name: clients; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.clients (
    fullname character varying(50),
    id integer NOT NULL,
    passport character varying(50),
    birthday_date date,
    address character varying(50),
    email character varying(50),
    password character varying(50)
);


ALTER TABLE public.clients OWNER TO admin;

--
-- Name: employers; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.employers (
    id integer NOT NULL,
    "position" character varying(50),
    fullname character varying(50),
    login character varying(50),
    password character varying(50),
    last_entry timestamp without time zone,
    entry_type character varying(50)
);


ALTER TABLE public.employers OWNER TO admin;

--
-- Name: goods; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.goods (
    id integer NOT NULL,
    title character varying NOT NULL,
    img character varying,
    cost_per_hour integer,
    full_price integer,
    description text,
    remaining_amount integer DEFAULT 0 NOT NULL,
    category character varying
);


ALTER TABLE public.goods OWNER TO admin;

--
-- Name: login_history; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.login_history (
    login character varying,
    entry_type character varying,
    entry_time timestamp without time zone,
    id integer NOT NULL
);


ALTER TABLE public.login_history OWNER TO admin;

--
-- Name: login_history_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.login_history_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.login_history_id_seq OWNER TO admin;

--
-- Name: login_history_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.login_history_id_seq OWNED BY public.login_history.id;


--
-- Name: order_goods; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.order_goods (
    order_id integer,
    goods_id integer
);


ALTER TABLE public.order_goods OWNER TO admin;

--
-- Name: orders; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.orders (
    id bigint NOT NULL,
    create_date date,
    create_time time without time zone,
    client_id integer,
    status character varying(50),
    close_date date,
    arenda_hour_time integer,
    employer_id integer
);


ALTER TABLE public.orders OWNER TO admin;

--
-- Name: login_history id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.login_history ALTER COLUMN id SET DEFAULT nextval('public.login_history_id_seq'::regclass);


--
-- Name: login_history_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.login_history_id_seq', 4, true);


--
-- Name: orders заказы_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT "заказы_pk" PRIMARY KEY (id);


--
-- Name: clients клиенты_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.clients
    ADD CONSTRAINT "клиенты_pk" PRIMARY KEY (id);


--
-- Name: employers сотрудники_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.employers
    ADD CONSTRAINT "сотрудники_pk" PRIMARY KEY (id);


--
-- Name: goods товары_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.goods
    ADD CONSTRAINT "товары_pk" PRIMARY KEY (id);


--
-- Name: orders заказы_fk; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT "заказы_fk" FOREIGN KEY (client_id) REFERENCES public.clients(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: orders заказы_сотрудники_fk; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT "заказы_сотрудники_fk" FOREIGN KEY (employer_id) REFERENCES public.employers(id) ON UPDATE SET NULL ON DELETE SET NULL;


--
-- Name: order_goods заказы_товары_fk; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.order_goods
    ADD CONSTRAINT "заказы_товары_fk" FOREIGN KEY (order_id) REFERENCES public.orders(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: order_goods заказы_товары_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.order_goods
    ADD CONSTRAINT "заказы_товары_fk_1" FOREIGN KEY (goods_id) REFERENCES public.goods(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

