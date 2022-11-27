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
-- Name: заказы; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."заказы" (
    "Код заказа" bigint NOT NULL,
    "Дата создания" date,
    "Время заказа" time without time zone,
    "Код клиента" integer,
    "Cтатус" character varying(50),
    "Дата закрытия" date,
    "Время проката" integer,
    "Код сотрудника" integer
);


ALTER TABLE public."заказы" OWNER TO admin;

--
-- Name: заказы_товары; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."заказы_товары" (
    "Код заказа" integer,
    "Код товара" integer
);


ALTER TABLE public."заказы_товары" OWNER TO admin;

--
-- Name: история_входа; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."история_входа" (
    "Логин" character varying,
    "Тип входа" character varying,
    "Время входа" timestamp without time zone,
    "Код входа" integer
);


ALTER TABLE public."история_входа" OWNER TO admin;

--
-- Name: клиенты; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."клиенты" (
    "ФИО" character varying(50),
    "Код клиента" integer NOT NULL,
    "Паспортные данные" character varying(50),
    "Дата рождения" date,
    "Адрес" character varying(50),
    "Эл. почта" character varying(50),
    "Пароль" character varying(50)
);


ALTER TABLE public."клиенты" OWNER TO admin;

--
-- Name: сотрудники; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."сотрудники" (
    "Код сотрудника" integer NOT NULL,
    "Должность" character varying(50),
    "ФИО" character varying(50),
    "Логин" character varying(50),
    "Пароль" character varying(50),
    "Последний вход" timestamp without time zone,
    "Тип входа" character varying(50)
);


ALTER TABLE public."сотрудники" OWNER TO admin;

--
-- Name: товары; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."товары" (
    "Код товара" integer NOT NULL,
    "Наименование" character varying NOT NULL,
    "Изображение" character varying,
    "Стоимость, руб. за час" integer,
    "Полная стоимость" integer,
    "Описание" text,
    "Оставшееся кол-во" integer DEFAULT 0 NOT NULL,
    "Категория" character varying
);


ALTER TABLE public."товары" OWNER TO admin;

--
-- Data for Name: заказы; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."заказы" ("Код заказа", "Дата создания", "Время заказа", "Код клиента", "Cтатус", "Дата закрытия", "Время проката", "Код сотрудника") FROM stdin;
45462526	2022-03-12	09:10:00	45462526	Новая	\N	2	101
45462527	2022-03-13	10:10:00	45462527	В прокате	\N	10	102
45462528	2022-03-14	11:10:00	45462528	В прокате	\N	2	103
45462529	2022-03-15	12:10:00	45462529	Новая	\N	10	104
45462530	2022-03-16	13:10:00	45462530	Закрыта	2022-04-16	5	105
45462531	2022-03-17	14:10:00	45462531	Новая	\N	8	106
45462532	2022-03-18	15:10:00	45462532	Новая	\N	4	107
45462533	2022-03-19	16:10:00	45462533	В прокате	\N	6	108
45462534	2022-03-20	10:00:00	45462534	В прокате	\N	12	109
45462535	2022-03-21	11:00:00	45462535	Новая	\N	2	110
45462536	2022-03-22	12:00:00	45462536	Закрыта	2022-03-22	10	101
45462537	2022-03-23	13:00:00	45462537	В прокате	\N	2	102
45462538	2022-03-24	14:00:00	45462538	В прокате	\N	10	102
45462539	2022-03-25	15:00:00	45462539	В прокате	\N	5	103
45462540	2022-03-26	16:00:00	45462540	Закрыта	2022-04-26	8	104
45462541	2022-03-27	17:00:00	45462541	Новая	\N	4	105
45462542	2022-03-28	18:00:00	45462542	В прокате	\N	6	106
45462543	2022-03-29	19:00:00	45462543	В прокате	\N	12	109
45462544	2022-03-30	12:30:00	45462544	Новая	\N	2	105
45462545	2022-03-31	13:30:00	45462545	Новая	\N	10	107
45462546	2022-04-01	14:30:00	45462546	Закрыта	2022-04-01	2	110
45462547	2022-04-02	15:30:00	45462547	Новая	\N	10	106
45462548	2022-04-03	16:30:00	45462548	Новая	\N	5	110
45462549	2022-04-04	17:30:00	45462549	В прокате	\N	8	108
45462550	2022-04-05	18:30:00	45462550	В прокате	\N	4	105
45462551	2022-04-06	15:30:00	45462551	В прокате	\N	6	108
45462552	2022-04-07	16:30:00	45462552	В прокате	\N	12	110
45462553	2022-04-08	17:30:00	45462553	Закрыта	2022-04-08	2	106
45462554	2022-04-09	18:30:00	45462554	Новая	\N	10	110
45462555	2022-04-10	19:30:00	45462555	В прокате	\N	2	108
45462556	2022-04-11	10:30:00	45462556	В прокате	\N	10	109
45462557	2022-04-12	11:30:00	45462557	Новая	\N	5	107
45462558	2022-04-13	12:30:00	45462558	Новая	\N	8	106
45462559	2022-04-14	13:30:00	45462559	Новая	\N	4	109
45462560	2022-04-15	14:30:00	45462560	В прокате	\N	6	105
45462561	2022-04-02	15:30:00	45462561	В прокате	\N	12	107
45462562	2022-04-03	16:30:00	45462562	В прокате	\N	2	109
45462563	2022-04-04	17:30:00	45462563	Закрыта	2022-04-04	10	108
45462564	2022-04-05	10:15:00	45462564	В прокате	\N	2	105
45462565	2022-04-06	11:15:00	45462565	Новая	\N	10	108
45462566	2022-04-07	12:15:00	45462566	Закрыта	2022-04-07	5	107
45462567	2022-04-08	13:15:00	45462567	В прокате	\N	8	105
45462568	2022-04-09	14:15:00	45462568	В прокате	\N	4	108
45462569	2022-04-01	15:15:00	45462569	В прокате	\N	6	106
45462570	2022-04-02	16:15:00	45462570	В прокате	\N	12	107
45462571	2022-04-03	10:45:00	45462571	В прокате	\N	8	110
45462572	2022-04-04	11:45:00	45462572	Закрыта	2022-04-04	5	109
45462573	2022-04-05	12:45:00	45462573	Новая	\N	8	106
45462574	2022-04-06	13:45:00	45462574	Новая	\N	4	105
45462575	2022-04-07	14:45:00	45462575	Новая	\N	6	108
\.


