-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema e-wallet
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema e-wallet
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `e-wallet` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `e-wallet` ;

-- -----------------------------------------------------
-- Table `e-wallet`.`cards`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `e-wallet`.`cards` (
  `card_id` INT NOT NULL,
  `cardholder_id` INT NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `balance` VARCHAR(45) NOT NULL,
  `number` INT(16) NOT NULL,
  `expiration_date` VARCHAR(5) NOT NULL,
  `cvv_code` INT NOT NULL,
  `design` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`card_id`),
  INDEX `cardholder_id_idx` (`cardholder_id` ASC) VISIBLE,
  CONSTRAINT `cardholder_id`
    FOREIGN KEY (`cardholder_id`)
    REFERENCES `e-wallet`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `e-wallet`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `e-wallet`.`users` (
  `user_id` INT NOT NULL,
  `password` VARCHAR(200) NOT NULL,
  `firstname` VARCHAR(45) NOT NULL,
  `lastname` VARCHAR(45) NOT NULL,
  `phone_number` VARCHAR(45) NOT NULL,
  `credit_card_id` INT NULL,
  `debit_card_id` INT NULL,
  `role` VARCHAR(5) NOT NULL,
  `username` VARCHAR(20) NOT NULL,
  `transaction_ids` VARCHAR(1000) NULL,
  PRIMARY KEY (`user_id`),
  INDEX `credit_card_id_idx` (`credit_card_id` ASC) VISIBLE,
  INDEX `debit_card_id_idx` (`debit_card_id` ASC) VISIBLE,
  CONSTRAINT `credit_card_id`
    FOREIGN KEY (`credit_card_id`)
    REFERENCES `e-wallet`.`cards` (`card_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `debit_card_id`
    FOREIGN KEY (`debit_card_id`)
    REFERENCES `e-wallet`.`cards` (`card_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `e-wallet`.`transactions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `e-wallet`.`transactions` (
  `transaction_id` INT NOT NULL,
  `sender_id` INT NULL,
  `receiver_id` INT NULL,
  `amount` INT NULL,
  `currency` VARCHAR(45) NULL,
  `category` VARCHAR(45) NULL,
  `card_id` INT NULL,
  `timestamp` DATETIME NULL,
  PRIMARY KEY (`transaction_id`),
  INDEX `sender_id_idx` (`sender_id` ASC) VISIBLE,
  INDEX `receiver_id_idx` (`receiver_id` ASC) VISIBLE,
  INDEX `card_id_idx` (`card_id` ASC) VISIBLE,
  CONSTRAINT `sender_id`
    FOREIGN KEY (`sender_id`)
    REFERENCES `e-wallet`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `receiver_id`
    FOREIGN KEY (`receiver_id`)
    REFERENCES `e-wallet`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `card_id`
    FOREIGN KEY (`card_id`)
    REFERENCES `e-wallet`.`cards` (`card_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `e-wallet`.`contact_lists`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `e-wallet`.`contact_lists` (
  `user_id` INT NOT NULL,
  `contacts` VARCHAR(1000) NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
