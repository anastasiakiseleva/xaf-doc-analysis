---
uid: "113451"
seealso:
- linkId: "113281"
title: 'Generate XPO Business Classes for Existing Data Tables'
owner: Ekaterina Kiseleva
---
# Generate XPO Business Classes for Existing Data Tables

From other documentation sources, you learned how to create business classes for your XAF applications. If you have business classes in your application, you have database tables in the application's database. However, the reality is that most programmers are not building new applications from scratch, but maintaining existing databases. In this instance, they can use the [XPO Data Model Wizard](xref:14810) that generates a business model declaration for the specified legacy database. Follow the steps below to generate business classes for your existing database that you are going to use in your XAF application.

If you prefer to watch a video rather than walk through these step-by-step instructions, you can access a corresponding tutorial in our YouTube Channel: [XAF: Create an Application Based on the Existing Database](https://www.youtube.com/watch?v=vw5ZnJ-9Iyw).

## Generate an XPO Data Model
* Create a new XAF solution using the DevExpress [Template Kit](xref:405447).
* Right-click the _BusinessObjects_ folder located in the [module project](xref:118045). Choose **Add** | **New Item**. In the invoked **Add New Item** dialog, choose the **DevExpress ORM Data Model Wizard** template located in the **DevExpress** category. Set the new item's name to **MySolutionDataModel.xpo** and click **Add**. You will see that the _MySolutionDataModel.xpo_ item is added and the wizard dialog is invoked.
* In the invoked wizard dialog, choose **Map to an existing database** and click **Next**.
	
	![XpoDesigner_LegacyDB_Wizard1](~/images/xpodesigner_legacydb_wizard1117140.png)
* Specify connection settings to the database containing the target data. The wizard supports multiple database systems (Microsoft SQL Server, DB2, MySql, Firebird, and so on). Use the **Provider** combo box to select the required database type. Note that the corresponding database provider assembly must be registered in the Global Assembly Cache (GAC) on your machine or the wizard will fail. In this example, we will use the "Northwind Traders" demo database. This database is shipped with DXperience and installed in _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\Components\Data\nwind.mdb_, by default.
	
	![XpoDesigner_LegacyDB_Wizard2](~/images/xpodesigner_legacydb_wizard2117141.png)
	
	Click **Next** after connection settings have been specified.
* In the next step, the wizard displays a list of tables that can be mapped to persistent classes.  Select a table(s) to be mapped to a persistent object(s) and for each table select columns that will be mapped to the persistent object's properties. For unchecked columns, persistent properties will not be generated. For instance, select the **Customers** and **Orders** tables.
	
	![XpoDesigner_LegacyDB_Wizard3](~/images/xpodesigner_legacydb_wizard3117142.png)
* Click **Next** to close the wizard. The generated data model will be shown in the **XPO Data Model** designer.
	
	![XpoDesigner_LegacyDB_Designer](~/images/xpodesigner_legacydb_designer117143.png)
	
	If you want to customize the generated data model, refer to the [How to: Create a Business Model in the XPO Data Model Designer](xref:113450) topic. The names of persistent classes and their properties match the names of selected tables and their columns. In the current sample, the table names are in plural form. So, you may want to change class names (`Customers` to `Customer` and **`Orders`** to `Order`). To rename a class or its property, select it in the designer and change the **Name** in the **Properties** window. The classes and properties with modified names will still be mapped to corresponding tables and columns, as the [](xref:DevExpress.Xpo.PersistentAttribute) is automatically added to the designer-generated code.
* In the **Visual Studio** toolbar, click save. The generated code files will appear in the **Solution Explorer**, in the _BusinessObjects\MySolutionDataModelCode_ folder.
	
	![XpoDesigner_LegacyDB_SolutionExplorer](~/images/xpodesigner_legacydb_solutionexplorer117144.png)
	
	> [!NOTE]
	> If you do not like to deal with the designer and prefer to do everything in code, create a separate code file and copy the generated classes into it. Then, remove files that are added by the designer.

## Add XAF-Specific Attributes in Code
* Open the _Customer.cs_ (_Customer.vb_) file. Decorate the `Customer` class with the [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) and [](xref:DevExpress.Persistent.Base.ImageNameAttribute) attributes. As the result, the `Customer` object will be added to the [Navigation System](xref:113198) and an icon from the built-in library will be associated with this object.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.Persistent.Base;
	// ...
	[DefaultClassOptions, ImageName("BO_Contact")]
	public partial class Customer{
	    public Customer(Session session) : base(session) { }
	    public Customer() : base(Session.DefaultSession) { }
	    public override void AfterConstruction() { base.AfterConstruction(); }
	}
	```
	
	***
* Open the _Order.cs_ (_Order.vb_) file. Decorate the **Order** class with the **DefaultClassOptions** and **ImageName** attributes.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.Persistent.Base;
	// ...
	[DefaultClassOptions, ImageName("BO_Order")]
	public partial class Order {
	    public Order(Session session) : base(session) { }
	    public Order() : base(Session.DefaultSession) { }
	    public override void AfterConstruction() { base.AfterConstruction(); }
	}
	```

	***

You can add more custom code to the auto-generated classes (for example, override base class methods). Do not change code located in files with the _designer_ suffix - they contain designer-generated code and should not be modified manually. The generated classes are declared as _partial_. Designed and custom class parts are located in different files.

> [!NOTE]
> We recommend that you use the `System.ComponentModel.DefaultProperty` attribute to specify the [default property](xref:113525) for each generated class  Default property is treated as a human-readable identifier in an XAF application UI.

> [!IMPORTANT]
> You cannot apply attributes to properties in the partial class' code. Instead, use the designer (see the next section).

## Add XAF-Specific Attributes in the Designer
Alternatively, you can use the designer to apply attributes. Focus the requires class or field and specify the **Custom Attributes** setting in the **Properties** window.

![CustomAttributes](~/images/customattributes132225.png)

## Specify the Connection String
An empty XAF application is generated with a default connection string: `Data Source=(localdb)\mssqllocaldb;Initial Catalog=MyApplication;Integrated Security=SSPI;Pooling=false`. You should change it, so that the application uses the required database. Change the connection string in the application configuration file. You can copy the valid connection string from the auto-created _MySolution.Module\app.config_ file.

## Run the Application
Now you can run the application to see the result. The application is completely based on the business model generated for the legacy database.

![XAF Windows Forms, DevExpress](~/images/xpodesigner_legacydb_runtimewin117145.png)