--
-- Data for Name: заказы_товары; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."заказы_товары" ("Код заказа", "Код товара") FROM stdin;
45462526	34
45462526	31
45462526	353
45462526	336
45462527	98
45462527	45
45462527	89
45462527	99
45462528	92
45462528	45
45462528	57
45462528	88
45462529	92
45462529	45
45462529	57
45462529	88
45462529	44
45462530	98
45462530	45
45462530	89
45462530	353
45462530	336
45462530	34
45462531	34
45462531	31
45462531	353
45462532	98
45462532	45
45462532	89
45462532	99
45462533	92
45462533	45
45462533	57
45462533	89
45462534	92
45462534	45
45462534	57
45462534	88
45462534	45
45462535	98
45462535	45
45462535	89
45462535	353
45462535	336
45462536	34
45462536	31
45462536	353
45462537	98
45462537	45
45462537	89
45462537	99
45462538	92
45462538	45
45462538	57
45462539	92
45462539	45
45462539	57
45462539	88
45462540	98
45462540	45
45462540	89
45462540	353
45462540	336
45462541	34
45462541	31
45462541	353
45462542	98
45462542	45
45462542	89
45462542	99
45462543	92
45462543	45
45462543	57
45462544	92
45462544	45
45462544	57
45462544	88
45462545	98
45462545	45
45462545	89
45462545	353
45462545	336
45462546	34
45462546	31
45462546	353
45462547	98
45462547	45
45462547	89
45462547	99
45462548	92
45462548	45
45462548	57
45462548	92
45462549	92
45462549	45
45462549	57
45462549	88
45462550	98
45462550	45
45462550	89
45462550	353
45462550	336
45462551	34
45462551	31
45462551	353
45462552	98
45462552	45
45462552	89
45462552	99
45462553	92
45462553	45
45462553	57
45462554	92
45462554	45
45462554	57
45462554	88
45462555	98
45462555	45
45462555	89
45462555	353
45462555	336
45462556	34
45462556	31
45462556	353
45462557	98
45462557	45
45462557	89
45462557	99
45462558	92
45462558	45
45462558	57
45462559	92
45462559	45
45462559	57
45462559	88
45462560	98
45462560	45
45462560	89
45462560	353
45462560	336
45462561	34
45462561	31
45462561	353
45462562	98
45462562	45
45462562	89
45462562	99
45462563	92
45462563	45
45462563	57
45462564	92
45462564	45
45462564	57
45462564	88
45462565	98
45462565	45
45462565	89
45462565	353
45462565	336
45462566	34
45462566	31
45462566	353
45462567	98
45462567	45
45462567	89
45462567	99
45462568	92
45462568	45
45462568	57
45462569	92
45462569	45
45462569	57
45462569	88
45462570	98
45462570	45
45462570	89
45462570	353
45462570	336
45462571	34
45462571	31
45462571	353
45462572	98
45462572	45
45462572	89
45462572	99
45462573	92
45462532	88
45462535	57
45462536	123
45462537	98
45462553	99
45462538	336
45462540	31
45462541	336
45462544	45
45462545	34
45462550	88
45462555	123
45462573	45
45462573	57
45462574	92
45462574	45
45462574	57
45462574	88
45462575	98
45462575	45
45462575	89
45462575	353
45462575	336
45462531	336
\.


