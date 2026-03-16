---
uid: "113209"
seealso:
- linkId: "113293"
- linkId: "113340"
title: EasyTest Configuration
owner: Ekaterina Kiseleva
---
# EasyTest Configuration

One of the EasyTest components is the test configuration file. This topic describes the purpose of the configuration file and its format. For general information on how to run test scripts, refer to the [Run Tests](xref:113210) topic.

To be able to perform a test script, EasyTest requires the _Config.xml_ configuration file to be present in the directory containing the test script. You can have as many test script files in a folder as required, and only one configuration file is needed. If it is not present in the folder, EasyTest will not be able to perform tests. The configuration file serves as the central store for configuration information. Configuration settings such as the definitions of the applications to be tested and test databases to be used are stored in this file. There are two main benefits of having the configuration information stored separately in the configuration file. First, if you need to change a particular setting, you can easily do it in a single place. Second, since the configuration information is separated from the actual testing procedures, you can use a single set of test scripts to test different XAF applications.

The configuration file is an XML file with the `Options` root element. This element has a single `DefaultTimeout` attribute that specifies the default testing time limit in minutes. The `Options` element also has several child elements that contain configuration information. These elements are [Applications](#applications-element), [TestDatabases](#testdatabases-element) and [Aliases](#aliases-element). Let's take a closer look at these elements.

## Applications Element
This element contains definitions of the applications that can be tested by the test scripts located in the configuration file's folder. You can define as many applications as required. This has no direct effect on test scripts. Each test script in turn, must contain at least one reference to an application defined in the configuration file. The `Applications` element comprises `Application` elements, whose format differs for Windows Forms applications. The following tables describe this format.

| Attribute | Description |
|---|---|
| `Name` | Specifies the name of the `Application` element. This name is used to differentiate between different applications. The `Application` [command](xref:113208) takes this name as the parameter. |
| `FileName` | Specifies the fully qualified name of the application's executable file. You can use the built-in `[ConfigPath]` alias to specify a path relative to the _Config.xml_ file location. |
| `Arguments` | Optional. Specifies the command-line arguments passed to the application when it is started. |
| `AdapterFileName` | The path to the WinForms EasyTest adapter. To use the standard adapter, specify the following path: _%PROGRAMFILES%\DevExpress <:xx.x:>\\Components\Bin\NetCore\DevExpress.ExpressApp.EasyTest.WinAdapter.v<:xx.x:>.dll_ | 
| `CommunicationPort` | Specifies the communication port number that will be used by EasyTest when testing the application. |

The following code snippet illustrates a sample `Applications` element.

# [XML](#tab/tabid-xml)

```XML
<Applications>
  <Application 
    Name="MyTestSolutionWin" 
    FileName="[ConfigPath]\..\MySolution.Win\TestSolutionWin.exe" 
    Arguments="-Debug" 
    AdapterFileName="%PROGRAMFILES%\DevExpress <:xx.x:>\Components\
        Bin\NetCore\DevExpress.ExpressApp.EasyTest.WinAdapter.v<:xx.x:>.dll" 
    CommunicationPort="4100"/>
</Applications>
```

***


## TestDatabases Element
This element contains database definitions used by the `DropDB` and `RestoreDB` [script commands](xref:113208). You can define as many databases as you want. Since the database definitions are only required for the `DropDB` and `RestoreDB` commands, the `TestDatabases` element can be empty if your scripts do not use these commands.

EasyTest can use either Microsoft SQL Server or Microsoft Access (Jet) databases for testing purposes. The `TestDatabases` element consists of the `Database` elements whose format varies for different database management systems. For the Microsoft SQL Server databases, the `Database` element has the following format.

| Attribute | Description |
|---|---|
| `xsi:type` | Specifies the type of the database in use. For Microsoft SQL Server databases the value is _TestMSSQLDatabase_. |
| `Server` | Specifies the SQL server instance name. For example, this attribute can be _(local)_ for Microsoft SQL Server or _(localdb)\mssqllocaldb_ for Microsoft SQL Server Express LocalDB. |
| `DBName` | Specifies the database name. The `DropDB` and `RestoreDB` commands take this name as the parameter. |
| `BackupFileName` | Optional. Specifies the fully qualified name of the database backup file. This attribute is required by the `RestoreDB` command. You can use the built-in `[ConfigPath]` alias to specify path relative to the _Config.xml_ file location. |

An optional `Login` element is available for the Microsoft SQL Server databases.

| Attribute | Description |
|---|---|
| `UserID` | Specifies the login that must be used when accessing the database. |
| `Password` | Specifies the password that must be used when accessing the database. |

For the Microsoft Access databases, the `Database` element has the following format.

| Attribute | Description |
|---|---|
| `xsi:type` | Specifies the type of the database in use. For Microsoft Access databases, the value is _TestAccessDatabase_. |
| `DBSourceLocation` | Specifies the fully qualified database file name. You can use the built-in `[ConfigPath]` alias to specify a path relative to the _Config.xml_ file location. |
| `DBName` | Specifies the database name. The `DropDB` and `RestoreDB` commands take this name as the parameter. |
| `BackupFileName` | Optional. Specifies the fully qualified filename of the database backup file. This attribute is required to use the `RestoreDB` command. You can use the built-in `[ConfigPath]` alias to specify a path relative to the _Config.xml_ file location. |

The following code snippet illustrates a sample `TestDatabases` element.

# [XML](#tab/tabid-xml)

```XML
<TestDatabases>
    <Database xsi:type="TestMSSQLDatabase" 
              Server="(local)" 
              DBName="MySolutionTestDatabase" 
              BackupFileName="\\TestServer\Backups\MySolutionTestDatabase_backup.dbbak">
        <Login UserID="" Password=""/>
    </Database>
    <Database xsi:type="TestMSSQLDatabase" 
              Server="(localdb)\mssqllocaldb" 
              DBName="MySolutionTestDatabaseWin"/>
    <Database xsi:type="TestAccessDatabase" 
              DBSourceLocation="D:\Test\MySolution.mdb" 
              DBName="AccessTestDatabase"/>
</TestDatabases>
```

***

## Aliases Element

The `Aliases` element is used to define EasyTest configuration aliases. EasyTest aliases can be thought of as environment variables. To use an alias, you first need to define it in the `Aliases` element and assign a value to it. Then, the alias name can be used in configuration files and in script files. When a test script is performed, the alias name found in the configuration or script files is replaced with the alias value. You can use existing aliases when defining a new alias. Additionally, you can use Windows environment variables, to specify an alias value.

The `Aliases` element consists of the `Alias` elements, which have the following format.

{|
|-

! Attribute
! Description
|-

| `Name`
| Specifies the alias name.
|-

| `Value`
| Specifies the alias value.
|-

| `ProfileName`
| Optional. Specifies the profile with which the alias is associated. Profiles allow an alias to have several values. So, you can define several aliases using the same name by specifying different profiles. 
This attribute is used by the [TestExecutor utility](xref:113210). This utility takes a command-line argument, which specifies the profile to be used.
|}

To use an alias in the configuration file or test scripts, enclose the alias name in square brackets.

The following code snippet illustrates a sample `Aliases` element.

# [XML](#tab/tabid-xml)

```XML
<Aliases>
    <Alias Name="DomainUserName" Value="%USERDOMAIN%\%USERNAME%"/>
    <Alias Name="TestsPath" Value="D:\Tests"/>
    <Alias Name="TestsPath" Value="S:\GlobalTests" ProfileName="Global"/>
    <Alias Name="Version" Value="v"/>
    <Alias Name="Port" Value="4125"/>
    <Alias Name="Url" Value="http://localhost:[Port]"/>
</Aliases>
```

***

There is also a built-in `ConfigPath` alias whose value is the configuration file location (as its name implies). For instance, you can use this alias when specifying `FileName` and `PhysicalPath` values.
