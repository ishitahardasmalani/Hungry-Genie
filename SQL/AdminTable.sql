CREATE TABLE Admin
(
	AdminId int auto_increment key,
	AdminName varchar(200),
	AdminPassword varchar(200),
    AdminEmail varchar(200),
    AdminPhoto varchar(500)
)

Insert into Admin(AdminName,AdminPassword,AdminEmail,AdminPhoto)
Values('Ishita','ABC','ishitah@gmail.com','user.jpg')