--
-- Data for Name: история_входа; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."история_входа" ("Логин", "Тип входа", "Время входа", "Код входа") FROM stdin;
fedorov@namecomp.ru	успешно	2022-11-27 16:01:57.619243	\N
fedorov@namecomp.ru	успешно	2022-11-27 16:02:17.853108	\N
fedorov@namecomp.ru	успешно	2022-11-27 16:02:52.584991	\N
fedorov@namecomp.ru	успешно	2022-11-27 16:04:13.85064	\N
fedorov@namecomp.ru	успешно	2022-11-27 16:04:19.657653	\N
fedorov@namecomp.ru	успешно	2022-11-27 20:58:17.277044	\N
fedorov@namecomp.ru	успешно	2022-11-27 20:58:23.536656	\N
fedorov@namecomp.ru	успешно	2022-11-27 20:58:29.785663	\N
fedorov@namecomp.ru	успешно	2022-11-27 20:58:40.271168	\N
fedorov@namecomp.ru	успешно	2022-11-27 20:58:46.827382	\N
fedorov@namecomp.ru	успешно	2022-11-27 20:59:00.342307	\N
fedorov@namecomp.ru	успешно	2022-11-27 20:59:39.223071	\N
fedorov@namecomp.ru	успешно	2022-11-27 20:59:57.367983	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:00:50.177659	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:01:53.990518	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:02:35.071034	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:02:52.228826	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:03:28.327805	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:04:30.229047	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:04:49.229047	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:05:29.081452	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:05:45.13734	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:06:08.935509	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:06:26.527327	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:09:05.919622	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:09:53.148921	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:10:50.286553	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:12:59.889733	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:13:49.773106	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:15:47.628204	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:20:52.543539	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:21:24.726775	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:22:03.847171	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:23:09.557247	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:24:38.980826	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:27:57.05747	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:33:41.450238	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:36:41.64765	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:37:45.443626	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:45:10.306977	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:46:40.345988	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:47:52.998015	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:49:01.772522	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:56:05.64517	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:56:41.306956	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:56:49.838764	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:58:12.886022	\N
fedorov@namecomp.ru	успешно	2022-11-27 21:59:23.338099	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:01:31.692819	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:01:39.773937	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:02:12.735561	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:03:03.406262	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:03:23.765568	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:03:40.40455	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:03:49.586398	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:03:59.929979	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:05:04.805471	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:06:29.560469	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:06:55.355148	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:07:46.182351	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:07:58.787824	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:08:45.145789	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:39:00.543052	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:39:47.967023	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:41:09.937071	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:41:16.997192	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:41:26.76098	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:42:27.007134	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:42:33.705072	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:43:35.649854	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:57:16.334289	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:57:41.185122	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:57:49.415583	\N
fedorov@namecomp.ru	успешно	2022-11-27 22:58:02.762973	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:04:01.273087	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:04:10.910326	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:04:46.150741	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:04:53.108268	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:05:25.882844	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:07:21.471044	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:08:24.487881	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:09:02.536266	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:13:26.530674	\N
fedorov@namecomp.rutt	не успешно	2022-11-27 23:14:01.597535	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:14:04.764698	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:15:41.955393	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:16:00.226577	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:20:55.991804	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:21:43.94503	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:23:11.826555	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:25:46.892432	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:26:08.351082	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:26:27.740504	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:27:03.703365	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:27:10.663304	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:32:47.262087	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:34:00.261094	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:45:20.045467	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:45:32.799658	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:49:25.523172	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:50:57.186271	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:51:05.97636	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:51:18.21924	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:54:00.395697	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:55:46.661138	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:55:54.526759	\N
fedorov@namecomp.ru	успешно	2022-11-27 23:56:03.873011	\N
fedorov@namecomp.ru	успешно	2022-11-28 00:06:16.621215	\N
fedorov@namecomp.ru	успешно	2022-11-28 00:06:31.479057	\N
fedorov@namecomp.ru	успешно	2022-11-28 00:07:14.83779	\N
fedorov@namecomp.ru	успешно	2022-11-28 00:07:21.661887	\N
fedorov@namecomp.ru	успешно	2022-11-28 00:07:30.646039	\N
fedorov@namecomp.ru	успешно	2022-11-28 00:07:51.710333	\N
fedorov@namecomp.ru	успешно	2022-11-28 00:08:04.03799	\N
fedorov@namecomp.ru	успешно	2022-11-28 00:08:24.548353	\N
fedorov@namecomp.ru	успешно	2022-11-28 00:09:19.575541	\N
fedorov@namecomp.ru	успешно	2022-11-28 00:10:29.344461	\N
fedorov@namecomp.ru	успешно	2022-11-28 00:11:53.881816	\N
\.


