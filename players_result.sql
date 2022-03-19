-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 09, 2020 at 03:20 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `game_detail`
--

-- --------------------------------------------------------

--
-- Table structure for table `players_result`
--

CREATE TABLE `players_result` (
  `name` varchar(20) DEFAULT NULL,
  `Total_Questions` int(255) DEFAULT NULL,
  `Correct_Questions` int(255) DEFAULT NULL,
  `Percentage` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `players_result`
--

INSERT INTO `players_result` (`name`, `Total_Questions`, `Correct_Questions`, `Percentage`) VALUES
('Rashmi', 5, 4, '80.0'),
('warun', 4, 2, '50.0'),
('rash', 8, 3, '37.5'),
('tiyara', 2, 0, '0.0'),
('uwan', 5, 4, '80.0'),
('wayana', 3, 3, '100.0');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
