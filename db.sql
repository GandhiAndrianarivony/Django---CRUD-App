-- Create database
CREATE DATABASE blog;

-- Create user which is assigned to this previous database i.e
CREATE USER blogadmin WITH ENCRYPTED PASSWORD 'django_password';

-- 
ALTER ROLE blogadmin SET client_encoding TO 'utf8';
ALTER ROLE blogadmin SET default_transaction_isolation TO 'read committed';

-- Grant blog db access to blogadmin
GRANT ALL PRIVILEGES ON DATABASE blog TO blogadmin;