--
-- Data for Name: клиенты; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."клиенты" ("ФИО", "Код клиента", "Паспортные данные", "Дата рождения", "Адрес", "Эл. почта", "Пароль") FROM stdin;
Фролов Андрей Иванович	45462526	Серия 1180 Номер 176596	2001-07-14	344288, г. Адлер, ул. Чехова, 1, кв. 34	gohufreilagrau-3818@yopmail.com	cl12345
Николаев Даниил Всеволодович	45462527	Серия 2280 Номер 223523	2001-02-10	614164, г. Адлер, ул. Степная, 30, кв. 75	xawugosune-1385@yopmail.com	cl12346
Снегирев Макар Иванович	45462528	Серия 4560 Номер 354155	1998-05-21	394242, г. Адлер, ул. Коммунистическая, 43, кв. 57	satrahuddusei-4458@yopmail.com	cl12347
Иванов Иван Ильич	45462529	Серия 9120 Номер 554296	1998-10-01	660540, г. Адлер, ул. Солнечная, 25, кв. 78	boippaxeufrepra-7093@yopmail.com	cl12348
Филиппова Анна Глебовна	45462530	Серия 2367 Номер 558134	1976-05-31	125837, г. Адлер, ул. Шоссейная, 40, кв. 92	zapramaxesu-7741@yopmail.com	cl12349
Иванов Михаил Владимирович	45462531	Серия 7101 Номер 669343	1985-11-04	125703, г. Адлер, ул. Партизанская, 49, кв. 84	rouzecroummegre-3899@yopmail.com	cl12350
Власов Дмитрий Александрович	45462532	Серия 3455 Номер 719630	1998-08-17	625283, г. Адлер, ул. Победы, 46, кв. 7	ziyeuddocrabri-4748@yopmail.com	cl12351
Серова Екатерина Львовна	45462533	Серия 2377 Номер 871623	1984-10-24	614611, г. Адлер, ул. Молодежная, 50, кв. 78	ketameissoinnei-1951@yopmail.com	cl12352
Борисова Ирина Ивановна	45462534	Серия 8755 Номер 921148	1976-10-14	454311, г. Адлер, ул. Новая, 19, кв. 78	yipraubaponou-5849@yopmail.com	cl12353
Зайцев Никита Артёмович	45462535	Серия 4355 Номер 104594	1999-10-14	660007, г. Адлер, ул. Октябрьская, 19, кв. 42	crapedocouca-3572@yopmail.com	cl12354
Медведев Святослав Евгеньевич	45462536	Серия 2791 Номер 114390	1985-07-13	603036, г. Адлер, ул. Садовая, 4, кв. 13	ceigoixakaunni-9227@yopmail.com	cl12355
Коротков Кирилл Алексеевич	45462537	Серия 5582 Номер 126286	1976-05-26	450983, г. Адлер, ул. Комсомольская, 26, кв. 60	yeimmeiwauzomo-7054@yopmail.com	cl12356
Калашникова Арина Максимовна	45462538	Серия 2978 Номер 133653	1999-08-13	394782, г. Адлер, ул. Чехова, 3, кв. 14	poleifenevi-1560@yopmail.com	cl12357
Минина Таисия Кирилловна	45462539	Серия 7512 Номер 141956	1985-10-13	603002, г. Адлер, ул. Дзержинского, 28, кв. 56	kauprezofautei-6607@yopmail.com	cl12358
Наумов Серафим Романович	45462540	Серия 5046 Номер 158433	1999-04-15	450558, г. Адлер, ул. Набережная, 30, кв. 71	quaffaullelourei-1667@yopmail.com	cl12359
Воробьева Василиса Евгеньевна	45462541	Серия 2460 Номер 169505	1999-01-13	394060, г. Адлер, ул. Фрунзе, 43, кв. 79	jsteele@rojas-robinson.net	cl12360
Калинин Александр Андреевич	45462542	Серия 3412 Номер 174593	1999-01-07	410661, г. Адлер, ул. Школьная, 50, кв. 53	vhopkins@lewis-mullen.com	cl12361
Кузнецова Милана Владиславовна	45462543	Серия 4950 Номер 183034	1999-01-24	625590, г. Адлер, ул. Коммунистическая, 20, кв. 34	nlewis@yahoo.com	cl12362
Фирсов Егор Романович	45462544	Серия 5829 Номер 219464	1993-09-02	625683, г. Адлер, ул. 8 Марта, 20, кв. 21	garciadavid@mckinney-mcbride.com	cl12363
Зимина Агния Александровна	45462545	Серия 6443 Номер 208059	1998-09-03	400562, г. Адлер, ул. Зеленая, 32, кв. 67	cbradley@castro.com	cl12364
Титов Андрей Глебович	45462546	Серия 7079 Номер 213265	1985-10-23	614510, г. Адлер, ул. Маяковского, 47, кв. 72	cuevascatherine@carlson.biz	cl12365
Орлов Николай Егорович	45462547	Серия 8207 Номер 522702	1985-07-27	410542, г. Адлер, ул. Светлая, 46, кв. 82	thomasmoore@wilson-singh.net	cl12366
Кузнецова Аиша Михайловна	45462548	Серия 9307 Номер 232158	1998-10-04	620839, г. Адлер, ул. Цветочная, 8, кв. 100	jessica84@hotmail.com	cl12367
Куликов Никита Георгиевич	45462549	Серия 1357 Номер 242839	1999-04-23	443890, г. Адлер, ул. Коммунистическая, 1, кв. 10	jessicapark@hotmail.com	cl12368
Карпова София Егоровна	45462550	Серия 1167 Номер 256636	1993-10-01	603379, г. Адлер, ул. Спортивная, 46, кв. 95	ginaritter@schneider-buchanan.com	cl12369
Смирнова Дарья Макаровна	45462551	Серия 1768 Номер 266986	1976-03-22	603721, г. Адлер, ул. Гоголя, 41, кв. 57	stephen99@yahoo.com	cl12370
Абрамова Александра Мироновна	45462552	Серия 1710 Номер 427875	1999-03-26	410172, г. Адлер, ул. Северная, 13, кв. 86	lopezlisa@hotmail.com	cl12371
Наумов Руслан Михайлович	45462553	Серия 1806 Номер 289145	1999-10-11	420151, г. Адлер, ул. Вишневая, 32, кв. 81	lori17@hotmail.com	cl12372
Бочаров Никита Матвеевич	45462554	Серия 1587 Номер 291249	1997-06-29	125061, г. Адлер, ул. Подгорная, 8, кв. 74	campbellkevin@gardner.com	cl12373
Соловьев Давид Ильич	45462555	Серия 1647 Номер 306372	1984-03-06	630370, г. Адлер, ул. Шоссейная, 24, кв. 81	morganhoward@clark.com	cl12374
Васильева Валерия Дмитриевна	45462556	Серия 1742 Номер 316556	1999-09-30	614753, г. Адлер, ул. Полевая, 35, кв. 39	carsontamara@gmail.com	cl12375
Макарова Василиса Андреевна	45462557	Серия 1474 Номер 326347	1999-04-08	426030, г. Адлер, ул. Маяковского, 44, кв. 93	kevinpatel@gmail.com	cl12376
Алексеев Матвей Викторович	45462558	Серия 1452 Номер 339539	1998-08-02	450375, г. Адлер, ул. Клубная, 44, кв. 80	sethbishop@yahoo.com	cl12377
Никитина Полина Александровна	45462559	Серия 2077 Номер 443480	1976-09-19	625560, г. Адлер, ул. Некрасова, 12, кв. 66	drollins@schultz-soto.net	cl12378
Окулова Олеся Алексеевна	45462560	Серия 2147 Номер 357518	1999-04-03	630201, г. Адлер, ул. Комсомольская, 17, кв. 25	pblack@copeland-winters.org	cl12379
Захарова Полина Яновна	45462561	Серия 2687 Номер 363884	1976-04-21	190949, г. Адлер, ул. Мичурина, 26, кв. 93	johnathon.oberbrunner@yahoo.com	cl12380
Зайцев Владимир Давидович	45462562	Серия 2376 Номер 443711	1998-01-26	350501, г. Адлер, ул. Парковая, 2, кв. 7	bradly29@gmail.com	cl12381
Иванов Виталий Даниилович	45462563	Серия 2568 Номер 386237	1976-08-11	450048, г. Адлер, ул. Коммунистическая, 21, кв. 3	stark.cristina@hilpert.biz	cl12382
Захаров Матвей Романович	45462564	Серия 2556 Номер 439376	1993-07-12	644921, г. Адлер, ул. Школьная, 46, кв. 37	bruen.eleanore@yahoo.com	cl12383
Иванов Степан Степанович	45462565	Серия 2737 Номер 407501	1998-09-19	614228, г. Адлер, ул. Дорожная, 36, кв. 54	percival.halvorson@yahoo.com	cl12384
Ткачева Милана Тимуровна	45462566	Серия 2581 Номер 441645	1998-05-24	350940, г. Адлер, ул. Первомайская, 23, кв. 2	javonte71@kuhlman.biz	cl12385
Семенов Даниил Иванович	45462567	Серия 2675 Номер 427933	1976-01-04	344990, г. Адлер, ул. Красноармейская, 19, кв. 92	vconnelly@kautzer.com	cl12386
Виноградов Вячеслав Дмитриевич	45462568	Серия 2967 Номер 434531	1976-07-12	410248, г. Адлер, ул. Чкалова, 11, кв. 75	anabelle07@schultz.info	cl12387
Соболева Николь Фёдоровна	45462569	Серия 3070 Номер 449655	1976-05-02	400839, г. Адлер, ул. 8 Марта, 46, кв. 44	nitzsche.katlynn@yahoo.com	cl12388
Тихонова Анна Львовна	45462570	Серия 3108 Номер 451174	1985-03-23	450539, г. Адлер, ул. Заводская, 3, кв. 81	corine16@von.com	cl12389
Кузнецова Ульяна Савельевна	45462571	Серия 3250 Номер 464705	1999-06-03	614591, г. Адлер, ул. Цветочная, 20, кв. 40	otha.wisozk@lubowitz.org	cl12390
Смирнова Анна Германовна	45462572	Серия 3392 Номер 471644	1997-07-18	400260, г. Адлер, ул. Больничная, 30, кв. 53	may.kirlin@hotmail.com	cl12391
Черепанова Анна Давидовна	45462573	Серия 3497 Номер 487819	1985-11-06	660924, г. Адлер, ул. Молодежная, 32, кв. 59	bryana.kautzer@yahoo.com	cl12392
Григорьев Максим Кириллович	45462574	Серия 3560 Номер 491260	1999-05-26	644133, г. Адлер, ул. Гагарина, 28, кв. 69	deborah.christiansen@quigley.biz	cl12393
Голубев Даниэль Александрович	45462575	Серия 3620 Номер 506034	1999-06-14	450698, г. Адлер, ул. Вокзальная, 14, кв. 37	connelly.makayla@yahoo.com	cl12394
Миронов Юрий Денисович	45462576	Серия 3774 Номер 511438	1985-01-26	620653, г. Адлер, ул. Западная, 15, кв. 25	tatum.collins@fay.org	cl12395
Терехов Михаил Андреевич	45462577	Серия 3862 Номер 521377	1976-07-06	644321, г. Адлер, ул. Клубная, 32, кв. 10	itzel73@anderson.com	cl12396
Орлова Алиса Михайловна	45462578	Серия 3084 Номер 535966	1997-02-24	603653, г. Адлер, ул. Молодежная, 2, кв. 45	arjun39@hotmail.com	cl12397
Кулаков Константин Даниилович	45462579	Серия 4021 Номер 541528	1993-06-20	410181, г. Адлер, ул. Механизаторов, 16, кв. 74	ohara.rebeka@yahoo.com	cl12398
Кудрявцев Максим Романович	45462580	Серия 4109 Номер 554053	1998-05-10	394207, г. Адлер, ул. Свердлова, 31, кв. 28	danika58@rath.com	cl12399
Соболева Кира Фёдоровна	45462581	Серия 4537 Номер 564868	1998-03-14	420633, г. Адлер, ул. Матросова, 18, кв. 41	janae.bogan@gmail.com	cl12400
Коновалов Арсений Максимович	45462582	Серия 4914 Номер 572471	1985-02-18	445720, г. Адлер, ул. Матросова, 50, кв. 67	vern91@yahoo.com	cl12401
Гусев Михаил Дмитриевич	45462583	Серия 4445 Номер 581302	1999-11-23	400646, г. Адлер, ул. Октябрьская, 47, кв. 65	mariana.leannon@larkin.net	cl12402
Суханова Варвара Матвеевна	45462584	Серия 4743 Номер 598180	1993-09-13	644410, г. Адлер, ул. Красная, 17, кв. 69	vmoore@gmail.com	cl12403
Орлова Ясмина Васильевна	45462585	Серия 4741 Номер 601821	1984-06-24	400750, г. Адлер, ул. Школьная, 36, кв. 71	damon.mcclure@mills.com	cl12404
Васильева Ксения Константиновна	45462586	Серия 4783 Номер 612567	1999-08-01	660590, г. Адлер, ул. Дачная, 37, кв. 70	grady.reilly@block.com	cl12405
Борисова Тамара Данииловна	45462587	Серия 4658 Номер 621200	1993-05-29	426083, г. Адлер, ул. Механизаторов, 41, кв. 26	boyd.koss@yahoo.com	cl12406
Дмитриев Мирон Ильич	45462588	Серия 4908 Номер 634613	1985-04-13	410569, г. Адлер, ул. Парковая, 36, кв. 17	obartell@franecki.info	cl12407
Лебедева Анна Александровна	45462589	Серия 5092 Номер 642468	1985-03-30	443375, г. Адлер, ул. Дзержинского, 50, кв. 95	reina75@ferry.net	cl12408
Пономарев Артём Маркович	45462590	Серия 5155 Номер 465274	1984-06-02	614316, г. Адлер, ул. Первомайская, 48, кв. 31	karson28@hotmail.com	cl12409
Борисова Елена Михайловна	45462591	Серия 5086 Номер 666893	1976-05-23	445685, г. Адлер, ул. Зеленая, 7, кв. 47	damaris61@okon.com	cl12410
Моисеев Камиль Максимович	45462592	Серия 5333 Номер 675375	1999-06-17	614505, г. Адлер, ул. Нагорная, 37, кв. 31	carroll.jerod@hotmail.com	cl12411
Герасимова Дарья Константиновна	45462593	Серия 5493 Номер 684572	1984-10-13	426629, г. Адлер, ул. Весенняя, 32, кв. 46	ron.treutel@quitzon.com	cl12412
Михайлова Мария Марковна	45462594	Серия 5150 Номер 696226	1976-12-02	603743, г. Адлер, ул. Матросова, 19, кв. 20	olen79@yahoo.com	cl12413
Коршунов Кирилл Максимович	45462595	Серия 1308 Номер 703305	1985-05-22	450750, г. Адлер, ул. Клубная, 23, кв. 90	pacocha.robbie@yahoo.com	cl12414
\.


