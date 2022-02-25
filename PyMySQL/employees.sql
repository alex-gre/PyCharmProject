-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- Хост: 127.0.0.1
-- Время создания: Фев 25 2022 г., 18:06
-- Версия сервера: 5.5.25
-- Версия PHP: 5.3.13

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База данных: `employees`
--

-- --------------------------------------------------------

--
-- Структура таблицы `employee_data`
--

CREATE TABLE IF NOT EXISTS `employee_data` (
  `emp_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `f_name` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `l_name` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `title` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `yos` int(11) DEFAULT NULL,
  `salary` int(11) DEFAULT NULL,
  `perks` int(11) DEFAULT NULL,
  `email` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`emp_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=21 ;

--
-- Дамп данных таблицы `employee_data`
--

INSERT INTO `employee_data` (`emp_id`, `f_name`, `l_name`, `title`, `age`, `yos`, `salary`, `perks`, `email`) VALUES
(1, 'John', 'Hagan', 'Senior Programmer', 32, 4, 120000, 25000, 'john_hagan@bignet.com'),
(2, 'Ganesh', 'Pillai', 'Senior Programmer', 32, 4, 110000, 20000, 'g_pillai@bignet.com'),
(3, 'Anamika', 'Pandit', 'Web Designer', 27, 3, 90000, 15000, 'ana@bignet.com'),
(4, 'Mary', 'Anchor', 'Web Designer', 26, 2, 85000, 15000, 'mary@bignet.com'),
(5, 'Fred', 'Kruger', 'Programmer', 31, 3, 75000, 15000, 'fk@bignet.com'),
(6, 'John', 'MacFarland', 'Programmer', 34, 4, 80000, 16000, 'john@bignet.com'),
(7, 'Edward', 'Sakamuro', 'Programmer', 25, 2, 75000, 14000, 'eddie@bignet.com'),
(8, 'Alok', 'Nanda', 'Programmer', 32, 3, 70000, 10000, 'alok@bignet.com'),
(9, 'Hassan', 'Rajabi', 'Multimedia Programmer', 33, 3, 90000, 15000, 'hasan@bignet.com'),
(10, 'Paul', 'Simon', 'Multimedia Programmer', 43, 2, 85000, 12000, 'ps@bignet.com'),
(11, 'Arthur', 'Hoopla', 'Multimedia Programmer', 32, 1, 75000, 15000, 'arthur@bignet.com'),
(12, 'Kim', 'Hunter', 'Senior Web Designer', 32, 2, 110000, 20000, 'kim@bignet.com'),
(13, 'Roger', 'Lewis', 'System Administrator', 35, 2, 100000, 13000, 'roger@bignet.com'),
(14, 'Danny', 'Gibson', 'System Administrator', 34, 1, 90000, 12000, 'danny@bignet.com'),
(15, 'Mike', 'Harper', 'Senior Marketing Executive', 36, 2, 120000, 28000, 'mike@bignet.com'),
(16, 'Monica', 'Sehgal', 'Marketing Executive', 30, 3, 90000, 25000, 'monica@bignet.com'),
(17, 'Hal', 'Simlai', 'Marketing Executive', 27, 2, 70000, 18000, 'hal@bignet.com'),
(18, 'Joseph', 'Irvine', 'Marketing Executive', 27, 2, 72000, 18000, 'joseph@bignet.com');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
