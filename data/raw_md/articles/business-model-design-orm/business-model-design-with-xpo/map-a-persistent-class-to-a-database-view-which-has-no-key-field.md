---
uid: "113281"
seealso:
- linkId: DevExpress.Xpo.XPLiteObject
- linkId: DevExpress.Xpo.KeyAttribute
- linkId: DevExpress.Xpo.PersistentAttribute
- linkId: "113146"
- linkId: "113451"
- linkId: 403909
  altText: How to map a persistent object to a view which does not have a key column
title: 'Map a Persistent Class to a Database View Which Has No Key Field'
owner: Ekaterina Kiseleva
---
# Map a Persistent Class to a Database View Which Has No Key Field

With XAF, you can build new applications from scratch or maintain existing databases. The [How to: Generate XPO Business Classes for Existing Data Tables](xref:113451) topic describes how to use the design-time wizard that generates business classes for one or more data tables in the specified database at the same time. Additionally, the existing database can contain views (stored queries), which need to be accessed in an XAF application's List Views, Analysis, and Reports. If the database view has a key column, you can map a persistent class to it using the same approach as mapping to a regular table.

This topic describes how to implement a persistent class mapped to a database view without a key.

> [!NOTE]
> This approach uses composite keys, which are not supported in the ASP.NET Core Blazor applications, and works only for WinForms applications.

1. Create a new XAF solution and follow the steps from the [How to: Generate XPO Business Classes for Existing Data Tables](xref:113451) topic. Do not forget to modify the connection string that connects your application to the _nwind.mbd_ database.
2. Open the _nwind.mbd_ database to see what views (queries) it contains. You can use Microsoft Office Access or any other MDB viewer application. In this example, the **CustomerReports** view is mapped to the `CustomerReports` persistent class:
	
	![MapDatabaseView_1](~/images/mapdatabaseview_1116672.png)
	
	> [!NOTE]
	> This view contains the `ProductName`, `CompanyName`, `OrderDate` and `ProductAmount` fields. These names are used when implementing the `CustomerReports` class.
3. Create a new `CustomerReports` persistent class (you can use the **DevExpress <:xx.x:> ORM Persistent Object** template). Replace the automatically generated class declaration with the following code:
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using System;
	using System.ComponentModel;

	using DevExpress.ExpressApp.Xpo.Utils;
	using DevExpress.Persistent.Base;
	using DevExpress.Xpo;
	// ...
    [DefaultClassOptions]
    public class CustomerReports : XPLiteObject {
        public CustomerReports(Session session) : base(session) { }
        CustomerReportsViewKey fKey;
        [Key, Persistent]
        public CustomerReportsViewKey Key {
            get { return fKey; }
            set { SetPropertyValue(nameof(Key), ref fKey, value); }
        }
        [PersistentAlias("Key.ProductName")]
        public string ProductName { get { return Key.ProductName; } }
        [PersistentAlias("Key.CompanyName")]
        public string CompanyName { get { return Key.CompanyName; } }
        [PersistentAlias("Key.OrderDate")]
        public DateTime OrderDate { get { return Key.OrderDate; } }
        [PersistentAlias("Key.ProductAmount")]
        public string ProductAmount { get { return Key.ProductAmount; } }
    }
    [TypeConverter(typeof(StructTypeConverter<CustomerReportsViewKey>))]
    public struct CustomerReportsViewKey {
        [Persistent("ProductName"), Browsable(false)]
        public string ProductName;
        [Persistent("CompanyName"), Browsable(false)]
        public string CompanyName;
        [Persistent("OrderDate"), Browsable(false)]
        public DateTime OrderDate;
        [Persistent("ProductAmount"), Browsable(false)]
        public string ProductAmount;
    }
	```

	***
	
	Each persistent class requires a primary key. The `CustomerReports` class is an [](xref:DevExpress.Xpo.XPLiteObject) descendant and does not have a key property generated automatically. For this reason, the example implements the composite `Key` property (a key formed by combining multiple columns).
	
	The `CustomerReportsViewKey` struct defines the columns that form the composite key. The struct uses the [TypeConverter](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.typeconverter) attribute so XAF can convert composite key values and process objects.
	
	Additionally, the `CustomerReports` class exposes properties corresponding to all the view's columns. You can omit any property, but the composite key should still include all columns.
	
	> [!NOTE]
	> * A database view can already have a key column. In this case, you do not need the composite key, and you should decorate the key property with the [](xref:DevExpress.Xpo.KeyAttribute).
	> * The number of columns included in the composite key is limited. For instance, Microsoft SQL Server allows a maximum of 16 columns.
	
	If you do not want your class to have the same name as the database view, you can use a custom name, and decorate the class with the [](xref:DevExpress.Xpo.PersistentAttribute):
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	[DefaultClassOptions, Persistent("CustomerReports")]
	public class MyCustomerReports : XPLiteObject {
	    // ...
	}
	```

	***
4. Run the application. The "Customer Reports" object is available.
	
	![MapDatabaseView_2](~/images/mapdatabaseview_2116673.png)
	
	You can use the `CustomerReports` class as the Data Type in [Reports V2](xref:113591):
	
	![MapDatabaseView_3](~/images/mapdatabaseview_3116674.png)