--
-- Data for Name: сотрудники; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."сотрудники" ("Код сотрудника", "Должность", "ФИО", "Логин", "Пароль", "Последний вход", "Тип входа") FROM stdin;
101	Продавец	Иванов Иван Иванович	Ivanov@namecomp.ru	2L6KZG	2022-11-04 13:13:00	Успешно
102	Продавец	Петров Петр Петрович	petrov@namecomp.ru	uzWC67	2022-11-04 13:13:00	Успешно
103	Администратор	Федоров Федор Федорович	fedorov@namecomp.ru	8ntwUp	2022-11-04 13:13:00	Успешно
104	Старший смены	Миронов Вениамин Куприянович	mironov@namecomp.ru	YOyhfR	2022-11-04 13:13:00	Успешно
105	Старший смены	Ширяев Ермолай Вениаминович	shiryev@namecomp.ru	RSbvHv	2022-11-04 13:13:00	Неуспешно
106	Старший смены	Игнатов Кассиан Васильевич	ignatov@namecomp.ru	rwVDh9	2022-11-04 13:13:00	Успешно
107	Продавец	Хохлов Владимир Мэлсович	hohlov@namecomp.ru	LdNyos	2022-11-04 13:13:00	Успешно
108	Продавец	Стрелков Мстислав Георгьевич	strelkov@namecomp.ru	gynQMT	2022-11-04 13:13:00	Неуспешно
109	Продавец	Беляева Лилия Наумовна	belyeva@@namecomp.ru	AtnDjr	2022-11-04 13:13:00	Успешно
110	Продавец	Смирнова Ульяна Гордеевна	smirnova@@namecomp.ru	JlFRCZ	2022-11-04 13:13:00	Успешно
\.


