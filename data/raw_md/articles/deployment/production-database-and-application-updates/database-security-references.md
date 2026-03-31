---
uid: "113237"
seealso:
- linkId: "113238"
- linkId: "113236"
title: Database Security References
---
# Database Security References

Your application may have an internal security strategy (see [Security System](xref:404204) section). However, that does not mean that a user who does not have an account in the application cannot gain direct access to the database. While, it is the job of a system administrator to protect the Database Server properly, it may be useful for a developer to understand basic security principles. In this lesson, you will learn how to make your database more secure.

We will consider two cases - End-User Workstations joined to a domain and End-User Workstations not joined to domain.

## Database Security in a Domain
If all End-User Workstations are joined to a domain, it is recommended to use an Active Directory authentication type in the application. Users will not have to provide credentials when starting the application. Instead, their Active Directory accounts will be used. The following security strategy is recommended.

* Set your Database Server security to Windows Authentication mode.
* Create a group in Active Directory. For instance, call it "XAF_Users". Add all the required end-user accounts to the newly created group.
* Provide this group with access to the application database in SQL server settings.
* Make sure that other users do not have access to the database.
* Configure your application to use Windows Authentication when connecting to the database. The sample connection string below illustrates this.
	
	# [XML](#tab/tabid-xml)
	
	```XML
	<add name="ConnectionString" connectionString="Integrated Security=SSPI;
	    Pooling=false;Data Source=DBSERVER;Initial Catalog=MySolution;" />
	```
	
	***
	
	For details, refer to the [Set Up the Database Connection](xref:113236) lesson.
* With this strategy, database access management can be easily performed. To restrict access to the database, remove a user from the "XAF_User" group. To grant access, add a user to this group.

> [!NOTE]
> Refer to your DBMS and Windows Server documentation for detailed information on the steps above.

## Database Security without a Domain
If End-User Workstations are not joined to a domain, you should use a Standard authentication type in the application. Users will have to provide credentials when logging into the application. The following security strategy is recommended.

* Set your Database Server security to SQL Server Authentication mode.
* Create a login in SQL server. For instance, call it "XAF_User".
* Allow this user to access the application database in SQL server settings.
* Make sure that other users do not have access to the database.
* Configure your application to use the "XAF_User" account when connecting to the database. The sample connection string below illustrates this.
	
	# [XML](#tab/tabid-xml)
	
	```XML
	<add name="ConnectionString" connectionString="Integrated Security=False;
	     Pooling=false;Data Source=DBSERVER;Initial Catalog=MySolution;
	     User ID=XAF_User;Password=PASSWORD;" />
	```
	
	***

> [!NOTE]
> Refer to your DBMS documentation for detailed information on the steps above.

## ASP.NET Core (Blazor and Web API Service) Security Specifics

It is not safe to keep a connection string that contains username and password in a plain text configuration file. You can persist it using a secret manager (e.g. [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault), [k8s Secrets](https://kubernetes.io/docs/concepts/configuration/secret/), etc.) or encrypt the _appsetting.json_ file.

It is recommended that you backup the database frequently. If something goes wrong, you will always have the ability to restore data. Refer to your DBMS documentation to find out how to set up automatic database backup or ask the database administrator to do it.

> [!NOTE]
> Since the application database can contain the personal data of end-users, ensure that the database backups are not publicly accessible.

To learn how to connect remote desktop clients to the Terminal Server with your Windows Forms application installed, refer to the [Connect Clients to the Terminal Server](xref:113244) lesson. If you are not deploying a Windows Forms application to the Terminal Server, refer to the [Application Update](xref:113239) lesson to learn how to update your application.
