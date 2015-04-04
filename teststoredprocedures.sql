-- Test Stored Procedures

CALL addPerson(
	'Anthony', 			-- First name
    'Marquez'); 		-- Last Name

CALL addRequest(
	'Request1',
    'This is a request yes it is',
    3,
    2,
    1);