--
-- Data for Name: товары; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."товары" ("Код товара", "Наименование", "Изображение", "Стоимость, руб. за час", "Полная стоимость", "Описание", "Оставшееся кол-во", "Категория") FROM stdin;
353	Сумеречная борьба	Sumerechnaya_Borba-1024x1024-wm.jpg	500	5500	"Сумеречная борьба" – это абсолютный хит среди настольных игр, который вот уже много лет занимает верхние строчки мировых рейтингов. Участвуйте в космической гонке, делите мир на сферы влияния, организовывайте локальные военные конфликты и восстания, но не позвольте им перерасти в Третью мировую войну. Если Часы Судного Дня пробьют полночь, то оба игрока проиграют.	1	Стратегические
34	Similo: Мифы	\N	50	490	Зевс, Дионис, Ахиллес, Пандора, Минотавр и многие другие жаждут проверить вашу логику. "Similo: Мифы" является полностью самостоятельной игрой, но её можно совместить с другими частями серии, чтобы сделать игровой процесс ещё более увлекательным.	5	Вечериночные
99	Маленький мир	Small-World_3D_roznica-1024x1024-wm.jpg	300	4490	Small World или иначе "Маленький мир" – это одна из самых известных настольных игр, появившаяся в 2009 году и до сих пор не теряющая своей популярности. Игра относится к стратегическим играм, одновременно сочетая в себе серьёзные механики с озорным подходом к сеттингу и жанру в целом. Достаточно просто посмотреть на дизайн персонажей, чтобы полностью проникнуться атмосферой игры.	2	Стратегические
45	Битва боевых магов: Битва на горе Черепламени	\N	150	1490	"Эпичные схватки боевых магов: Битва на горе Черепламени" – уникальная по своему стилю карточная игра на составление комбинаций заклинаний. Игра наполнена чёрным юмором и потрясающими иллюстрациями Ника Эдвардса с подчёркнутым садизмом и гротескной жестокостью. Игра компактна и проста в освоении, но при этом подарит вам массу эмоций и настоящего угара! Подобных игр вы ещё не видели, это точно!	5	Вечериночные
92	Битва за Рокуган	bitva-za-rokugan_3D_roznica-1024x1024-wm.jpg	250	2990	Захватите королевство и принесите честь и славу для своего клана в битве за Рокуган! В этой стратегической игре о завоеваниях земель и войнах за них, игроки оказываются в ролях настоящих даймё великих японских кланов, которые борются за богатые ресурсами земли Изумрудной Империи. Главы кланов должны грамотно распоряжаться доступными ресурсами, мудро планировать атаки своих армий и быть на шаг впереди своих соперников, чтобы вырвать уверенную победу.	1	Стратегические
44	Космический контакт	Cosmic_Encounter_1-1024x1024-wm.jpg	600	4490	"Космический контакт" – стратегическая игра о межпланетных разборках, которая уже давно обрела культовый статус и завоевала сердца сотен фанатов. Если вы ещё не успели познакомиться с очаровательным и динамичным миром "Космического контакта", то самое время обратить внимание на новое, юбилейное издание легендарной настольной игры и принять участие в уникальном состязании за власть над галактикой!	0	Стратегические
98	Манчкин	Munchkin00-1024x1024-wm.jpg	200	1290	Игра "Манчкин" – локализация настольной карточной игры Munchkin. На русском языке игра, как ни старайся, приобретает новое звучание, но остаётся по-прежнему азартной, динамичной и злорадной. Ролевое зубоскальство по простым, но местами намеренно туманным правилам подвергает насмешкам благородных эльфов, мудрых магов, отважных воинов и мохноногих хафлингов.	7	Вечериночные
31	Корова 006	\N	100	790	"Корова 006" – динамичная настольная игра для тех, кто ценит сочетание расчёта и удачи. Простые и элегантные правила делают игру одновременно лёгкой и увлекательной, а оригинальные иллюстрации придают ей особое обаяние. "Корова 006" – хороший повод собраться с друзьями или в кругу семьи и отлично провести время. Почему нам так нравится "Корова 006"?	3	Карточные
57	Цитадели	Citadeli_201700-1024x1024-wm.jpg	200	990	В "Цитаделях" игроки соревнуются за право называться главным строителем королевства. Для этого нужно впечатлить монарха незаурядными навыками и заручиться поддержкой вельмож и богачей.	1	Стратегические
88	Сиггил	\N	100	590	Перенесёмся в сказочно-чарующий, тёплый и немного мрачный мир духов. И сегодня большой день – вам в качестве Посвящённого предстоит показать всё, чему вы научились, но помните, что это может быть опасно… Чтобы пройти испытание, вам необходимо открыть сиггил, освободить всех духов, заключённых в нём, и пленить их вновь! Покажите своё мастерство и докажите, что именно вы освоили уроки своих мудрых наставников лучше всех!	2	Карточные
336	Взрывные котята	vzryvnye_kotyata_2022-1024x1024-wm.jpg	150	890	"Взрывные котята" – это нашумевший карточный хит с площадки "Кикстартер", где он побил все мыслимые рекорды и сразу же влюбил в себя более двухсот тысяч человек по всему миру. Игра крайне проста в освоении и отличается уникальным дизайном, вы точно влюбитесь в этих прекрасных рисованных котят!	3	Вечериночные
89	Битва боевых магов: Крутаггидон	ESW_Deckbuilding_box_3d-roznica-1024x1024-wm.jpg	150	1390	Близится ежегодное состязание Крутагидона! Каждый, хоть чего-то стоящий колдун, готов побороться за приз, прекрасно понимая, что жуткая смерть с расчленением ждёт всех и каждого, и даже победителя раз-другой да покромсают! И пускай вы начнёте бой с одной лишь хилой волшебной палочкой в руках, по ходу состязания вы будете добавлять в свою колоду всё больше новых и мощных карт, которые помогут вам одолеть как обычных врагов, так и легендарных магов (предыдущих победителей турнира). Это ведь эпичные схватки, вы не забыли!?	4	Карточные
123	Пэчворк	patchwork_main-1024x1024-wm.jpg	170	1190	Приятнее всего спать под лоскутным одеялом, потому что оно сделано своими руками. В игре "Пэчворк" двум игрокам предстоит попробовать себя в лоскутном шитье, и, хотя, номинально один из них будет назван победителем, удовольствие от игры получат все.	3	Абстрактные
\.


