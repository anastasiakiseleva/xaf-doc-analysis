---
uid: "113236"
title: Set Up the Database Connection for a Deployed Application
seealso:
- linkId: 113239#how-database-is-updated-in-debug-mode
  altText: How Database is Updated in Debug Mode
- linkId: "113238"
- linkId: 404290
---
# Set Up the Database Connection for a Deployed Application

This lesson explains how to connect your application to a database server, create an initial database, and resolve database and application version mismatches.

> [!NOTE]
> This topic describes how to set up database connections for WinForms and Blazor XAF application. For other cases, for instance, non-Windows deployment to Azure AppService or Linux, see topics from the following help section: [Deployment Recommendations for XAF Blazor UI Applications](xref:403362).

1. Run the application at the target workstation or server. Ensure there are no missing assemblies or other non-database-specific errors. The application should display the "_The application cannot connect to the specified database, because the latter does not exist, or its version is older than that of the application" message. If you see another message, review the lesson you followed to deploy the application.
1. Ensure that your database server is up and running. The database server must also accept remote connections.
1. Open the application configuration file and find the following line:
	* _MySolution.Blazor.Server\appsettings.json_ for Blazor/WebAPI applications
	* _MySolution.Win\App.config_ for WinForms applications

	# [Blazor (EF Core)](#tab/tabid-json1)
	
	```JSON
	"ConnectionString": "Integrated Security=SSPI;Pooling=true;MultipleActiveResultSets=true;
		Data Source=(localdb)\\mssqllocaldb;Initial Catalog=MySolution",
	```
	# [Blazor (XPO)](#tab/tabid-json2)
	
	```JSON
	"ConnectionString": "Integrated Security=SSPI;Pooling=false;
		Data Source=(localdb)\\mssqllocaldb;Initial Catalog=MySolution",
	```

	# [WinForms (EF Core)](#tab/tabid-xml1)
	
	```XML
	<add name="ConnectionString" connectionString="Integrated Security=SSPI;MultipleActiveResultSets=True;
		Data Source=(localdb)\mssqllocaldb;Initial Catalog=MySolution" />
	```

	# [WinForms (XPO)](#tab/tabid-xml2)
	
	```XML
	<add name="ConnectionString" connectionString="Integrated Security=SSPI;Pooling=false;
		Data Source=(localdb)\mssqllocaldb;Initial Catalog=MySolution" />
	```
	***
	
	Substitute `(localdb)\mssqllocaldb` with the database server name or its IP address. Use `localhost` or `(local)` if you use a local database server.
	
	If your database server authentication mode is SQL Server Authentication, disable integrated security and add user credentials.
	
	# [Blazor (EF Core)](#tab/tabid-json1)
	
	```JSON
	"ConnectionString": "Integrated Security=False;Pooling=true;MultipleActiveResultSets=true;
		Data Source=YOUR_DB_SERVER;Initial Catalog=MySolution;User ID=YOUR_USER_ID;Password=YOUR_PASSWORD",
	```
	# [Blazor (XPO)](#tab/tabid-json2)
	
	```JSON
	"ConnectionString": "Integrated Security=False;Pooling=false;MultipleActiveResultSets=true;
		Data Source=YOUR_DB_SERVER;Initial Catalog=MySolution;User ID=YOUR_USER_ID;Password=YOUR_PASSWORD",
	```

	# [WinForms (EF Core)](#tab/tabid-xml1)
	
	```XML
	<add name="ConnectionString" connectionString="Integrated Security=False;MultipleActiveResultSets=True;
		Data Source=YOUR_DB_SERVER;Initial Catalog=MySolution;User ID=YOUR_USER_ID;Password=YOUR_PASSWORD" />
	```

	# [WinForms (XPO)](#tab/tabid-xml2)
	
	```XML
	<add name="ConnectionString" connectionString="Integrated Security=False;Pooling=false;
		Data Source=YOUR_DB_SERVER;Initial Catalog=MySolution;User ID=YOUR_USER_ID;Password=YOUR_PASSWORD" />
	```
	***
	
	> [!NOTE]
	> An account used to run the application must have appropriate permissions at the database server. You can use an administrative account for training purposes and set up a limited account later (see [Database Security References](xref:113237) lesson).

1. Launch a command line interpreter, for instance, **Command Prompt**. Run your application with the `-updateDatabase` command and follow the on-screen instructions. The update mechanism connects to the database server, determines that the application database does not yet exist, and creates it. If the database exists, the mechanism updates the database structure.

	Refer to the following topic for additional details: <xref:113239>.

1. Run the application and ensure that the database is successfully created or updated. 

	![Deployment_Tutorial_0090](~/images/deployment_tutorial_0090116471.png)

1. Your local database on the Developer Workstation may contain objects created while developing and debugging an application. If you want this data to be accessible to users, create a database backup on the Developer Workstation and restore it on the database server with Microsoft SQL Server Management Studio. Connect to a local database server at the Developer Workstation. Right-click your database name in Object Explorer and choose **Tasks** | **Back Up…** | **Database…**. Select a backup destination in the invoked dialog and click OK. Connect to the database server. Right-click your database name in Object Explorer and choose **Tasks** | **Restore…** | **Database…**. Select the backup file in the invoked dialog and click OK. Run the application to view the objects created when developing and debugging the application.
	
	![Deployment_Tutorial_0110](~/images/deployment_tutorial_0110116472.png)
	
	> [!NOTE]
	> If you made changes to the application solution after deployment, you will get an error, stating a database and application version mismatch: "An error with number 1111 has occurred.
	> Error message: The database version is greater than the application version. The application needs to be updated. Please contact your system administrator or download a new version.". In this instance, update the application as described in the [Application Update](xref:113239) lesson.

Follow the [Database Security References](xref:113237) lesson recommendations to make your database more secure.
