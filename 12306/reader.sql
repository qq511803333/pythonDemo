CREATE TABLE `reader` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_station` varchar(10) DEFAULT NULL,
  `end_station` varchar(10) DEFAULT NULL,
  `train_date` date DEFAULT NULL,
  `seat` varchar(10) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8