--
-- Name: заказы заказы_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."заказы"
    ADD CONSTRAINT "заказы_pk" PRIMARY KEY ("Код заказа");


--
-- Name: клиенты клиенты_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."клиенты"
    ADD CONSTRAINT "клиенты_pk" PRIMARY KEY ("Код клиента");


--
-- Name: сотрудники сотрудники_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."сотрудники"
    ADD CONSTRAINT "сотрудники_pk" PRIMARY KEY ("Код сотрудника");


--
-- Name: товары товары_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."товары"
    ADD CONSTRAINT "товары_pk" PRIMARY KEY ("Код товара");


--
-- Name: заказы заказы_fk; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."заказы"
    ADD CONSTRAINT "заказы_fk" FOREIGN KEY ("Код клиента") REFERENCES public."клиенты"("Код клиента") ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: заказы заказы_сотрудники_fk; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."заказы"
    ADD CONSTRAINT "заказы_сотрудники_fk" FOREIGN KEY ("Код сотрудника") REFERENCES public."сотрудники"("Код сотрудника") ON UPDATE SET NULL ON DELETE SET NULL;


--
-- Name: заказы_товары заказы_товары_fk; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."заказы_товары"
    ADD CONSTRAINT "заказы_товары_fk" FOREIGN KEY ("Код заказа") REFERENCES public."заказы"("Код заказа") ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: заказы_товары заказы_товары_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."заказы_товары"
    ADD CONSTRAINT "заказы_товары_fk_1" FOREIGN KEY ("Код товара") REFERENCES public."товары"("Код товара") ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

