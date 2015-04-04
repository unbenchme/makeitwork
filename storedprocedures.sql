USE UnBenchMe
GO

CREATE PROCEDURE addRequest(
@rname varchar(255),
@rdesc text,
@rtime float(6,2),
@rmaxpeople tinyint,
@p_id int)
AS
BEGIN
	DECLARE @r_id int;
	-- Inserts new request
	INSERT INTO Request(
						RequestName,
                        RequestDesc,
                        RequestTime,
                        RequestMaxPeople)
				Values(
						@rname,
                        @rdesc,
                        @rtime,
                        @rmaxpeople);
	SET @r_id = @@IDENTITY;
	-- Associates user with request
	INSERT INTO UserRequest(
							Person_ID,
                            Request_ID)
				Values(
						@p_id,
                        @r_id);

END

/* Won't need this in v1 w/ skills (Anthony)

USE UnBenchMe
GO

CREATE PROCEDURE addRequestSkill(
r_id int,	
s_id int)
AS
BEGIN
	INSERT INTO RequestSkill(
							Request_ID,
                            Skill_ID
                            )
					Values(
							r_id,
                            s_id);
END

*/
GO

CREATE PROCEDURE acceptTask(
@r_id int,
@p_id int)
AS
BEGIN
	-- Adds person and request to TaskAccept
	INSERT INTO TaskAccept(
							Request_ID,
                            Person_ID)
				Values(
						@r_id,
                        @p_id);
	
    -- Removes one person from max people needed, if 0 afterward, says it is filled
    UPDATE Request
	SET
		IsRequestFilled = CASE WHEN RequestMaxPeople <= 1 THEN 1 END,
		RequestMaxPeople = CASE WHEN RequestMaxPeople > 0 THEN RequestMaxPeople - 1 END
	WHERE
		Request_ID = @r_id;
        
END

GO

CREATE PROCEDURE removePersonFromTask(
@r_id int,
@p_id int)
AS
BEGIN
	-- Deletes person/request from task accept
	DELETE FROM TaskAccept
    WHERE Request_ID=@r_id AND Person_ID=@p_id;
	
    -- Changes request to incomplete and adds one to max people needed
    UPDATE Request
	SET
		IsRequestFilled = 0,
		RequestMaxPeople = RequestMaxPeople + 1
	WHERE
		Request_ID = @r_id;    

END

GO

CREATE PROCEDURE addPerson(
@uname varchar(255),
@fname varchar(255),
@lname varchar(255),
@email varchar(255)
)
AS
BEGIN
	-- Adds person to person table
    INSERT INTO Person(
						UserName,
						FirstName,
                        LastName,
						EmailAddress)
				Values(
						@uname,
                        @fname,
                        @lname,
                        @email);
END

GO

CREATE PROCEDURE addCategory(
@cname varchar(255),
@cdesc text)
AS
BEGIN
	-- Adds category to category table
    INSERT INTO Category(
						CategoryName,
                        CategoryDesc)
				Values(
						@cname,
                        @cdesc);

END

/* Removed skill proc for v1 (Anthony)

GO
CREATE PROCEDURE addSkill(
@sname varchar(255),
@sdesc text,
@c_id int)
AS
BEGIN
DECLARE s_id int;
	-- Adds skill to skill table
    INSERT INTO Skill(
						SkillName,
                        SkillDesc,
                        Category_ID)
				Values(
						sname,
                        sdesc,
                        c_id);
	-- Adds skill to skillcategory table
	SET s_id = last_insert_id();
    INSERT INTO SkillCategory(
								Category_ID,
                                Skill_ID)
						Values(
								c_id,
                                s_id);
END//

*/