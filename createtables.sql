CREATE TABLE Organization								-- Table to store info related to organization
(
Org_ID int IDENTITY(1,1) NOT NULL,
OrgName varchar(255) NOT NULL							-- Name of org
PRIMARY KEY (Org_ID)
);

CREATE TABLE Person										-- Table to store user information
(
Person_ID int IDENTITY(1,1) NOT NULL,					-- Primary key autonumber
FirstName varchar(255) NOT NULL,						-- First name of user
LastName varchar(255) NOT NULL,							-- Last name of user
UserName varchar(255) NOT NULL,
EmailAddress varchar(255) NOT NULL,
PRIMARY KEY (Person_ID)									-- Set primary key
);

CREATE TABLE OrganizationOwner							-- Table to store organization owners (admins)
(
Org_ID int NOT NULL,
Person_ID int NOT NULL,
FOREIGN KEY (Org_ID) REFERENCES Organization(Org_ID),
FOREIGN KEY (Person_ID) REFERENCES Person(Person_ID)
);

CREATE TABLE PersonOrganization							-- Table to store people who exist in organization
(
Person_ID int NOT NULL,
Org_ID int NOT NULL,
FOREIGN KEY (Person_ID) REFERENCES Person(Person_ID),
FOREIGN KEY (Org_ID) REFERENCES Organization(Org_ID)
);

CREATE TABLE LookingForWork 							-- Table to identify if user is available for work
(
Person_ID int NOT NULL,									-- Foreign Key from People table
IsAvailable bool NOT NULL DEFAULT 0,					-- Yes/No is user available for work, defaults to no
FOREIGN KEY (Person_ID) REFERENCES Person(Person_ID)	-- Foreign key to People table
);

CREATE TABLE Category								-- Table to store skill group info
(
Category_ID int IDENTITY(1,1) NOT NULL,			-- Primary key autonumber
CategoryName varchar(255) NOT NULL,					-- Name of skill group
CategoryDesc text,									-- General description of skill group
PRIMARY KEY (Category_ID)							-- Set primary key
);

/* Commented out (Anthony) because this probably isn't necessary in v1

	CREATE TABLE Skill									-- Table to store skills info
	(
	Skill_ID int NOT NULL auto_increment,				-- Primary key			
	SkillName varchar(255) NOT NULL,					-- Name of skill
	SkillDesc text,										-- General description of skill
	PRIMARY KEY (Skill_ID)
	);
*/


-- Do we add a rating system? (Anthony)
/*
CREATE TABLE Expertise								-- Table to store levels of expertise
(
Expertise_ID int NOT NULL auto_increment,			-- Primary key
ExpertiseName varchar(255) NOT NULL,				-- Name of level of expertise
ExpertiseDesc text,									-- Description of level of expertise
PRIMARY KEY (Expertise_ID)
);

*/

/* Further skills commented out for v1 (Anthony)

CREATE TABLE SkillCategory							-- Identify which skills belong to what category
(
Category_ID int NOT NULL,							-- Foreign key from Category table
Skill_ID int NOT NULL,								-- Foreign key from Skill table
FOREIGN KEY (Category_ID) REFERENCES Category(Category_ID),
FOREIGN KEY (Skill_ID) REFERENCES Skill(Skill_ID)
);

CREATE TABLE UserSkill								-- Store persons skills and expertisee
(
Person_ID int NOT NULL,
Skill_ID int NOT NULL,
Expertise_ID int NOT NULL,
FOREIGN KEY (Person_ID) REFERENCES Person(Person_ID),
FOREIGN KEY (Skill_ID) REFERENCES Skill(Skill_ID),
FOREIGN KEY (Expertise_ID) REFERENCES Expertise(Expertise_ID)
);

*/

CREATE TABLE Request								-- Requests
(
Request_ID int IDENTITY(1,1) NOT NULL,				-- Primary key
RequestName varchar(255),							-- Name of request
RequestDesc text,									-- Descripton of request
RequestTime float(6, 2),							-- Time request will take
RequestMaxPeople tinyint,							-- Amount of people for request
IsRequestFilled bool DEFAULT 0,						-- Is request filled
IsRequestComplete bool DEFAULT 0,					-- Is request complete
PRIMARY KEY (Request_ID)
);

CREATE TABLE UserRequest							-- Table associates request with user
(
Person_ID int NOT NULL,
Request_ID int NOT NULL,
FOREIGN KEY (Person_ID) REFERENCES Person(Person_ID),
FOREIGN KEY (Request_ID) REFERENCES Request(Request_ID)
);

/* Skills commented out

CREATE TABLE RequestSkill							-- Table associates requests with skills
(
Request_ID int NOT NULL,
Skill_ID int NOT NULL,
FOREIGN KEY (Request_ID) REFERENCES Request(Request_ID),
FOREIGN KEY (Skill_ID) REFERENCES Skill(Skill_ID)
);

*/

CREATE TABLE TaskAccept								-- Table tracks who accepts what
(
Request_ID int NOT NULL,
Person_ID int NOT NULL,
FOREIGN KEY (Request_ID) REFERENCES Request(Request_ID),
FOREIGN KEY (Person_ID) REFERENCES Person(Person_ID)
);