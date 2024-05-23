-- Drone Flight Management System Database
-- Test Data
-- Inserts mock data into the database to test functionality
-- Run corresponding 'databasemodel.sql' before this script

USE `dfmsDB`;

INSERT INTO accounts (account_id, username, password, first_name, last_name)
VALUES
	(1, 'firstUser', '$2y$10$KuICCFeBrH54nm4vE.5cYekd.FZSCW4lJke8yg.9PDmrmG6F61hDq', 'John', 'Doe'),
	(2, 'secondUser', '$2y$10$vkJl6pPKX8FhcXd8XSfgvesWu9bwVWKNAuhAgg9hvEIYXNIh19IUu', 'Jane', 'Doe'),
	(3, 'thirdUser', '$2y$10$R2LomiOQmKwIjbMPQFihM.V3rn15fLiwtkoaduflFTCZwf2luyFY.', 'Joe', 'Schmoe'),
	(4, 'fourthUser', '$2y$10$KuICCFeBrH54nm4vE.5cYekd.FZSCW4lJke8yg.9PDmrmG6F61hDq', 'John', 'Smith'),
	(5, 'fifthUser', '$2y$10$vkJl6pPKX8FhcXd8XSfgvesWu9bwVWKNAuhAgg9hvEIYXNIh19IUu', 'Jane', 'Smith'),
	(6, 'sixthUser', '$2y$10$R2LomiOQmKwIjbMPQFihM.V3rn15fLiwtkoaduflFTCZwf2luyFY.', 'Joe', 'Bloggs'),
	(7, 'seventhUser', '$2y$10$KuICCFeBrH54nm4vE.5cYekd.FZSCW4lJke8yg.9PDmrmG6F61hDq', 'Average', 'Joe'),
	(8, 'eighthUser', '$2y$10$vkJl6pPKX8FhcXd8XSfgvesWu9bwVWKNAuhAgg9hvEIYXNIh19IUu', 'Jane', 'Doe'),
	(9, 'ninthUser', '$2y$10$R2LomiOQmKwIjbMPQFihM.V3rn15fLiwtkoaduflFTCZwf2luyFY.', 'Some', 'Guy'),
	(10, 'tenthUser', '$2y$10$KuICCFeBrH54nm4vE.5cYekd.FZSCW4lJke8yg.9PDmrmG6F61hDq', 'Random', 'Dude'),
	(11, 'eleventhUser', '$2y$10$vkJl6pPKX8FhcXd8XSfgvesWu9bwVWKNAuhAgg9hvEIYXNIh19IUu', 'Some', 'One'),
	(12, 'twelvethUser', '$2y$10$R2LomiOQmKwIjbMPQFihM.V3rn15fLiwtkoaduflFTCZwf2luyFY.', 'Test', 'User');

INSERT INTO base (base_id, location, rpa_count, maintainer_count)
VALUES
	(1, 'UnitedStates', 4, 5),
	(2, 'GreatBritain', 3, 2),
	(3, 'Australia', 5, 3);

INSERT INTO devices (device_id, account, last_login, still_authorized)
VALUES
	(1, 1, '2024-04-09 14:30:00', 1),
	(2, 2, '2024-04-08 12:12:00', 0),
	(3, NULL, '2024-04-07 10:45:00', 0);

INSERT INTO organization (organization_id, name, base)
VALUES
	(1, '14th Squadron', 1),
	(2, '10th Squadron', 2),
	(3, '5th Squadron', 3);

INSERT INTO pilot (pilot_id, organization, last_training, status)
VALUES
	(1, 1, '2024-04-01 10:00:00', 'ON LEAVE'),
	(2, 2, '2024-04-01 10:00:00', 'AVAILABLE'),
	(3, 3, '2024-04-01 10:00:00', 'TASKED');

INSERT INTO sensor_operator (sensor_id, organization, last_training, status)
VALUES
	(4, 1, '2024-04-01 10:00:00', 'ON LEAVE'),
	(5, 2, '2024-04-01 10:00:00', 'AVAILABLE'),
	(6, 3, '2024-04-01 10:00:00', 'TASKED');

INSERT INTO maintainer (maintainer_id, organization, last_training, status, base)
VALUES
	(7, 1, '2024-04-01 10:00:00', 'ON LEAVE', 1),
	(8, 2, '2024-04-01 10:00:00', 'AVAILABLE', 2),
	(9, 3, '2024-04-01 10:00:00', 'TASKED', 3);

INSERT INTO planner (planner_id, organization, status)
VALUES
	(10, 1, 'ON LEAVE'),
	(11, 2, 'AVAILABLE'),
	(12, 3, 'TASKED');

INSERT INTO remotely_piloted_aircraft (rpa_id, model_name, manufacturer, pilot, sensor_operator, maintainer, base)
VALUES
	(1, 'MQ-9', 'General Atomics', 1, 4, 7, 1),
	(2, 'MQ-1', 'General Atomics', 2, 5, 8, 2),
	(3, 'RQ-4', 'Northrop Grumman', 3, 6, 9, NULL);

INSERT INTO maintenance_appointment (appointment_id, rpa, maintainer, scheduled_time)
VALUES
	(1, 1, 7, '2024-04-09 16:00:00'),
	(2, 2, 8, '2024-04-06 16:00:00'),
	(3, 3, 9, '2024-04-03 16:00:00');

INSERT INTO maintenance_log (rpa, appointment, start_time, end_time, status)
VALUES
	(1, 1, '2024-04-09 16:05:00', NULL, 'IN PROGRESS'),
	(2, 2, '2024-04-06 16:10:00', '2024-04-06 20:00:00', 'COMPLETED'),
	(3, 3, '2024-04-03 16:00:00', '2024-04-06 20:10:00', 'COMPLETED');

INSERT INTO payload (payload_id, weightlbs, pylon_count)
VALUES
	(1, 2000, 4),
	(2, 1200, 2),
	(3, 0, 0);

INSERT INTO flight_plan (plan_id, planner, waypoints, launch_base, recovery_base, payload)
VALUES
	(1, 10, '11S 2796 3254', 3, 1, 1),
	(2, 11, '15T 2543 2557', 2, 2, 2),
	(3, 12, '17R 5345 2123', 1, 3, 3);

INSERT INTO mission (mission_id, flight_plan, rpa, task)
VALUES
	(1, 1, 1, 'ISR'),
	(2, 2, 2, 'BAI'),
	(3, 3, 3, 'ISR');

INSERT INTO sortie (sortie_id, mission, rpa, launch_time, recovery_time)
VALUES
	(1, 1, 1, '2024-04-04 16:05:00', '2024-04-04 20:10:00'),
	(2, 2, 2, '2024-04-07 16:10:00', '2024-04-07 20:00:00'),
	(3, 3, 3, '2024-04-09 16:00:00', NULL);

INSERT INTO flight_log (rpa, sortie, flight_time)
VALUES
	(1, 1, '04:05:00'),
	(2, 2, '03:50:00'),
	(3, 3, '03:37:54');