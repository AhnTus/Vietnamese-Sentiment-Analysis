use SalesPhone
go
CREATE Or Alter PROCEDURE CheckLogin
    @Username NVARCHAR(50),
    @Password NVARCHAR(50)
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @Count INT;
    
    SELECT @Count = COUNT(*) 
    FROM Users 
    WHERE Username = @Username AND Password = @Password;

    IF @Count > 0
        SELECT 1 AS LoginSuccess;  -- Return 1 if login is successful
    ELSE
        SELECT 0 AS LoginSuccess;  -- Return 0 if login is unsuccessful
END;